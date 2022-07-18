from domain.repository.camera_repository import AbsCameraRepository
import http.client
import json
import config

class CameraRepository(AbsCameraRepository):
    def FindAll(self):
        with http.client.HTTPConnection(config.API_DOMAIN) as connection:
            connection.request("GET", "/api/v1/cameras")
            response = connection.getresponse().read()
            data = json.load(response)
            return data
        
    def FindByModelName(self, model_name):
        with http.client.HTTPConnection(config.API_DOMAIN) as connection:
            connection.request("GET", f"/api/v1/cameras?model_name={model_name}")
            response = connection.getresponse().read()
            data = json.load(response)
            return data
        
    def Create(self, model_name, focal_length):
        with http.client.HTTPConnection(config.API_DOMAIN) as connection:
            post_data = {"model_name": model_name, "focal_length": focal_length}
            connection.request("POST", "/api/v1/cameras", json=post_data)
            response = connection.getresponse().read()
            data = json.load(response)
            return data