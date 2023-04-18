# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spider.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tvillare <tvillare@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/18 12:14:58 by tvillare          #+#    #+#              #
#    Updated: 2023/04/18 19:14:01 by tvillare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
from urllib.parse import urlparse
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
import re


parser = argparse.ArgumentParser(description='Web scraping, consige TODAS las fotos de una web indicando los subniveles')
parser.add_argument('url',
					help='enlace de busqueda')

parser.add_argument('-r', '--recusive',
					dest="r",
					action='store_true',
					help='Cantidad de subniveles debusqueda')

parser.add_argument('-l', '--lenght',
					metavar="[N]",
					dest='l',
					type=int,
					default=5,
					help='Cantidad de subniveles debusqueda')

parser.add_argument('-P', '--PATH',
					metavar="[PATH]",
					type=str,
					default="./data",
					dest='p',
					help='Path para guardar imagenes (defecto ./Data)')
args = parser.parse_args()



extenciones =  ["jpg", "jpeg", "png", "gif", "bmp"]

def	pull_img(imgs, path):
	for url in imgs:
		img_url = url
		if (len(img_url) > 2):
			try:
				name = img_url.split("/")
				if (len(name[-1]) < 0):
					return
				ext = name[-1].split(".")
				if ext[-1] in extenciones:
					nom_img = path + '/' + name[-1]
					respuesta = requests.get(img_url, stream=True)
					respuesta.raise_for_status()
					with open(nom_img, "wb") as archivo:
						for chunk in respuesta.iter_content(chunk_size=8192):
							archivo.write(chunk)
			except:
				print(tmp, "\n", name[-1])


def	create_list_img(soup):
	imgs = soup.find_all("img")
	imges = soup.find_all("image")
	lista = []
	for x in imgs:
		lista.append(x.get( 'src' ))
	for x in imges:
		lista.append(x.get( 'href' ))
	#print(lista)
	lista = list(set(lista))
	return (lista)


def	is_dominio(org, new, sub):
	if (org in new):
		return new
	name = sub.split('/')
	if not(re.match("^(https?|file):\/\/[^\s\/$.?#].[^\s]*$", new)):
		#print("no pass",new)
		if new[0] == '/':
			return (name[0] + "//" + name[2] + new)
		else:
			return ( name[0] + "//" + name[2] + '/' + new)



def find_url(soup, org, nivel, blacklist, path, back):
	url = soup.find_all("a")
	if (len(url) == 0):
		return
	imgs = create_list_img(soup)
	pull_img(imgs, path)
	for link in url:

		try:
			link_url = (link.get( 'href' ))
			link_url = is_dominio(org, link_url, back)

			if (org in link_url) and not(link_url in blacklist) and (nivel > 0):
				print("-->",link_url)
				blacklist.append(link_url)
				tmp_page = requests.get(link_url)
				tmp_soup = BeautifulSoup(tmp_page.content, "html.parser")
				find_url(tmp_soup, org, nivel - 1, blacklist, path, link_url)
		except:
			continue


if not os.path.exists(args.p):
	os.mkdir(args.p)

blacklist = []

if args.url.startswith('https://') or args.url.startswith('http://') or args.url.startswith('file://'):
	org = args.url
else:
	org = "https://" + args.url
if args.r:
	nivel = args.l
else:
	nivel = 0

if (nivel < 0):
	nive = 0

page = requests.get(org)
dominio = urlparse(org).netloc
print(dominio)
soup = BeautifulSoup(page.content, "html.parser")
blacklist.append(dominio)
print(nivel)
find_url(soup, dominio, nivel, blacklist, args.p, org)
