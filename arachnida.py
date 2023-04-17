# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    arachnida.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tvillare <tvillare@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 13:09:09 by tvillare          #+#    #+#              #
#    Updated: 2023/04/17 14:11:49 by tvillare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import os
import urllib.request
from bs4 import BeautifulSoup
import unicodedata


def	descargar_img(url):
	#img = soup3.find(class_= "vtex-store-components-3-x-productImageTag vtex-store-components-3-x-productImageTag--main")
	#print(url)
	img_url= (url.get( 'src' ))
	if (len(img_url) > 2):
		try:
			name = img_url.split("/")
			if (len(name[-1]) < 2):
				return
			tmp = unicodedata.normalize('NFKD', name[-1]).encode('ASCII', 'ignore').decode('utf-8')
			nom_img = "./img/" + tmp
			respuesta = requests.get(img_url, stream=True)
			respuesta.raise_for_status()
			with open(nom_img, "wb") as archivo:
				for chunk in respuesta.iter_content(chunk_size=8192):
					archivo.write(chunk)
			print("Imagen descargada y guardada como:", nom_img)
		except:
			print(tmp, "\n", name[-1])


if not os.path.exists('img'):
	os.mkdir("img")
page = requests.get( "https://www.42madrid.com/")
soup = BeautifulSoup(page.content, "html.parser")
imgs = soup.find_all("img")
print(*imgs, sep="\n")
for x in imgs:
	descargar_img(x)
#urllib.request.urlretrieve(img_url,nom_img)
print("----------------")
#url = soup.find_all("a")
#print(*url, sep="\n")
