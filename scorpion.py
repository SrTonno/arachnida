# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tvillare <tvillare@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 14:56:24 by tvillare          #+#    #+#              #
#    Updated: 2023/04/19 15:46:07 by tvillare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image
from PIL.ExifTags import TAGS
import os

def fecha_info(exif):
	date_time_original = exif.get(36867)
	print("Fecha y hora de creación:", date_time_original)

def camara_info(exif):
	# Información de la cámara
	make = exif.get(271)
	model = exif.get(272)
	serial_number = exif.get(42033)
	exposure_time = exif.get(33434)
	aperture = exif.get(33437)
	focal_length = exif.get(37386)
	print("Cámara:")
	print("\tFabricante:", make)
	print("\tModelo:", model)
	print("\tNúmero de serie:", serial_number)
	print("\tTiempo de exposición:", exposure_time)
	print("\tApertura:", aperture)
	print("\tDistancia focal:", focal_length)

def exposicion_info(exif):
	shutter_speed = exif.get(37377)
	iso_speed = exif.get(34855)
	print("Configuración de exposición:")
	print("\tVelocidad de obturación:", shutter_speed)
	print("\tSensibilidad ISO:", iso_speed)

def gps_info(exif):
	gps_latitude = exif.get(2)
	gps_longitude = exif.get(4)
	gps_altitude = exif.get(6)
	gps_time_stamp = exif.get(36867)
	print("Información de GPS:")
	print("\tLatitud:", gps_latitude)
	print("\tLongitud:", gps_longitude)
	print("\tAltitud:", gps_altitude)
	print("\tMarca de tiempo GPS:", gps_time_stamp)

# Abrir la imagen
img = Image.open('/Users/tvillare/Desktop/IMG_20170429_110054.jpg')

# Obtener los metadatos de la imagen
exif = img._getexif()
if exif:
# Mostrar los metadatos
	date_time_original = exif.get(36867)
	#print("Fecha y hora de creación:", date_time_original)

	# Informacion de la cámara
	#camara_info(exif)
	# Configuración de exposición
	#exposicion_info(exif)
	# Información de GPS
	#gps_info(exif)

	# Configuracion de color y perfil ICC
	#color_space = exif.get(40961)
	#icc_profile = exif.get(34675)


	for tag_id in exif:
		try:
			tag = TAGS.get(tag_id, tag_id)
			data = exif.get(tag_id)
			if isinstance(data, bytes):
				data = data.decode()
			print(f"{tag}: {data}")
		except:
			continue
else:
	print("La imagen no tiene metadatos EXIF.")
