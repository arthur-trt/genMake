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

from pathlib import Path
from colorama import Fore, Style

from .source_file_maker import populate_sources
from .args import parse_args
from .cli import obtain_parameters
from .makefile import generate_makefile


def create_makefile(params: dict):
	"""
	Create Makefile and fill it with user params
	"""
	content = generate_makefile(params)
	with open("Makefile", "w") as file:
		file.write(content)
		file.close()
	print(Fore.GREEN + "✅ Makefile created!" + Style.RESET_ALL)



def main():
	args = parse_args()
	p = Path('Makefile')
	if (args.remake == True) or not p.exists():
		params = obtain_parameters()
		create_makefile(params)
	populate_sources()

