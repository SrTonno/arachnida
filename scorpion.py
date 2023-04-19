from PIL import Image
from PIL.ExifTags import TAGS

# Abrir la imagen
img = Image.open('/Users/tvillare/Desktop/cositas25.png')

# Obtener los metadatos de la imagen
exif_data = img._getexif()

# Mostrar los metadatos
if exif_data:
	for tag_id in exif_data:
		tag = TAGS.get(tag_id, tag_id)
		data = exif_data.get(tag_id)
		if isinstance(data, bytes):
			data = data.decode()
		print(f"{tag}: {data}")
else:
	print("La imagen no tiene metadatos EXIF.")
