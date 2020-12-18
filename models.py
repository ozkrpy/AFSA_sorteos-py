from datetime import datetime
from main import db

class Jugador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    numero_camiseta = db.Column(db.Integer)
    date = db.Column(db.Date, nullable=False)

    # se va representar a si misma
    def __repr__(self):
        return f'{self.nombre}(#{self.numero_camiseta})'

class Equipos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    listado = db.Column(db.String(150), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.listado}'
