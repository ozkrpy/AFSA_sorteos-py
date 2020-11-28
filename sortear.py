from bottle import post, request, route, run, static_file
import random

lista = [1,2,3,4,5,6,7,8,9,0]
cantidad = 5

@route('/')
def server_static(filepath='home.html'):
    return static_file(filepath, root='./')

def sortear():
    while (len(lista)>=cantidad):
        equipo = random.sample(lista, cantidad)
        for i in equipo:
            lista.remove(i)
        print(equipo)
    return equipo

if __name__=="__main__":
    print("INICIO")
    sortear()
    run(host='127.0.0.1', port=5000, debug=True)
