import requests
from funciones import filtros
import time

# Busca el ID de un artista por nombre
def getId(artista):
    url = "https://musicbrainz.org/ws/2/artist"
    params = {
        "query": f'artist:"{artista}"',
        "fmt": "json"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        # Si hay resultados, devuelve el ID del primer artista
        if data.get("artists"):
            return data["artists"][0]["id"]
        else:
            print("Artista no encontrado.")
            return None
    else:
        print("Error al buscar el artista:", response.status_code)
        return None

# Busca canciones de un artista utilizando su ID
def getCanciones(artist_id, artista):
    url = "https://musicbrainz.org/ws/2/recording"

    titulos = [] # Lista de títulos de canciones en formato string
    canciones = []  # Lista para almacenar todas las canciones
    limit = 100  # Límite máximo por solicitud según la API
    offset = 0  # Punto de inicio en los resultados

    while True:
        time.sleep(1) # sleep de 1s para evitar bloqueos

        # Solicitud
        params = {
            "artist": artist_id,
            "fmt": "json",
            "limit": limit,
            "offset": offset
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            recordings = data.get("recordings", [])

            # Si no hay más grabaciones, terminar el bucle
            if not recordings:
                break

            # Filtrar resultados que no sean canciones
            for recording in recordings:
                
                # añade canciones a lista si pasan filtros
                if filtros(recording):
                    canciones.append(artista + " - " + recording["title"])

            offset += limit

        else:
            print("Error al buscar canciones:", response.status_code)
            break


    # Borra repetidas
    canciones = list(set(canciones))

    return canciones