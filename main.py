# [START gae_python38_app]
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'textoDeSeguridad'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' 
db = SQLAlchemy(app)

from routes import *   

if __name__ == "__main__":
    app.run(debug=True, port=5001)
# [END gae_python38_app]
