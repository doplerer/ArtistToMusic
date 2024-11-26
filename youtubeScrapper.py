import requests
from bs4 import BeautifulSoup
import json

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
    }

def youtube_link(cancion):
    url = f"https://www.youtube.com/results?search_query={cancion}"
    video_id = 0000

    try:
        # Hacer la solicitud GET
        response = requests.get(url, headers=headers)

         # Parsear el HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar todos los scripts que contienen los datos de los videos (generalmente están en un <script> con "var ytInitialData")
        scripts = soup.find_all('script')

        for script in scripts:
            if 'ytInitialData' in script.text:
                
                # Extraer el contenido de ytInitialData
                json_text = script.text.strip()
                json_text = json_text[json_text.find('{'):json_text.rfind('}')+1]
                data = json.loads(json_text)

                # Itera sobre cada video renderer y busca el primer video orgánico
                video_renderers = data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']
                video_id = None

                for item in video_renderers:
                    try:
                        # Verificar si es un video o un anuncio
                        if 'videoRenderer' in item:
                            video_renderer = item['videoRenderer']
                            video_id = video_renderer['videoId']
                            break  # Salir después de encontrar el primer video orgánico
                    except KeyError:
                        continue

                # RESULTADO
                if video_id:
                    return f"https://www.youtube.com/watch?v={video_id}"
                else:
                    return "No se encontraron videos relevantes."

    except:
        print(response.text)

    return "ERROR"

#print(youtube_link("laura pausini"))