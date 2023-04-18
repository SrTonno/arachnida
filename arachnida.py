# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    arachnida.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tvillare <tvillare@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 13:09:09 by tvillare          #+#    #+#              #
#    Updated: 2023/04/18 11:57:21 by tvillare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import os
from bs4 import BeautifulSoup
import unicodedata
import time


import requests
import os
from bs4 import BeautifulSoup
import unicodedata
import time
import argparse
parser = argparse.ArgumentParser(description='es recursibo.')
parser.add_argument('-r', metavar="", type=int, default=5,
					help='busqueda en subniveles')
parser.add_argument('-l', metavar="", type=int, default=5,
					help='Cantidad de subniveles debusqueda')
parser.add_argument('-P [PATH]', metavar="", type=str, default="Data",
					help='Path para guardar imagenes (defecto ./Data)')
#args = parser.parse_args()
#print(args.accumulate(args.integers))
def	pull_img(imgs):
	for url in imgs:
		img_url= (url.get( 'src' ))
		if (len(img_url) > 2):
			try:
				name = img_url.split("/")
				if (len(name[-1]) < 0):
					return
				ext = name[-1].split(".")
				#print(ext[-1])
				if (ext[-1] == "jpg" or ext[-1]  == "jpeg" or ext[-1]  == "png" or ext[-1]  == "gif" or ext[-1]  == "bmp"):
					#print(">>",name[-1])
					nom_img = "./img/" +  unicodedata.normalize('NFKD', name[-1]).encode('ASCII', 'ignore').decode('utf-8')
					respuesta = requests.get(img_url, stream=True)
					respuesta.raise_for_status()
					with open(nom_img, "wb") as archivo:
						for chunk in respuesta.iter_content(chunk_size=8192):
							archivo.write(chunk)
					#print("Imagen descargada y guardada como:", nom_img)
			except:
				print(tmp, "\n", name[-1])

def	find_url(soup, org, nivel, blacklist):
	url = soup.find_all("a")
	imgs = soup.find_all("img")
	pull_img(imgs)
	#blacklist = []
	for link in url:
		try:
			link_url = (link.get( 'href' ))
			if (org in link_url) and (org != link_url) and not(link_url in blacklist) and (nivel > 0):
				print("-->",link_url, " ", nivel, "from", org)
				blacklist.append(link_url)
				#print("-->",link_url, "\n", link)
				tmp_page = requests.get(link_url)
				tmp_soup = BeautifulSoup(tmp_page.content, "html.parser")
				find_url(tmp_soup, link_url, nivel - 1, blacklist)
		except:
			continue
if not os.path.exists('img'):
	os.mkdir("img")
blacklist = []
org = "https://www.42madrid.com"
nivel = 0
page = requests.get(org)
soup = BeautifulSoup(page.content, "html.parser")
find_url(soup, org, nivel, blacklist)
