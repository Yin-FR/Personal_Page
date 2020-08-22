from flask import Flask
from flask_cors import CORS
from communication.views import communication

app1 = Flask(__name__)
CORS(app1, supports_credentials=True)
app1.register_blueprint(communication, url_prefix='/communication')

if __name__ == '__main__':
    app1.run()
