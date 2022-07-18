from flask import Flask
from flask_injector import FlaskInjector
import presentation.controller.camera_controller as camera_controller
import presentation.controller.object_model_controller as object_model_controller
import config
import provider

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
# ルート設定
app.register_blueprint(camera_controller.app, url_prefix="/api/v1")
app.register_blueprint(object_model_controller.app, url_prefix="/api/v1")

        
FlaskInjector(app=app, modules=[provider.AppDIModule()])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=4000)