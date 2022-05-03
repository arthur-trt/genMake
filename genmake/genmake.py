#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    genmake.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: atrouill <atrouill@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/22 00:47:02 by atrouill          #+#    #+#              #
#    Updated: 2021/01/22 00:47:06 by atrouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from importlib.resources import path
from pathlib import Path
from colorama import Fore, Style

from .source_file_maker import populate_sources
from .args import parse_args
from .cli import obtain_parameters
from .makefile import generate_makefile
from .update import check_update

def create_makefile(params: dict):
	"""
	Create Makefile and fill it with user params
	"""
	content = generate_makefile(params)
	with open("Makefile", "w") as file:
		file.write(content)
		file.close()
	print(Fore.GREEN + "✅ Makefile created!" + Style.RESET_ALL)

def	check_makefile_before_parse(path: path) -> bool:
	with open(path, 'r') as f:
		line = f.readline()
		f.close()
		if "Generated with GenMake" not in line:
			return (False)
		return (True)

def main():
	args = parse_args()
	p = Path('Makefile')
	check_update()
	if (args.remake == True) or not p.exists():
		params = obtain_parameters()
		create_makefile(params)
	if (check_makefile_before_parse(p)):
		populate_sources()
	else:
		print(Fore.RED + "Your Makefile does not seem to have been generated with genMake.\n(make a backup just in case before deleting it)" + Style.RESET_ALL)

