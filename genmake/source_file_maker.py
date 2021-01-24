#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    source_file_maker.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: atrouill <atrouill@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/21 23:34:32 by atrouill          #+#    #+#              #
#    Updated: 2021/01/22 00:47:16 by atrouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import pathlib
import fileinput

from colorama.ansi import Fore, Style

sources_file_path = "./sources.mk"

def obtain_list_file(path, extension):
	p = path.glob('*')
	files = [x for x in p if x.is_file() and x.suffix == extension]
	return files

def obtain_list_dir(src_folder: str):
	p = pathlib.Path(r'.').glob(src_folder + '/**')
	dir = [x for x in p if x.is_dir()]
	return dir

def write_comment(file, text: str):
	file.write("## " + text.upper() + " ##\n\n")

def write_file_list(source_file, files):
	source_file.write("SOURCES\t\t+=\n")
	for file in files:
		source_file.write("\t\t" + str(file) + "\n")
	source_file.write("\n\n")

def build_source_file(source_file):
	dirs = obtain_list_dir(obtain_src_folder())
	for dir in dirs:
		files = obtain_list_file(dir, ".c")
		if files:
			write_comment(source_file, str(dir))
			write_file_list(source_file, files)

def obtain_max_lenght(source_file):
	max_length = 0
	source_file.seek(0, os.SEEK_SET)
	for line in source_file:
		if(len(line) > max_length):
	  	  max_length = len(line)
	return max_length

def beautify_file(sources_file_path, len: int):
	"""
	Check file if everything is aligned
	"""
	for line in fileinput.input(sources_file_path, inplace=True):
		if ".c" in line:
			print('{0:{len}}{1}'.format(line.rstrip(), "\t\\\n", len=len), end='')
		elif "+=" in line:
			print('{0:{len}}{1}'.format(line.rstrip(), "\t\t\\\n", len=len), end='')
		else:
			print(line, end='')

def create_source_file():
	"""
	Create sources.mk
	"""
	p = pathlib.Path(sources_file_path)
	if p.exists():
		os.remove(sources_file_path)
	source_file = open(sources_file_path, 'w+')
	write_comment(source_file, p.name)
	return source_file

def obtain_src_folder():
	"""
	Parse Makefile and return the SRCDIR configured by user
	"""
	with open("Makefile", 'r') as file:
		for line in file:
			if "SRCDIR" in line:
				src_folder = line.split()
				file.close()
				return src_folder[-1]

def populate_sources():
	"""
	List all .c files and create sources.mk
	"""
	source_file = create_source_file()

	build_source_file(source_file)
	max_lenght = obtain_max_lenght(source_file)
	beautify_file(sources_file_path, max_lenght + 5)
	source_file.close()
	print(Fore.GREEN + "✅ Makefile updated!" + Style.RESET_ALL)
