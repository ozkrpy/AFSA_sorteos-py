# [START gae_python38_app]
from bottle import post, request, route, run, static_file
import random

# lista = [1,2,3,4,5,6,7,8,9,0]
archivo = {}
presentes = []
equipos = []
cantidad = 5

@route('/')
def server_static(filepath='home.html'):
    return static_file(filepath, root='./')

def sortear():
    #global lista
    while len(presentes)>=cantidad:
        equipo = random.sample(presentes, cantidad)
        for i in equipo:
            presentes.remove(i)
        equipos.append(equipo)
        # print(equipo)
        # print(lista)

def leer_archivo():
    # global archivo
    with open('jugadores.txt',mode='r') as listado:
        for i in listado:
            # lista.append(i[:-1])
            numero, nombre = i.partition(',')[::2]
            # print(numero, nombre)
            # lista.append({numero,nombre[:-1]})#, nombre)
            archivo[numero]=nombre[:-1]

def cargar_lista():
    for numero, jugador in archivo.items():
        presentes.append(numero)

def mostrar_equipos():
    for i in equipos:
        for j in i:
            print (archivo[j], end='\t')
        print('')
            
if __name__ == "__main__":
    leer_archivo()
    cargar_lista()
    sortear()
    if len(presentes)>0:
        resto_del_mundo=presentes
    mostrar_equipos()

    # run(host='127.0.0.1', port=5000, debug=True)
# [END gae_python38_app]