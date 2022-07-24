from domain.repository.object_model_repository import AbsObjectModelRepository
import http.client
import json
import config

class ObjectModelRepository(AbsObjectModelRepository):
    def FindByHash(self, hash: str):
        connection = http.client.HTTPConnection(config.API_DOMAIN)
        url = f"/api/v1/object_models/{hash}"
        header = {'content-type': 'application/json'}
        connection.request("GET", url, headers=header)
        response = connection.getresponse().read()
        data = json.loads(response)
        connection.close()
        return data
        
    def UpdatePid(self, object_model_id, pid):
        connection = http.client.HTTPConnection(config.API_DOMAIN)
        url = f"/api/v1/object_models/{object_model_id}/pid"
        header = {'content-type': 'application/json'}
        connection.request("PATCH", url, body=json.dumps({"pid": pid}), headers=header)
        response = connection.getresponse().read()
        data = json.loads(response)
        connection.close()
        return data
        
    def CreateProcessHistory(self, object_model_id, process_type_id):
        connection = http.client.HTTPConnection(config.API_DOMAIN)
        upload_data = {"process_type_id": process_type_id}
        header = {'content-type': 'application/json'}
        url = f"/api/v1/object_models/{object_model_id}/process_histories"
        connection.request("POST", url, body=json.dumps(upload_data), headers=header)
        response = connection.getresponse().read()
        data = json.loads(response)
        connection.close()
        return data
        
    def CreateModelObjectFile(self, object_model_id, file_path, file_name, file_size):
        connection = http.client.HTTPConnection(config.API_DOMAIN)
        header = {'content-type': 'application/json'}
        upload_data = {
            "path": file_path,
            "file_name": file_name,
            "file_size": file_size
        }
        url = f"/api/v1/object_models/{object_model_id}/object_model_files"
        connection.request("POST", url, body=json.dumps(upload_data), headers=header)
        response = connection.getresponse().read()
        data = json.loads(response)
        connection.close()
        return data