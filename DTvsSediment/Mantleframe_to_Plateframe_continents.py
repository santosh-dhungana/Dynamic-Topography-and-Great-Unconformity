# Points projections using old framework
import pygplates
#import PyGPlates_PlateFrameRasters
import sys
import os
import shutil
import xarray as xr
import rioxarray as rxr
import glob
import os
#from optparse import OptionParser
from scipy.io import netcdf_file as netcdf
from scipy.interpolate import RectBivariateSpline
import pandas as pd
import geopandas as gpd

def GetReconstructedMultipoint(reconstructed_feature_geometry):
    
    """Takes in reconstructed_feature_geometry and returns reconstructed lats, lon along with present day lats and lons

    -reconstructed_feature_geometry
    -retruns: reconstructed lats, lons and present day lat, lons
    """

    # Get the reconstructed geometry and the associated present day geometry.
    reconstructed_multipoint_geometry = reconstructed_feature_geometry.get_reconstructed_geometry()
    # present_day_multipoint_geometry = pygplates.get_geometry_from_property_value(
    #         reconstructed_feature_geometry.get_property().get_value(),
    #         pygplates.MultiPointOnSphere)
    # Get the reconstructed feature's geometry
    reconstructed_geometry = reconstructed_multipoint_geometry
    present_day_multipoint_geometry = reconstructed_feature_geometry.get_present_day_geometry()
    # If the geometry is a MultiPointOnSphere, ensure you cast or handle the geometry accordingly
    if isinstance(present_day_multipoint_geometry, pygplates.MultiPointOnSphere):
        present_day_multipoint_geometry = present_day_multipoint_geometry
    else:
        # Handle other types of geometry if needed
        present_day_multipoint_geometry = None
        
    reconstructed_points = list(reconstructed_multipoint_geometry)
    present_day_points = list(present_day_multipoint_geometry)
    reconstructed_lat_points = []
    reconstructed_lon_points = []
    present_day_lat_lon_points = []
    # Iterate over the points in both multipoints (they should both have the same number of points).
    num_points = len(reconstructed_multipoint_geometry)
    # print 'num points in multipoint: %d' % num_points
    for point_index in range(0, num_points):
        # Index into the multipoint to get pygplates.PointOnSphere's.
        reconstructed_lat_lon_mp = pygplates.convert_point_on_sphere_to_lat_lon_point(reconstructed_points[point_index])
        reconstructed_lat_points.append(reconstructed_lat_lon_mp.get_latitude())
        reconstructed_lon_points.append(reconstructed_lat_lon_mp.get_longitude())
        present_day_lat_lon_mp = pygplates.convert_point_on_sphere_to_lat_lon_point(present_day_points[point_index])
        present_day_lat_lon_points.append((present_day_lat_lon_mp.get_latitude(), present_day_lat_lon_mp.get_longitude()))

    return (reconstructed_lon_points, reconstructed_lat_points, present_day_lat_lon_points)

def GeneratePlateReferenceFrameXYZ(rotation_model,reconstruction_time,multipoint_feature_collection,InputGridFile):
  
    data =  rxr.open_rasterio(InputGridFile).drop_vars('spatial_ref').sel(band=1).rename({'x':'lon', 'y':'lat'})#netcdf(InputGridFile,'r')
    if data.lon.min().values < 0:
        data = data.sortby('lon', ascending=True)  
        data = data.sortby('lat', ascending=True) 
        #print('I was in if loop')
    else:
        #print('I was in else loop')
        data['lon'] = data['lon'].where(data['lon'] <= 180, data['lon'] - 360)
        data = data.drop_duplicates(dim='lon')  # Drop duplicates based on longitude ('x')
        data = data.drop_duplicates(dim='lat') 
        data = data.sortby('lon', ascending=True)  # Sort by longitude
        data = data.sortby('lat', ascending=True) 
        #data = netcdf(InputGridFile,'r')
    # else:
    #     data =#netcdf(InputGridFile,'r')
    with open('output', 'w') as output_file:
        # Create an interpolation object for this grid
        
        #f=RectBivariateSpline(data.variables['lon'][:],data.variables['lat'][:],data.variables['z'][:].T)
        f=RectBivariateSpline(data['lon'][:],data['lat'][:],data[:].T)
        # Reconstruct the multipoint features into a list of pygplates.ReconstructedFeatureGeometry's.
        reconstructed_feature_geometries = []
        pygplates.reconstruct(multipoint_feature_collection, rotation_model, reconstructed_feature_geometries, reconstruction_time)
        print ('num reconstructed multipoint geometries: %d' % len(reconstructed_feature_geometries))
        with open ('check', 'w') as check_file:
            for reconstructed_feature_geometry in reconstructed_feature_geometries:
                
                reconstructed_lon_points, reconstructed_lat_points, present_day_lat_lon_points = GetReconstructedMultipoint(reconstructed_feature_geometry)
                num_points = len(reconstructed_lon_points)
                
                # evaluate the current grid at the multipoint coordinates of the current feature
                gridZr = f.ev(reconstructed_lon_points, reconstructed_lat_points)

                # append the interpolated points as lon,lat,Z triples to an ascii file
                for point_index in range(0, num_points):
                    pdp = present_day_lat_lon_points[point_index]
                    output_file.write('%f %f %f %f\n' % (pdp[1], pdp[0], gridZr[point_index], reconstruction_time))
                    #check_file.write(f'{reconstruction_time} {reconstructed_lat_points[point_index]} {reconstructed_lon_points[point_index]}{present_day_lat_lon_points[point_index]}\n')
            

                

def GeneratePlateReferenceFramesXYZ(rotation_model,raster_times,raster_filenames,multipoint_feature_collection,output_file_stem, model):
    print(output_file_stem)
    for reconstruction_time_index in range(0,len(raster_times)):
    
        reconstruction_time = raster_times[reconstruction_time_index]
        InputGridFile = raster_filenames[reconstruction_time_index]
        print ('time: %d Ma' % reconstruction_time)
        #InputGridFile = GridDir+'gld9NLt-%d.topo_0.5d_corr.0.grd' % reconstruction_time 
        GeneratePlateReferenceFrameXYZ(rotation_model,reconstruction_time,multipoint_feature_collection,InputGridFile)

        cmd = f"gmt nearneighbor output -G%s{model}PlateFrameGrid%d.nc -Rd -I0.5d -N1 -S0.75d -V" % (output_file_stem,reconstruction_time)
        #cmd = "nearneighbor output -G%sPlateFrameGrid%d.nc -Rd -I0.25d -N1 -S0.75d -V" % (output_file_stem,reconstruction_time)
        #cmd = f"gmt nearneighbor output -G%sPlateFrameGrid%d.nc -Rd -I0.125d -N1 -S0.75d -V" % (output_file_stem,reconstruction_time)
        os.system(cmd)
        #print('I did my job')
        cmd = "rm output"
        os.system(cmd)

import re
# extract age from the mantlefraem grid files
# Optimized function that extracts the age and sorts the file paths
def sort_files_by_age(fpaths, match_string='Ma'):
    """
    This function extracts ages from file paths and sorts them (reverse/)chronologically.

    Parameters:
    fpaths: list of file paths
    match_string: the string to match before the age (default is 'Ma')

    Returns:
    Dictionary with the extracted age as the key and the sorted file paths as values
    """
    # Use a generator to extract ages and pair them with file paths
   
    def extract_age(file_name):
        match = re.search(f'{match_string}(\d+).', file_name)
        return int(match.group(1)) if match else float('inf')  # return inf if no match is found

    # Sort the file paths by the extracted age using a generator expression
    sorted_files = sorted(fpaths, key=lambda x: extract_age(x))
    
    # Return a dictionary with the age as the key and the file path as the value
    return {extract_age(file): file for file in sorted_files}

def main():
    #workdir = './'
    MODELLIST=[ 'gld486', 'gld504'] #]'gld560', 'gld563', 'gld564', 'gld565'] #'gld428', 'gld504',
    plate_ids = [101, 301, 701, 201, 801]
    continents= ['LAU', 'EAS', 'AFR', 'AMZ', 'AUS']
    print(MODELLIST)
    
    for model in MODELLIST:
        print(model)
        for plate_id, continent in zip(plate_ids, continents):
            if model in ['gld421']:
                input_rotation_filename = [ 
                    f'../Reconstructions/For_gld421/1000_0_rotfile_Merdith_et_al.rot',
                ]
                                           
                                           
                rotation_model = pygplates.RotationModel(input_rotation_filename)
                #input_multipoint_filename = f'Reconstructions/For_gld428/lat_lon_velocity_domain_720_1440_with_plate_IDs_with_ages_for_gld428.gpml'
                input_multipoint_filename = f'gld428_{continent}_{plate_id}.gpml'
                
            elif model in ['gld428', 'gld431', 'gld434']:
                input_rotation_filename = [ 
                    f'../Reconstructions/For_gld428/1000_410_rotations_NNR.rot',
                    f'../Reconstructions/For_gld428/Global_EB_410-250Ma_GK07_2017-NNR.rot',
                    f'../Reconstructions/For_gld428/Global_EB_250-0Ma_GK07_2017-NNR.rot',
                    f'../Reconstructions/For_gld428/NR_0Ma_1000Ma_for_gplates.rot'
                ]
                                           
                                           
                rotation_model = pygplates.RotationModel(input_rotation_filename)
                input_multipoint_filename = f'gld428_{continent}_{plate_id}.gpml'
                
            elif model in ['gld504','gld486']:
                input_rotation_filename = [
                    '../Reconstructions/For_gld504/1000_0_rotfile_Merdith_et_al_slightly_changed_for_nnr_nico_mod.rot',
                    '../Reconstructions/For_gld504/NR_0Ma_1000Ma_for_gplates_combine.rot'
                ]
                rotation_model = pygplates.RotationModel(input_rotation_filename)
                input_multipoint_filename = f'gld504_{continent}_{plate_id}.gpml'
        
                
            elif model in ['gld560', 'gld564']:
                input_rotation_filename = f'../Reconstructions/1.8Ga/optimisation/no_net_rotation_model_20240725_run3.rot',
                rotation_model = pygplates.RotationModel(input_rotation_filename)
                input_multipoint_filename = f'gld560_{continent}_{plate_id}.gpml'
                
            else:
                input_rotation_filename = f'../Reconstructions/1.8Ga/optimisation/optimised_rotation_model_20240725_run3.rot',
                print(f'I am using {input_rotation_filename} for gld563')
                rotation_model = pygplates.RotationModel(input_rotation_filename)
                input_multipoint_filename = f'gld563_{continent}_{plate_id}.gpml'
                  
           # print(rotation_model)
            
            #input_multipoint_filename = f'./Reconstructions/1.8Ga/Points_for_plate_frame/lat_lon_velocity_domain_720_1440_with_plate_IDs.gpml'
            if model in ['gld428']: #['gld428', 'gld504']:
                raster_files_path = glob.glob(f'../Model_data/{model}/lat*/*.grd')
            elif model == 'gld504':
                raster_files_path = glob.glob(f'../Model_data/{model}/Latitude*/*.grd')
                
            else:
                raster_files_path = glob.glob(f'../Model_data/{model}/lat*/*.grd')
            
            raster_filenames = list(sort_files_by_age(raster_files_path, match_string = f'{model}NLt-').values())
            raster_times = list(sort_files_by_age(raster_files_path, match_string = f'{model}NLt-').keys())
            print(raster_filenames[:2])
            
            output_file_dir = f'{model}/' 
            output_file_stem = f'{model}/PlateFrameGrid_{continent}/'
            
            if not os.path.exists(output_file_dir):
                os.makedirs(output_file_dir)
            if not os.path.exists(output_file_stem):
                os.makedirs(output_file_stem)
                
            #rotation_model = pygplates.RotationModel(input_rotation_filename)
            
            file_registry = pygplates.FeatureCollectionFileFormatRegistry()
            print ('Reading multipoint data...')
            multipoint_feature_collection = file_registry.read(input_multipoint_filename)
            
                #PyGPlates_PlateFrameRasters.main()
            GeneratePlateReferenceFramesXYZ(rotation_model, raster_times, raster_filenames, multipoint_feature_collection, output_file_stem, model)

if __name__ == "__main__":
    main()