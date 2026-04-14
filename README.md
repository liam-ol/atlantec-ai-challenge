# Atlantec AI Challenge 2026
**State Machines** - Liam Ó Lionáird, Micael Pereira, Peter Hyland, Miguel Martins

## Idea: Help Your Gaeltacht

(Gaeltacht = designated Irish-language predominant areas of Ireland)

### Datasets (found in `datasets` folder)
* [Gaeltacht Boundaries Generalised 100m](https://data.gov.ie/dataset/gaeltacht-boundaries-generalised-100m-national-administrative-boundaries-20151) (Published by Tailte Éireann, Creative Commons Attribution license)
* [Settlements Generalised 100m](https://data.gov.ie/dataset/settlements-generalised-100m-national-statistical-boundaries-20151) (Published by Tailte Éireann, Creative Commons Attribution license)
    * Contains town location coordinates.
* `gael_towns.geojson`
    * Our custom list of Gaeltacht towns generated from the above datasets using `new_dataset.py` script in `datasets` folder.

Both of these datasets have ArcGIS GeoService REST API endpoints, our AI agent could query them remotely if we want.

### Project Outline:
1. Finds the nearest Gaeltacht towns near your location. (easy to test in Galway :P)
2. *[still undecided...]* Searches each town's website (or other sources) to find local development projects you can help out in.
3. Generates a brief glossary of Irish words related to results found in Step 2, to boost your vocabulary when you visit.
