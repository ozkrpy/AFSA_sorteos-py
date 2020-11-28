from flask import Flask
import random
from bottle import post, request, route, run, static_file

lista = [1,2,3,4,5,6,7,8,9,0]
cantidad=5


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def listar():
    """Return a friendly HTTP greeting."""
    while (len(lista)>=cantidad):
        equipo=random.sample(lista,cantidad)
        for i in equipo:
            lista.remove(i)
    print(equipo)   
    return 'OK'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python38_app]
