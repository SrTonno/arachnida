# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tvillare <tvillare@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 14:56:24 by tvillare          #+#    #+#              #
#    Updated: 2023/05/10 18:31:43 by tvillare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import os
import sys

import exiftool
#installar conda install -c conda-forge exiftool
def leer_metadatos(archivo):
	with exiftool.ExifToolHelper() as et:
		metadata = et.get_metadata(archivo)
		for item in metadata:
			for etiqueta, valor in item.items():
				print("{:<40}:\t{:<30}".format(etiqueta, valor))

def eliminar_metadatos(archivo, etiquetas):
	with ExifTool() as et:
		et.delete_tags(archivo, etiquetas)

a = sys.argv[1:]
for x in a:
	print("\n->",x)
	try:
		meta = leer_metadatos(x)
	except:
		print("ERROR name img")
