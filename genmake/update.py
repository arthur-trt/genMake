# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    update.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: atrouill <atrouill@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/09/08 10:01:25 by atrouill          #+#    #+#              #
#    Updated: 2021/09/08 11:20:46 by atrouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import pathlib
from colorama import Style, Fore
import genmake.config as config

def	get_last_version() -> dict:
	origin_infos = dict()
	headers = {"Accept": "application/vnd.github.v3+json"}
	url = "https://api.github.com/repos/arthur-trt/genmake/releases"
	r = requests.get(url, headers=headers)
	r = r.json()
	origin_infos["version"] = r[0]['tag_name']
	origin_infos["changelog"] = r[0]['body']
	return (origin_infos)

def obtain_generator_version() -> str:
	path = pathlib.Path("./Makefile")
	try:
		makefile = open(path, 'r')
	except:
		return (None)
	lines = makefile.readlines()
	for line in lines:
		if "# genmake v" in line:
			return(line.split(" ")[2].strip())

def	check_update():
	origin = get_last_version()
	gen = obtain_generator_version()

	if (origin["version"] != config.VERSION):
		print(Fore.YELLOW, end='')
		print("A new version is available.")
		print("Please update with : 'python3 -m pip install --upgrade genmake'")
		print("Changelog :")
		changelog = origin["changelog"].split('\n')
		for line in changelog:
			print("\t" + line)
		print(Style.RESET_ALL)

	elif (config.VERSION != gen):
		print(Fore.YELLOW, end='')
		print("Your Makefile was generated with an old version of genmake")
		print("It is recommended to run 'genmake --remake' to correct possible bugs")
		print(Style.RESET_ALL)

