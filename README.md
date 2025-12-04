Online supplement for:

			The Deep Earth Origin of the Great Unconformity

Santosh Dhungana, Nicolas Flament*
Environmental Futures, School of Science, University of Wollongong, Northfields Avenue, NSW 2522, Australia

Email: nflament@uow.edu.au 


<h2>Datasets</h2>

	{} - variable

<h3> 1. Input data for cluster analysis </h3>
The directory ‘Input_Data_Cluster’ contains NetCDF files of dynamic topography at 20-million-year intervals, in a plate-frame reference, for models M6, Laurentia, and Baltica, used for cluster analysis.

<h3> 2. Reconstructions </h3>
The directory ‘Reconstructions’ contains tectonic reconstruction files (‘.rot’,  ‘.gpml’ ) considered in this study that can be easily imported into GPlates for interaction and visualisation. 

<h3> 3. Temperature and velocity data </h3>
The ‘Temperature_and_Velocity’ directory includes temperature and velocity vector files in ‘.grd’ format, stored in the Temperature and Velocity subdirectories for 440 Ma and 640 Ma.


<h3> 4. Cluster analysis: results </h3>
The directory ‘ClusterAnalysis’ contains the NetCDF outputs from the cluster analyses performed across all six models for two time intervals: 920–420 Ma and 420–0 Ma, with files distinguished by suffixes _2 and _3 for the 2 and 3 clusters, respectively. It also includes separate NetCDF datasets for Laurentia and Baltica for both time windows. Additionally, a dedicated subdirectory, ‘elbow_plots_data’, stores all dataframes used to generate the elbow plots.

<h3> 5. Comparing dynamic topography to preserved sediment flux for each continent </h3>
The directory ‘DTvsSediment’ contains sub-directories organised by model, with each model subdirectory containing the NetCDF files of dynamic topography calculated at 20-million-year intervals in the plate frame of reference. These files are organised by continent, used in Keller et al. (2019), compiled by Ronov et al. (1980). The folder structure follows the pattern:
 	{model}/PlateFrameGrid_{continent}/*.nc

In addition to the dynamic topography grids, the directory includes a set of .gpml files. These files contain ~0.45°-spaced points that represent continental blocks, grouped by plate ID. Each file corresponds to a single paleo-continental block and follows the naming pattern:
  	{model}_{continent}_{plateID}
Where model, continent, and plateID are the model name, 3-letter continental abbreviation used in this study, such as ‘AFR’ for Africa, and plate ID, respectively.

Two Python scripts are also included:

	▪	‘extract_long_lat_velpoint.py’, which generates the evenly spaced continental points used to create the .gpml files.
	▪	‘Mantleframe_to_Plateframe_continents.py’, which extracts dynamic topography along these points for each continent or continental block at 20 million-year increments and rotates the dynamic topography values to the plate frame of reference.

<h3> 6. Data for Extended Data Figure 7 </h3>
The directory ‘EDF7_Data’ contains all inputs and outputs for Extended Data Figure 7.

<h3> 7. Extended Data Figures </h3>
The directory ‘ExtendedDataFigures’ contains all nine Extended Data Figures presented in this study.

<h3> 8. Main Figures </h3>
The directory ‘MainFigures’ contains four figures presented in the Main Text of the manuscript.

<h3> 9. Orogens </h3>
The directory ‘orogens’ contains shapefiles of orogens compiled by Condie et al. (2021). 

<h3> 10. Reconstructed topologies </h3>
The directory ‘topologies_reconstructed’ contains shape files of reconstructed plate topologies, including ‘plate ridge and transform’,  ‘plate subduction’ and ‘Continent-Ocean boundary’ in 20-million-year increments for model M6, which serves as input for Figure 2 and Supplementary Video 1.

<h3> 11. Fit to deep Earth</h3>
The directory 'Fit_to_deep_Earth' contains csv files in respective 'accuracy_and_sensitivity', 'area' and 'eruptions_to_BlOBS' sub-directories used to evaluate performance of mantle flow models.


# 📘 Scripts

---

# 1. 🧩 [`Sedimentary_deposits_Macrostrat_Figure1.ipynb`](Sedimentary_deposits_Macrostrat_Figure1.ipynb)

**Description:** ## The lithostratigraphic data was downloaded from the Macrostrat (https://macrostrat.org/api/units/?lith_class=sedimentary) database via API (v2). This script uses the ‘macrostrat_ProtoCamb.geojson’ file in the root directory to filter sedimentary strata greater than 472 million years ago (Ma) and less than or equal to 635 Ma to plot the transgressive sedimentary deposits of the Great Unconformity.
 
**Referenced Paths:**
  - 📄 macrostrat_ProtoCamb.geojson

**Dependencies**
  - 📁Python Packages
	- json
	- requests
	- geopandas
	- pandas
	-pygmt

Outputs:
  - 📄 Figure1
---

# 2. 🧩 [`Joint_DT_Mantle_Temperature_Evolution_Figure2.ipynb`](Joint_DT_Mantle_Temperature_Evolution_Figure2.ipynb)

**Description:** ## This script generates a visual representation of the combined evolution of dynamic topography and mantle temperature at 640 Ma and 440 Ma, as shown in Figure 2 of the main manuscript. It also generates an animation (Supplementary Video 1) illustrating this joint evolution from 920 to 0 Ma, based on model case M6. This script creates a transect along a great circle, defined by the end and centre points that span across Laurentia in the present day. The script then creates a polyline based on these points and rotates through time using reconstruction files for the specified age. The dynamic topography and temperature profiles are extracted and plotted along the transect for cross-section.

**Dependencies**
  - 📁Python Packages
	- cartopy
	- geopandas
	- glob
	- gplately
	- imageio
	- io
	- math
	- numpy
	- pandas
	- PIL
	- pygmt
	- pygplates
	- pyproj
	- re
	- shapely
	- rioxarray
	- xarray


**Referenced Paths:**
  - 📁 Temperature_and_Velocity
      - 📁 Velocity
          - 📄 *{vel}-{age}Ma*km.grd
    - 📁 Temperature
          - 📄 *{temp}-{age}Ma*km.grd
      - 📁 Reconstructions
          - 📁 For_gld428  
              - 📄 1000_410_Convergence_NNR.gpml
              - 📄 1000_410_Divergence_NNR.gpml
              - 📄 1000_410_Topologies_NNR.gpml
              - 📄 1000_410_Transforms_NNR.gpml
              - 📄 Global_EarthByte_Mesozoic-Cenozoic_plate_boundaries_2016_v5_NNR.gpml
              - 📄 Global_EarthByte_Paleozoic_plate_boundaries_2016_v5_F_NNR.gpml
              - 📄 TopologyBuildingBlocks_AREPS_NNR.gpml
              - 📄 shapes_continents_Merdith_et_al.gpml
              - 📄 shapes_cratons_Merdith_et_al.gpml
          - 📁 For_gld504
              - 📄 1000_410_Convergence_Merdith_et_al.gpml
              - 📄 1000_410_Divergence_Merdith_et_al.gpml
              - 📄 1000_410_Topologies_Merdith_et_al.gpml
              - 📄 1000_410_Transforms_Merdith_et_al.gpml
              - 📄 COBfile_1000_0_combined_by_xianzhi.gpml
          - 📁 For_{model} # other models
              - 📄 1000_0_rotfile_Merdith_et_al_slightly_changed_for_nnr_nico_mod.rot
              - 📄 1000_410_rotations_NNR.rot
              - 📄 Global_EB_250-0Ma_GK07_2017-NNR.rot
              - 📄 Global_EB_410-250Ma_GK07_2017-NNR.rot
              - 📄 NR_0Ma_1000Ma_for_gplates.rot
              - 📄 NR_0Ma_1000Ma_for_gplates_combine.rot
          - 📄 shapes_static_polygons_Merdith_et_al.gpml
 
Outputs:
  - 📄 Figure2
  - 📄 SupplementaryVideo1_files
  - 📁 topologies_reconstructed
      - 📄 {model}_reconstructed_COB.shp
      - 📄 {model}_convergence.shp
      - 📄 {model}_reconstructed_polyline_{name}.shp
	
---

# 3. 🧩 [`Spatiotemporal_evolution_of_DT_Figure3.ipynb`](Spatiotemporal_evolution_of_DT_Figure3.ipynb)

**Description:** ### This script computes the optimal number of clusters that share similar dynamic topography evolution, based on the Davies-Bouldin Index (DBI), Silhouette Score and elbow plots for all six model cases for both the Great Unconformity formation (920–420 Ma) and preservation (420–0 Ma) periods. It plots the statistics for DBI, Silhouette Score, and the elbow plot, with circles indicating the optimal number of clusters (Extended Data Figure 2). 
It also computes the final raster map that identifies regions that formed or preserved the Great Unconformity, as well as areas that did not. It then creates a six-panel figure for all six model cases: the first four panels show the spatial distribution of clusters and the temporal evolution of dynamic topography for each cluster. The last two panels display the final map of the Great Unconformity formation and preservation, overlaid on the cluster map with orogen outlines (Figure 3). The analysis considers continental blocks that have continuously existed from 920Ma. 

The script performs a sensitivity analysis on the spatial extent of regions related to the number of clusters during both the Great Unconformity formation (920–420 Ma) and preservation (420–0 Ma) periods across all six model scenarios (Extended Data Figure 5). It then creates a vote map of different cluster combinations, highlighting areas where the Great Unconformity formed and was preserved (Extended Data Figure 6).

**Dependencies**
  - 📁Python Packages
	- cartopy
	- functools
	- geopandas
	- glob
	- gplately
	- itertools
	- matplotlib
	- numpy
	- operator
	- pandas
	- pygmt
	- pyproj
	- re
	- seaborn
	- shapely
	- sklearn
	- rioxarray
	- xarray


**Referenced Paths:**
  - 📁 Input_Data_Cluster
      - 📁 {model}
          - 📁 PlateFrameGrid
              - 📄 **PlateFrameGrid*.nc
          - 📁 PlateFrameGrid_BAL
              - 📄 **PlateFrameGrid*.nc
          - 📁 PlateFrameGrid_NA
              - 📄 **PlateFrameGrid*.nc
      - 📁 Reconstructions
          - 📁 For_gld504
              - 📄 1000_410_Topologies_Merdith_et_al.gpml
          - 📁 For_{model}
              - 📄 1000_0_rotfile_Merdith_et_al_slightly_changed_for_nnr_nico_mod.rot
              - 📄 NR_0Ma_1000Ma_for_gplates_combine.rot
          - 📄 shapes_static_polygons_Merdith_et_al.gpml
      - 📁 Scotese_paleogeography
          - 📁 Reconstruction
              - 📄 PALEOMAPGlobalPlateModel
  - 📁 ClusterAnalysis
      - 📄 BAL_{model}_{window.start}-{window.stop}.nc.   # window is either ‘920-420’ or ‘420-0’
      - 📄 BAL_{model}_{window.start}-{window.stop}_{n_clusters}.nc.   # n_clusters is the number of clusters
      - 📄 NA_{model}_{window.start}-{window.stop}.nc
      - 📄 NA_{model}_{window.start}-{window.stop}_{n_clusters}.nc
      - 📄 cluster_{model}_{window.start}-{window.stop}_{n_clusters}.nc
      - 📁 elbow_plots_data
          - 📄 {model}_{gaps}gap_{window.start}-{window.stop}_{n_clusters}_df.csv
  - 📁 Input_Data_Cluster
      - 📁 {model}
          - 📄 **_PlateFrameGrid*.nc.  # dynamic topography files
          - 📁 nolith
              - 📄 **_PlateFrameGrid*.nc
  - 📁 Reconstructions
      - 📁 For_gld504
          - 📄 COBfile_1000_0_combined_by_xianzhi.gpml
  - 📄 cob_540.shp
  - 📁 {scotese_datapath}
      - 📄 PALEOMAP_PlateModel.rot
      - 📄 PALEOMAP_PlatePolygons.gpml


Outputs:
  - 📄 Figure3
  - 📄 Extended Data Figure 2
  - 📄 Extended Data Figure 5
  - 📄 Extended Data Figure 6
 
---


# 4.  🧩 [`DTvsSedimentAnalysis_Figure4.ipynb`](DTvsSedimentAnalysis_Figure4.ipynb)

**Description:** This script extracts and plots the dynamic topography data at sedimentary volume data time step for every continent except Antarctica, based on datasets compiled by Ronov et al. (1980) and sourced from Keller et al. (2019). It also includes the sedimentary flux for each continent at the time steps of dynamic topography cycles. The sediment flux (increasing downward) and dynamic topography are then plotted against time (from 920 to 0 Ma), scaled by continental area,   for model case M6 (Figure 4). Additionally, the script plots the dynamic topography of continental blocks with distinct histories of dynamic topography within Eurasia and Africa (Extended Data Figure 8). The script also creates a plot of sedimentary flux and dynamic topography patterns across all six model cases and all continental blocks that continuously existed from 920 Ma (Extended Data Figure 9).

**Dependencies**
  - 📁Python Packages
	- cartopy
	- geopandas
	- glob
	- gplately
	- matplotlib
	- numpy
	- pandas
	- pygmt
	- pyproj
	- re
	- scipy
	- seaborn
	- shapely
	- rioxarray
	- xarray


**Referenced Paths:**
  - 📁 Input_Data_Cluster
      - 📁 {model}
          - 📁 PlateFrameGrid_{continent}
              - 📄 *.nc.    # Dynamic topography files extracted for each continent (DTvsSediment Folder and two Python scripts there)
  - 📁 DTvsSediment
      - 📄 *.xls.  # sediment data
      - 📁 {model}
          - 📁 PlateFrameGrid_{continent}
              - 📄 *.nc

Outputs:
  - 📄 Figure4
  - 📄 Extended Data Figure 8
  - 📄 Extended Data Figure 9

---

# 5. 🧩 [`Evaluation_Of_Mantle_Flow_Models_EDF1.ipynb`](Evaluation_Of_Mantle_Flow_Models_EDF1.ipynb)

**Description:** # This script processes a set of CSV files containing fractional area, accuracy, and distance to large igneous province (LIP) metrics for ten global tomographic models and six geodynamic model cases considered for both paleomagnetic frame of reference (PMAG) and no-net rotation (NNR) frame of reference. It generates a six-panel figure in which:
	•	Top row (three panels): Displays the metric values derived from the ten tomographic models for fractional area, accuracy, and LIP distance.
	•	Bottom row (three panels): Shows the corresponding metric values for the six forward-model cases.
A grey-shaded envelope is plotted in each panel, representing the spread of values obtained for the tomographic models. 

**Dependencies**
  - 📁Python Packages
	- glob
	- matplotlib
	- numpy
	- pandas
	- seaborn

**Referenced Paths:**
   - 📁 Fit_to_deep_Earth
      - 📁 {metric}     #[ accuracy, fractional area, distance to LIP]
              - 📄 {model}.csv.    # Tomography model or mantle flow model 

Outputs:
  - 📄 Extended Data Figure 1
 
---

# 6. 🧩 [`Dynamic_Topography_2clusters_2SD_formation_EDF3.ipynb`](Dynamic_Topography_2clusters_2SD_formation_EDF3.ipynb)

**Description:** This script produces a plot of the spatial distribution of two clusters and the temporal evolution of dynamic topography, bounded by two standard deviations, for each cluster for a period of 920–420 Ma across all model cases.

**Dependencies**
  - 📁Python Packages
	- geopandas
	- glob
	- numpy
	- pandas
	- pygmt
	- rioxarray
	- xarray


**Referenced Paths:**
 - 📁 ClusterAnalysis
      - 📄 cluster_{model}_420-920_2.nc.   


Outputs:
  - 📄 Extended Data Figure 3

---

# 7. 🧩 [`Dynamic_Topography_3clusters_temporal_evolution_EDF4.ipynb`](Dynamic_Topography_3clusters_temporal_evolution_EDF4.ipynb)

**Description:** This script produces a plot of the spatial distribution of three clusters and the temporal evolution of dynamic topography, bounded by two standard deviations, for each cluster for two periods:  920–420 Ma and 420–0 Ma for model M4.

**Dependencies**
  - 📁Python Packages
	- geopandas
	- glob
	- numpy
	- pandas
	- pygmt
	- rioxarray
	- xarray

**Referenced Paths:**
   - 📁 ClusterAnalysis
      - 📄 cluster_{model}_{window}_3.nc.    # window is either  ‘920-420’ or ‘420-0’
   
Outputs:
  - 📄 Extended Data Figure 4
  
---


#  8. 🧩 [`DynamcTopography_Rate_Elevation_Cluster_to_Scotese_Reconstruction_EDF7.ipynb`](DynamcTopography_Rate_Elevation_Cluster_to_Scotese_Reconstruction_EDF7.ipynb)

**Description:** # This script first rotates the dynamic topography grids at 540 Ma and 220 Ma, along with the long-term dynamic topography rates of change (computed for 600–540 Ma and 280–220 Ma), to the present day using the reconstruction file. The resulting present-day reconstructions are then rotated back to their respective geological ages (540 Ma and 220 Ma) using the Scotese rotation file in the PMAG frame of reference.
In addition, the script rotates the dynamic topography clusters for 920–420 Ma to 540 Ma, and for 420–0 Ma to 220 Ma, again using the Scotese rotation files.
Finally, it generates an eight-panel figure, for both 540 Ma (first column) and 220 Ma (second column), in which the following datasets are plotted:
Paleoelevation, dynamic topography, long-term dynamic topography rate of change, and dynamic topography clusters.

**Dependencies**
  - 📁Python Packages
	- geopandas
	- gplately
	- glob
	- numpy
	- optparse
	- pandas
	- pygmt
	- pyglates
	- rioxarray
	- scipy
	- shapely
	- shutil
	- xarray


**Referenced Paths:**
  - 📁 Input_Data_Cluster
      - 📁 {model}
          - 📁 Latitude*
              - 📄 *{age}*.grd
          - 📁 PlateFrameGrid
              - 📄 {model}PlateFrameGrid220.nc
              - 📄 {model}PlateFrameGrid280.nc
              - 📄 {model}PlateFrameGrid540.nc
              - 📄 {model}PlateFrameGrid600.nc
          - 📄 {model}_PlateFrameRate{rate_age}Ma.nc
      - 📁 Reconstructions
          - 📁 For_gld504
              - 📄 COBfile_1000_0_combined_by_xianzhi.gpml
              - 📄 lat_lon_velocity_domain_720_1440_with_plate_IDs_with_ages_for_gld504.gpml
          - 📁 For_{model}
              - 📄 1000_0_rotfile_Merdith_et_al_slightly_changed_for_nnr_nico_mod.rot
              - 📄 NR_0Ma_1000Ma_for_gplates_combine.rot
          - 📄 shapes_static_polygons_Merdith_et_al.gpml
      - 📁 Scotese_paleogeography
          - 📁 Reconstruction
              - 📁 PALEOMAPGlobalPlateModel
                  - 📄 lat_lon_velocity_domain_720_1440_plate_IDs_and_ages.gpml
  - 📁 ClusterAnalysis
      - 📄 cluster_gld504_0-420_{n_clusters}.nc
      - 📄 cluster_gld504_420-920_{n_clusters}.nc
  - 📁 Data_Fig4
      - 📄 reconstructed_{model}_DTrate_{rate_age}_to_0MA_504.nc
  - 📁 EDF7_Data
      - 📄 reconstructed_cob_{cluster_age}.shp
      - 📄 reconstructed_{model}_DT_{age}_to_{0}MA.nc
      - 📄 reconstructed_{model}_DT_{cluster_age}_to_0MA_504.nc
      - 📄 reconstructed_{model}_DT_{cluster_age}_to_{cluster_age}MA_504.nc
      - 📄 reconstructed_{model}_DTrate_{rate_age}_to_{cluster_age}MA_504.nc
  - 📁 Scotese_paleogeography
      - 📁 Reconstruction
          - 📁 PALEOMAPGlobalPlateModel
              - 📁 paleogeography_reconstructed
                  - 📄 Paleo-Elevation_0_504.nc
  - 📄 cob_540.shp
  - 📁 topologies_recon
      - 📄 cluster_{model}_420-920_540MA.nc
  - 📁 {scotese_datapath}
      - 📄 PALEOMAP_PlateModel.rot
      - 📄 PALEOMAP_PlatePolygons.gpml

Outputs:
  - 📄 Extended Data Figure 7
---


References

Keller, C. B. et al. Neoproterozoic glacial origin of the Great Unconformity. Proceedings of the National Academy of Sciences 116, 1136-1145 (2019). https://doi.org/10.1073/pnas.1804350116
Ronov, A. B., Khain, V. E., Balukhovsky, A. N. & Seslavinsky, K. B. Quantitative analysis of Phanerozoic sedimentation. Sedimentary Geology 25, 311-325 (1980). https://doi.org/https://doi.org/10.1016/0037-0738(80)90067-6 

