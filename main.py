# Artist to Music
import musicApi
from threadController import controladorThreads
from txt import guardar_txt

def main():
    artista = input("Introduce el nombre del cantante: ")
    id_artista = musicApi.getId(artista)

    canciones = musicApi.getCanciones(id_artista, artista) # Nombres de canciones
    links = [] # Links de descarga
    
    for cancion in canciones:
        print(cancion)

    # Generación de links
    links = controladorThreads(canciones=canciones, max_workers=100)
    if links[0] is not False:
        links = list(set(links))
        # Guardado de links en .txt
        guardar_txt(artista=artista, links=links)

        print("Se han generado " + str(len(links)) + " links")



if __name__ == "__main__":
    main()