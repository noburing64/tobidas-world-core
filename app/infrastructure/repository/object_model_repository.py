from domain.repository.object_model_repository import AbsObjectModelRepository
import http.client
import json
import config

class ObjectModelRepository(AbsObjectModelRepository):        
    def FindByHash(self, hash: str):
        url = f"/api/v1/object_models/{hash}"
        return self.__request(config.API_DOMAIN, url, "GET")
        
    def UpdatePid(self, object_model_id, pid):        
        url = f"/api/v1/object_models/{object_model_id}/pid"
        return self.__request(config.API_DOMAIN, url, "PATCH", {"pid": pid})
        
    def CreateProcessHistory(self, object_model_id, process_type_id):
        upload_data = {"process_type_id": process_type_id}
        url = f"/api/v1/object_models/{object_model_id}/process_histories"
        return self.__request(config.API_DOMAIN, url, "POST", upload_data)
        
    def CreateModelObjectFile(self, object_model_id, file_path, file_name, file_size):
        upload_data = {
            "path": file_path,
            "file_name": file_name,
            "file_size": file_size
        }
        url = f"/api/v1/object_models/{object_model_id}/object_model_files"
        return self.__request(config.API_DOMAIN, url, "POST", upload_data)

    def __request(self, domain: str, path: str, method: str, request_data = None) -> dict:
        conn = http.client.HTTPConnection(domain)
        headers = {'content-type': 'application/json'}
        body = json.dumps(request_data) if request_data is dict else None
        
        conn.request(method.upper(), path, headers=headers, body=body)
        response = conn.getresponse()
        if response.status == 302:
            # HTTPSにリダイレクト
            conn = http.client.HTTPSConnection(domain)
            conn.request(method.upper(), path, headers=headers, body=body)
            response = conn.getresponse()
            data = json.loads(response.read())
        else:
            data = json.loads(response.read())
        
        conn.close()
        return data
    
