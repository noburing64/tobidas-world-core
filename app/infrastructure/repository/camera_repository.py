from domain.repository.camera_repository import AbsCameraRepository
import http.client
import json
import config
from urllib.parse import urlencode

class CameraRepository(AbsCameraRepository):
    def FindAll(self):
        connection = http.client.HTTPConnection(config.API_DOMAIN)
        connection.request("GET", "/api/v1/cameras")
        response = connection.getresponse().read()
        data = json.loads(response)
        connection.close()
        return data
        
    def FindByModelName(self, model_name):
        connection = http.client.HTTPConnection(config.API_DOMAIN)
        header = {'content-type': 'application/json'}
        url = f"/api/v1/cameras?{urlencode({'model_name': model_name})}"
        connection.request("GET", url, headers=header)
        response = connection.getresponse().read()
        data = json.loads(response)
        connection.close()
        return data
        
    def Create(self, model_name, focal_length):
        connection = http.client.HTTPConnection(config.API_DOMAIN)
        header = {'content-type': 'application/json'}
        post_data = {"model_name": model_name, "focal_length": focal_length}
        connection.request("POST", "/api/v1/cameras", body=json.dumps(post_data), headers=header)
        response = connection.getresponse().read()
        data = json.loads(response)
        connection.close()
        return data