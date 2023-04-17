import unicodedata
import requests

# URL de la imagen a descargar
url_imagen =  "https://www.42madrid.com/wp-content/uploads/2022/06/Hub-de-Innovacion-y-Talento-e1655116389582-1366x621.png"

# Nombre de archivo para guardar la imagen
nombre_archivo = "imagen.jpg"

try:
	# Descargar la imagen y guardarla en un archivo local
	respuesta = requests.get(url_imagen, stream=True)
	respuesta.raise_for_status()
	with open(nombre_archivo, "wb") as archivo:
		for chunk in respuesta.iter_content(chunk_size=8192):
			archivo.write(chunk)
	print("Imagen descargada y guardada como:", nombre_archivo)
except requests.exceptions.RequestException as e:
	print("Error al descargar la imagen:", e)
