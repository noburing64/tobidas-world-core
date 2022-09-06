from flask import Blueprint, jsonify
from injector import inject

from domain.entity.camera_database import CameraDatabase

app = Blueprint('camera_controller', __name__)

# TODO: コントローラーにリポジトリは存在させない
# コントローラーのDIはアプリサービスのみにする

@app.route("/cameras", methods=['GET'])
def index():
    camera_database = CameraDatabase()
    camera_database.load()
    return jsonify(camera_database.getDataBase())

@inject
@app.route("/cameras/init")
def init():
    camera_database = CameraDatabase()
    camera_database.load()
    camera_database.getDataBase()
    return "done"
'''
@app.route("/cameras/<int:camera_id>")

'''