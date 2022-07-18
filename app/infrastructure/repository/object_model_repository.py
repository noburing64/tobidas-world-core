from domain.repository.object_model_repository import AbsObjectModelRepository
import http.client
import json
import config

class ObjectModelRepository(AbsObjectModelRepository):
    def FindByHash(self, hash: str):
        with http.client.HTTPConnection(config.API_DOMAIN) as connection:
            connection.request("GET", f"/api/v1/object_models/{hash}")
            response = connection.getresponse().read()
            data = json.load(response)
            return data
        
    def UpdatePid(self, object_model_id, pid):
        with http.client.HTTPConnection(config.API_DOMAIN) as connection:
            connection.request("PATCH", f"/api/v1/object_models/{object_model_id}/pid", json={"pid": pid})
            response = connection.getresponse().read()
            data = json.load(response)
            return data
        
    def CreateProcessHistory(self, object_model_id, process_type_id):
        with http.client.HTTPConnection(config.API_DOMAIN) as connection:
            upload_data = {"process_type_id": process_type_id}
            connection.request("PATCH", f"/api/v1/object_models/{object_model_id}/process_histories", json=upload_data)
            response = connection.getresponse().read()
            data = json.load(response)
            return data
        
    def CreateModelObjectFile(self, object_model_id, file_path, file_name, file_size):
        with http.client.HTTPConnection(config.API_DOMAIN) as connection:
            upload_data = {
                "path": file_path,
                "file_name": file_name,
                "file_size": file_size
            }
            connection.request("POST", f"/api/v1/object_models/{object_model_id}/object_model_files", json=upload_data)
            response = connection.getresponse().read()
            data = json.load(response)
            return data