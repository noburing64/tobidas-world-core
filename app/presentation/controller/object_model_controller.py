from application.interactor.object_model_interactor.abs_create_object_model_interactor import AbsCreateObjectModelInteractor
from flask import Blueprint, jsonify, request
from injector import inject

from application.service.object_model_service.abs_create_object_model_app_service import AbsCreateObjectModelAppService

app = Blueprint('object_model_controller', __name__)

# TODO: コントローラーにリポジトリは存在させない
# コントローラーのDIはアプリサービスのみにする

@inject
@app.route("/object_models/<string:hash>", methods=['POST'])
def create_object_model(hash: str, create_app_interactor: AbsCreateObjectModelInteractor):
    # イメージの取得
    data = request.json
    response = create_app_interactor.handle(data)
    #response = create_app_service.handle(hash, data)
    
    return response

@inject
@app.route("/object_models/<string:hash>/cancel", methods=['POST'])
def cancel_progress():
    #
    return "HOGE"
