# Artist to Music
import api

def main():
    cantante = input("Introduce el nombre del cantante: ")
    id_cantante = api.getId(cantante)
    canciones = api.getCanciones(id_cantante)
    
    canciones_counter = 0
    for cancion in canciones:
        canciones_counter += 1
        print(cancion.getTitle())

    print( " ############## Se han mostrado: " + str(canciones_counter) + " canciones ##############")
    

if __name__ == "__main__":
    main()