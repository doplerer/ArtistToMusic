# Artist to Music
import api
from threadController import controladorThreads
from txt import guardar_txt

def main():
    cantante = input("Introduce el nombre del cantante: ")
    id_cantante = api.getId(cantante)

    canciones = api.getCanciones(id_cantante) # Nombres de canciones
    links = [] # Links de descarga
    
    # Generación de links
    links = controladorThreads(canciones=canciones, max_workers=100)
    if links[0] is not False:
        
        # Guardado de links en .txt
        guardar_txt(cantante=cantante, links=links)

        print("Se han generado " + str(len(links)) + " links")



if __name__ == "__main__":
    main()