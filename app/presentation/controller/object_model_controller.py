from application.interactor.object_model_interactor.abs_create_object_model_interactor import AbsCreateObjectModelInteractor
from presentation.request_param.interactor.object_model.create_object_model_param import CreateObjectModelParam as CreateObjectModelInteractorParam
from flask import Blueprint, jsonify, request
from injector import inject

app = Blueprint('object_model_controller', __name__)

# TODO: コントローラーにリポジトリは存在させない
# コントローラーのDIはアプリサービスのみにする

@inject
@app.route("/object_models/<string:hash>", methods=['POST'])
def create_object_model(hash: str, create_app_interactor: AbsCreateObjectModelInteractor):
    # イメージの取得
    data = request.json
    input = CreateObjectModelInteractorParam(hash, data["images"])
    response = create_app_interactor.handle(input)
    
    return response

@inject
@app.route("/object_models/<string:hash>/cancel", methods=['POST'])
def cancel_progress():
    #
    return "HOGE"
