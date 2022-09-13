from domain.repository.camera_repository import AbsCameraRepository
import domain.helper.http_helper as http_helper
import config
from urllib.parse import urlencode

class CameraRepository(AbsCameraRepository):
    def FindAll(self):
        return http_helper.request(config.API_DOMAIN, "/api/v1/cameras", "GET")
        
    def FindByModelName(self, maker_name: str, model_name: str):
        url = f"/api/v1/cameras?{urlencode({'model_name': model_name, 'maker_name': maker_name})}"
        return http_helper.request(config.API_DOMAIN, url, "GET")
        
    def Create(self, maker_name, model_name, focal_length):
        post_data = {
            "maker_name": maker_name,
            "model_name": model_name,
            "focal_length": focal_length
        }
        return http_helper.request(config.API_DOMAIN, "/api/v1/cameras", "POST", post_data)
