#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cli.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: atrouill <atrouill@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/24 16:01:19 by atrouill          #+#    #+#              #
#    Updated: 2021/01/24 16:01:20 by atrouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from colorama import Fore, Style

def	input_bool(prompt: str) -> bool:
	while True:
		res = input(prompt)
		if not res or res.lower() == "n" or res.lower() == "no":
			return False
		elif res.lower() == "y" or res.lower() == "yes":
			return True
		else:
			continue

def obtain_parameters() -> dict:
	"""
	Obtain parameters from the user
	"""
	params = dict()
	print(Fore.CYAN + "MAKEFILE CONFIGURATION :" + Style.RESET_ALL)
	print(Style.BRIGHT + "A few questions to configure your Makefile as well as possible!" + Style.RESET_ALL)
	params["target"] = input("\tProgramm name : ")
	params["bin_folder"] = input("\tBinary folder name : ")
	params["src_folder"] = input("\tSource folder name : ")
	params["inc_folder"] = input("\tInclude folder name : ")
	print("\tLibraries : ")
	params["library_libft"] = input_bool("\t\tlibftprintf [y/N] : ")
	if params["library_libft"]:
		params["folder_libft"] = input("\t\t\tLibftprintf folder : ")
	params["library_mlx"] = input_bool("\t\tminilibx [y/N] : ")
	if params["library_mlx"]:
		params["compile_mlx"] = input_bool("\t\t\tDoes minilibx need to compile with your project? [y/N] : ")
		if params["compile_mlx"]:
			params["folder_mlx"] = input("\t\t\tMinilibx folder : ")
	params["library"] = input("\t\tOther argument for library (empty if none) : ")

	return params
