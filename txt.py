# Guardar los links en un archivo de texto

def guardar_txt(cantante, links):
    archivo_salida = f"{cantante}.txt"
    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        for link in links:
            archivo.write(link + "\n")