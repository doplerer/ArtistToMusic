# Artist to Music
import api
from concurrent.futures import ThreadPoolExecutor

def controladorThreads(canciones, max_workers):
    pass



def main():
    cantante = input("Introduce el nombre del cantante: ")
    id_cantante = api.getId(cantante)

    canciones = api.getCanciones(id_cantante) # Nombres de canciones
    links = [] # Links de descarga
    
    # Proceso de descargas
    resultados = controladorThreads(canciones=canciones, max_workers=20)

    canciones_counter = 0

    for cancion in canciones:
        canciones_counter+=1
        print(cancion)


    print( " Se han encotrado: " + str(canciones_counter) + " canciones")
    

if __name__ == "__main__":
    main()