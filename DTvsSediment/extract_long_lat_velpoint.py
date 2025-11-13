import pygplates
import geopandas as gpd
import glob

# Load the global coastline features.
lat_lon_files = [
    f'../Reconstructions/For_gld428/lat_lon_velocity_domain_720_1440_with_plate_IDs_with_ages_for_gld428.gpml',
    f'../Reconstructions/For_gld504/lat_lon_velocity_domain_720_1440_with_plate_IDs_with_ages_for_gld504.gpml',
    f'../Reconstructions/1.8Ga/Points_for_plate_frame/lat_lon_velocity_domain_720_1440_with_plate_IDs_and_ages.gpml',
    f'../Reconstructions/1.8Ga/Points_for_plate_frame/lat_lon_velocity_domain_720_1440_with_plate_IDs_and_ages.gpml',
    f'../Reconstructions/1.8Ga/Points_for_plate_frame/lat_lon_velocity_domain_720_1440_with_plate_IDs_and_ages.gpml',
    f'../Reconstructions/1.8Ga/Points_for_plate_frame/lat_lon_velocity_domain_720_1440_with_plate_IDs_and_ages.gpml'

]

models =['gld428', 'gld504','gld560', 'gld564', 'gld563', 'gld565']

# plate_id_reference ={'601':'NCC',
#         #'602':'SC',
#         '7703' : 'KAL',
#         '701' : 'CON',
#         '77144' : 'WAC',
#         '803':'ANC',
#         '802' : 'ANC',
#         #'8013':'ANC',
#         '8011': 'AUS',
#         '201': 'AMZ',
#         #'26' :'AN',
#         '302': 'BAL',
#         '401' :'SIB',
#            }
#plate_id = 302

plate_ids = [601] #[101, 301, 701, 201, 801]
startswith = ['601'] #['1', ('3','4','501','502','503','510','60'), '7', '2', '801']
names= ['NCC'] #['LAU', 'EAS', 'AFR', 'AMZ', 'AUS']

for name, plate_id, startwith in zip(names, plate_ids, startswith):
    
    for model, pts in zip(models, lat_lon_files):
        
        input_feature_collection = pygplates.FeatureCollection(pts)
        
        # Start with an empty list of coastline features on plate 101.
        features_in_plateid = []
        
        # Iterate over all coastline features and add those on plate 101 or starting with 1 to 'features_in_plate_101'.
        for feature in input_feature_collection:
            
            if feature.get_reconstruction_plate_id() == plate_id or str(feature.get_reconstruction_plate_id()).startswith(startwith):
                features_in_plateid.append(feature)
        
        # Write the coastline features for plate 801 to a new file.
        output_feature_collection = pygplates.FeatureCollection(features_in_plateid)
        output_feature_collection.write(f'{model}_{name}_{plate_id}.gpml')
        
        print(f"Filtered GPML file saved to {output_feature_collection}")