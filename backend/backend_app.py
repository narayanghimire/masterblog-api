from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from controllers.post_controller import post_controller


SWAGGER_URL = "/api/docs"
API_URL = "/static/masterblog.json"

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(post_controller)
    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Masterblog API"}
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5002, debug=True)
