# 📘 Project Notebooks Overview

This auto-generated README provides a structured overview of all Jupyter notebooks in this project.
Each section lists file paths referenced in the notebook — including glob patterns and f-strings with variables.

---

## 🧩 [`DTvsSedimentAnalysis.ipynb`](DTvsSedimentAnalysis.ipynb)

**Description:** ### Extract DT evolution for each continental block to Ronov's time step

**Referenced Paths:**
  - 📁 ..
      - 📁 Model_data
          - 📁 {model}
              - 📁 PlateFrameGrid_{continent}
                  - 📄 *.nc
  - 📁 DTvsSediment
      - 📄 *.xls
      - 📁 {model}
          - 📁 PlateFrameGrid_{continent}
              - 📄 *.nc

---

## 🧩 [`DynamcTopography_Rate_Elevation_Cluster_to_Scotese_Reconstruction_EDF7.ipynb`](DynamcTopography_Rate_Elevation_Cluster_to_Scotese_Reconstruction_EDF7.ipynb)

**Description:** # Rotate Dynamic Topography to present day

**Referenced Paths:**
  - 📁 ..
      - 📁 Model_data
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

---

## 🧩 [`Dynamic_Topography_2clusters_2SD_formation_EDF3.ipynb`](Dynamic_Topography_2clusters_2SD_formation_EDF3.ipynb)

**Description:** No description available.

**Referenced Paths:**
  - *(No file paths found)*

---

## 🧩 [`Dynamic_Topography_3clusters_temporal_evolution_EDF4.ipynb`](Dynamic_Topography_3clusters_temporal_evolution_EDF4.ipynb)

**Description:** No description available.

**Referenced Paths:**
  - *(No file paths found)*

---

## 🧩 [`Evaluation_Of_Mantle_Flow_Models_EDF1.ipynb`](Evaluation_Of_Mantle_Flow_Models_EDF1.ipynb)

**Description:** # 3 columns plot [Fractional Area, Accuracy and Distance to LIPs] with GyPSuMS

**Referenced Paths:**
  - *(No file paths found)*

---

## 🧩 [`Joint_DT_Mantle_Temperature_Evolution_Figure2.ipynb`](Joint_DT_Mantle_Temperature_Evolution_Figure2.ipynb)

**Description:** ## Figure 2: Predicted joint evolution of dynamic topography and mantle temperature and Supplementary Video 1

**Referenced Paths:**
  - 📁 ..
      - 📁 Model_data
          - 📁 {model}
              - 📁 Velocity
                  - 📄 *{vel}-{age}Ma*km.grd
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
          - 📁 For_{model}
              - 📄 1000_0_rotfile_Merdith_et_al_slightly_changed_for_nnr_nico_mod.rot
              - 📄 1000_410_rotations_NNR.rot
              - 📄 Global_EB_250-0Ma_GK07_2017-NNR.rot
              - 📄 Global_EB_410-250Ma_GK07_2017-NNR.rot
              - 📄 NR_0Ma_1000Ma_for_gplates.rot
              - 📄 NR_0Ma_1000Ma_for_gplates_combine.rot
          - 📄 shapes_static_polygons_Merdith_et_al.gpml
  - 📁 Reconstructions
      - 📁 For_gld504
          - 📄 1000_410_Topologies_Merdith_et_al.gpml
          - 📄 250_0_plate_boundaries_Merdith_et_al.gpml
          - 📄 410_250_plate_boundaries_Merdith_et_al.gpml
          - 📄 COBfile_1000_0_combined_by_xianzhi.gpml
          - 📄 TopologyBuildingBlocks_Merdith_et_al.gpml
  - 📄 SupplementaryVideo1_files
  - 📁 topologies_reconstructed
      - 📁 {model}
          - 📄 {model}_reconstructed_COB.shp
  - 📁 {input_folder}
      - 📄 DT_tempanomaly_Robinson_{age}.png
      - 📄 crosssection_{age}.png
  - 📁 {outfile_dir}
      - 📄 {model}_convergence.shp
      - 📄 {model}_convergence_fileseg.shp
      - 📄 {model}_reconstructed_polyline_{name}.shp
      - 📄 {model}_reconstructed_{fname}.shp
      - 📄 {model}_reconstructed_{fname}_{age}.shp

---

## 🧩 [`PathTree_and_Readme.ipynb`](PathTree_and_Readme.ipynb)

**Description:** No description available.

**Referenced Paths:**
  - 📄 *
  - 📄 *.ipynb
  - 📄 /
  - 📄 \
  - 📄 \\
  - 📄 \n
  - 📁 data
      - 📄 file.csv
  - 📁 folder
      - 📄 *.ext
      - 📁 {var}
          - 📄 file.nc

---

## 🧩 [`Sedimentary_deposits_Macrostrat_Figure1.ipynb`](Sedimentary_deposits_Macrostrat_Figure1.ipynb)

**Description:** ## Figure 1: Oldest sedimentary deposits of the Great Unconformity using digital database Macrostrat

**Referenced Paths:**
  - 📄 macrostrat_ProtoCamb.geojson

---

## 🧩 [`Spatiotemporal_evolution_of_DT_Figure3.ipynb`](Spatiotemporal_evolution_of_DT_Figure3.ipynb)

**Description:** ### Figure 3: Cluster Anslysis and Spatio-temporal evolution of dynamic topography

**Referenced Paths:**
  - 📁 ..
      - 📁 Model_data
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
      - 📄 BAL_{model}_{window.start}-{window.stop}.nc
      - 📄 BAL_{model}_{window.start}-{window.stop}_{n_clusters}.nc
      - 📄 NA_{model}_{window.start}-{window.stop}.nc
      - 📄 NA_{model}_{window.start}-{window.stop}_{n_clusters}.nc
      - 📄 cluster_{model}_{window.start}-{window.stop}_{n_clusters}.nc
      - 📁 elbow_plots_data
          - 📄 {model}_{gaps}gap_{window.start}-{window.stop}_{n_clusters}_df.csv
  - 📁 Model_data
      - 📁 {model}
          - 📄 **_PlateFrameGrid*.nc
          - 📁 nolith
              - 📄 **_PlateFrameGrid*.nc
  - 📁 Reconstructions
      - 📁 For_gld504
          - 📄 COBfile_1000_0_combined_by_xianzhi.gpml
  - 📄 cob_540.shp
  - 📁 {scotese_datapath}
      - 📄 PALEOMAP_PlateModel.rot
      - 📄 PALEOMAP_PlatePolygons.gpml

---

_This README was generated automatically — do not edit manually unless necessary._

Generated by `generate_notebook_readme.py` 🪄