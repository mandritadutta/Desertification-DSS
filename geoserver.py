import requests

# Connection details for enterprise server
gs_url = "http://localhost:8080/geoserver/rest"
auth = ("admin", "geoserver")
workspace = "desertification_project"

# Automating the creation of a new coverage store for risk maps
def publish_raster(layer_name, file_path):
    url = f"{gs_url}/workspaces/{workspace}/coveragestores/{layer_name}/external.geotiff"
    headers = {'Content-type': 'text/plain'}
    response = requests.put(url, auth=auth, data=file_path, headers=headers)
    return response.status_code

print(publish_raster("Current_Risk", "/data/Current_Risk.tif"))