from flask import Flask
from flask_cors import CORS
from routes import *

app = Flask(__name__)
CORS(app)
cors_option = {
    "methods": ['GET','POST','DELETE', 'PUT', 'PATCH', 'OPTIONS'],
    "origins": ['http://localhost:4200', "127.0.0.1:4200"]
}

app.register_blueprint(api_routes)

if __name__ == "__main__":
    app.run(debug=True)