from concurrent.futures import ThreadPoolExecutor
import api

def controladorThreads(canciones, max_workers):

    # Lista de links finales
    links = []

    # Funcion que ejecuta cada thread
    def threadFunction(cancion):
        return api.youtube_link(cancion)
    
    
    # Usamos ThreadPoolExecutor para procesar en paralelo
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(threadFunction, canciones)  # Procesa cada canción
        links.extend(results)  # Recoge los resultados
    
    return links