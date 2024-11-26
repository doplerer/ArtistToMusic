# Guardar los links en un archivo de texto
def guardar_txt(artista, links):
    archivo_salida = f"{artista}.txt"
    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        for link in links:
            archivo.write(link + "\n")