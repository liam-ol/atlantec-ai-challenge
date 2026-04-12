import geopandas
from shapely import Point

if __name__ == "__main__":
    # More robust geocoding goes here. For now, choose from the below sample towns as input. 
    # Sample town lat/long coordinates from Wikipedia
    sample_towns = {
        "Kilkenny": Point(-7.251389, 52.650556),
        "Galway": Point(-9.048889, 53.271944),
        "Cork": Point(-8.47, 51.897222),
        "Letterkenny": Point(-7.7203, 54.9566)
    }

    with open("datasets/gael_towns.geojson") as gaeltacht_json:
        gaeltacht = geopandas.read_file(gaeltacht_json)

    your_town = input("Enter your town.\n> ")

    closest_towns = [gaeltacht.distance(sample_towns[your_town]).sort_values().index[x] for x in range(3)]

    print(f"""The 3 closest Gaeltacht towns are:
    {gaeltacht.loc[closest_towns[0]]["SETTL_NAME"]}
    {gaeltacht.loc[closest_towns[1]]["SETTL_NAME"]}
    {gaeltacht.loc[closest_towns[2]]["SETTL_NAME"]}""")