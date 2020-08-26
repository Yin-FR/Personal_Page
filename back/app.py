from flask import Flask
from flask_cors import CORS
from communication.views import communication
from ML.datasets.views import datasets
from ML.ML.views import ML

app1 = Flask(__name__)
CORS(app1, supports_credentials=True)

app1.register_blueprint(communication, url_prefix='/communication')
app1.register_blueprint(datasets, url_prefix='/datasets')
app1.register_blueprint(ML, url_prefix='/ML')

if __name__ == '__main__':
    app1.run()
