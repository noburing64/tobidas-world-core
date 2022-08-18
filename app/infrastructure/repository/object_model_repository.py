from domain.repository.object_model_repository import AbsObjectModelRepository
import domain.helper.http_helper as http_helper
import config

class ObjectModelRepository(AbsObjectModelRepository):        
    def FindByHash(self, hash: str):
        url = f"/api/v1/object_models/{hash}"
        return http_helper.request(config.API_DOMAIN, url, "GET")
        
    def UpdatePid(self, object_model_id, pid):        
        url = f"/api/v1/object_models/{object_model_id}/pid"
        return http_helper.request(config.API_DOMAIN, url, "PATCH", {"pid": pid})
        
    def CreateProcessHistory(self, object_model_id, process_type_id):
        upload_data = {"process_type_id": process_type_id}
        url = f"/api/v1/object_models/{object_model_id}/process_histories"
        return http_helper.request(config.API_DOMAIN, url, "POST", upload_data)
        
    def CreateModelObjectFile(self, object_model_id, file_path, file_name, file_size):
        upload_data = {
            "path": file_path,
            "file_name": file_name,
            "file_size": file_size
        }
        url = f"/api/v1/object_models/{object_model_id}/object_model_files"
        return http_helper.request(config.API_DOMAIN, url, "POST", upload_data)
    
