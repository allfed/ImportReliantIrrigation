# ImportReliantIrrigation

## Introduction

Multiple sources of data are used to estimate the fraction of irrigated cropland that is reliant on electricity or diesel:
 - aquastat: includes government level census data with information about the country's irrigated cropland area technologies, including the amount of land that is supplied by pumps (source), and how that water is then applied to the cropland (scheme).
 - gmiav5: includes global 5 minute resolution data including the total area equipped for irrigation, the total surface water irrigation, and the total groundwater irrigation.  
 - pandas "naturalearth_lowres": a low resolution map including shapefiles for all country boundaries, identified by country code.

** These data are global. A complex series of data manipulations were required to come to a reasonable estimate of the irrigation, and it should be considered a first pass with low confidence in any particular region. **

- **Dataset**: Global Map of Irrigation Areas – Version 5
  - **Definition**: area equipped for irrigation (% of total area)
  - **Spatial resolution**: 5 arcmin
  - **Time Period**: 22005
  - **Source**: Siebert et al. (2013)
  - **Available online**: [Link](https://data.apps.fao.org/map/catalog/srv/api/records/f79213a0-88fd-11da-a88f-000d939bc5d8)

- **Dataset**: AQUASTAT – FAO’s Global Information System on Water and Agriculture
  - **Definition**: 
    - Area (1000 hectares) equipped for:
    - Irrigation (Equipped Lowland Areas, Spate Irrigation, Total)
    - Full control irrigation (Surface, Sprinkler, Localized, Total, Actually Irrigated)
    - Power irrigation
  - **Spatial resolution**: Country level
  - **Time Period**: Around mid-2010s
  - **Source**: FAO (2019)
  - **Available online**: [Link](http://fao.org/aquastat/statistics/query/index.html?lang=en)

Available data from aquastat includes the following country level data:
 - spate_area
 - lowland_area
 - sprinkler_area
 - localized_area
 - surface_area
 - power_area
 - surface_water_area
 - ground_water_area
 - total_irrigated_area
