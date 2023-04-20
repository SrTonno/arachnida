# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tvillare <tvillare@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 14:56:24 by tvillare          #+#    #+#              #
#    Updated: 2023/04/20 16:05:38 by tvillare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image
from PIL.ExifTags import TAGS
import os
import sys


# Abrir la imagen
#img = Image.open('/Users/tvillare/Desktop/IMG_20170429_110054.jpg')

# Obtener los metadatos de la imagen
def get_meta(data):
	img = Image.open(data)
	exif = img._getexif()
	if exif:
		for tag_id in exif:
			try:
				tag = TAGS.get(tag_id, tag_id)
				data = exif.get(tag_id)
				if isinstance(data, bytes):
					data = data.decode()
				print("{:<30}:\t{:>20}".format(tag, data))
			except:
				continue
	else:
		print("La imagen no tiene metadatos EXIF.")


a = sys.argv[1:]
for x in a:
	print("\n->",x)
	try:
		get_meta(x)
	except:
		print("ERROR name img")
