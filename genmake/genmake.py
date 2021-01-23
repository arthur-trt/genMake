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

from colorama import Fore, Back, Style
from requests import get
import fileinput
import sys
import argparse
from . import source_file_maker
from . import build_rules
import pathlib

def obtain_parameters():
	"""
	Obtain parameters from the user
	"""
	params = dict()
	print(Fore.CYAN + "MAKEFILE CONFIGURATION :" + Style.RESET_ALL)
	print(Style.BRIGHT + "A few questions to configure your Makefile as well as possible!" + Style.RESET_ALL)
	print("\tProgramm name : ", end='')
	params["target"] = str(input())
	print("\tBinary folder name : ", end='')
	params["bin_folder"] = str(input())
	print("\tSource folder name : ", end='')
	params["src_folder"] = str(input())
	print("\tInclude folder name : ", end='')
	params["inc_folder"] = str(input())
	print("\tLibraries : ")
	print("\t\tlibftprintf [y/n] : ", end='')
	params["library_libft"] = str(input())
	if params["library_libft"] == "y":
		print("\t\t\tLibftprintf folder : ", end='')
		params["folder_libft"] = str(input())
	print("\t\tminilibx [y/n] : ", end='')
	params["library_mlx"] = str(input())
	if params["library_mlx"] == "y":
		print("\t\t\tDoes minilibx need to compile with your project? [y/n] : ", end='')
		params["compile_mlx"] = str(input())
		if params["compile_mlx"] == "y":
			print("\t\t\tMinilibx folder : ", end='')
			params["folder_mlx"] = str(input())
	print("\t\tOther argument for library (empty if none) : ", end='')
	params["library"] = str(input())
	return params

def create_makefile(params):
	"""
	Create Makefile and fill it with user params
	"""
	with open("Makefile", "wb") as file:
		r = get("https://raw.githubusercontent.com/arthur-trt/genMake/main/template")
		file.write(r.content)
		file.close()
	for line in fileinput.input("Makefile", inplace=True):
		if "VAR_TARGET_NAME" in line:
			print(line.replace("VAR_TARGET_NAME", params["target"]), end='')
		elif "VAR_SRCS_DIR" in line:
			print(line.replace("VAR_SRCS_DIR", params["src_folder"]), end='')
		elif "VAR_INC_DIR" in line:
			print(line.replace("VAR_INC_DIR", params["inc_folder"]), end='')
		elif "VAR_BIN_DIR" in line:
			print(line.replace("VAR_BIN_DIR", params["bin_folder"]), end='')
		else:
			print(line, end='')
	set_rules(params)
	print(Fore.GREEN + "✅ Makefile created!" + Style.RESET_ALL)

def set_rules(params):
	"""
	Modifying rules with user informations
	"""
	rules = build_rules.build_rules(params)
	for line in fileinput.input("Makefile", inplace=True):
		if "VAR_LIB" in line:
			print(line.replace("VAR_LIB", rules["lib_inc"]), end='')
		elif "ALL_RULES" in line:
			print(line.replace("ALL_RULES", rules["all_rules"]), end='')
		elif "FCLEAN_RULES" in line:
			print(line.replace("FCLEAN_RULES", rules["fclean"]), end='')
		elif "CLEAN_RULES" in line:
			print(line.replace("CLEAN_RULES", rules["clean"]), end='')
		elif "RULES" in line:
			print(line.replace("RULES", rules["rules"]), end='')
		else:
			print(line, end='')


def main():
	parser = argparse.ArgumentParser(description='Generate Makefile for C Projects')
	parser = argparse.ArgumentParser(prog='genmake')
	parser.add_argument('--version', action='version', version='%(prog)s 0.2.3')
	parser.add_argument('--remake',
		action="store_true",
		help='Delete and reconstruct Makefile'
	)
	args = parser.parse_args()
	p = pathlib.Path('Makefile')
	if (args.remake == True) or not p.exists():
		params = obtain_parameters()
		create_makefile(params)
	source_file_maker.populate_sources()

