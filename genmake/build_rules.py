#!/bin/usr/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    build_rules.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: atrouill <atrouill@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/23 19:15:47 by atrouill          #+#    #+#              #
#    Updated: 2021/01/23 19:15:48 by atrouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	clean(params: dict) -> str:
	"""
	Build clean rules for Makefile
	"""
	clean = "\t@$(RM) -rf $(BUILDDIR)\n"

	if params["library_libft"]:
		clean += "\t@make $@ -C " + params["folder_libft"] + "\n"
	if params["library_mlx"] and params["compile_mlx"]:
		clean += "\t@make $@ -C " + params["folder_mlx"] + "\n"

	return clean

def	fclean(params: dict) -> str:
	"""
	Build fclean rules for Makefile
	"""
	fclean = str()

	if params["bin_folder"] == ".":
		fclean += "\t@$(RM) -rf $(TARGET)\n"
	else:
		fclean += "\t@$(RM) -rf $(TARGETDIR)\n"
	if params["library_libft"]:
		fclean += "\t@make $@ -C " + params["folder_libft"] + "\n"

	return fclean

def lib(params: dict) -> str:
	"""
	Build rules for make lib
	"""
	rules = str()

	if params["library_libft"]:
		rules += "libft:\n"
		rules += "\t@make -C " + params["folder_libft"] + "\n"
	if params["library_mlx"] and params["compile_mlx"]:
		rules += "\nminilibx:\n"
		rules += "\t@make -C " + params["folder_mlx"] + "\n"

	return rules

def all(params: dict) -> str:
	"""
	Build rules for all with all lib
	"""
	all_rules = str()

	if params["library_libft"]:
		all_rules += " libft"
	if params["library_mlx"] and params["compile_mlx"]:
		all_rules += " minilibx"
	all_rules += " $(TARGETDIR)/$(TARGET)"

	return all_rules

def bonus(params: dict) -> str:
	"""
	Build rules for bonus with all lib
	"""
	all_rules = str()

	if params["library_libft"]:
		all_rules += " libft"
	if params["library_mlx"] and params["compile_mlx"]:
		all_rules += " minilibx"
	all_rules += " $(TARGETDIR)/$(TARGET_BONUS)"

	return all_rules

def lib_inc(params: dict) -> str:
	"""
	Build lib inc for linker settings
	"""
	lib_inc = str()

	if params["library_libft"]:
		lib_inc += " -L" + params["folder_libft"] + " -lftprintf"
	if params["library_mlx"] and params["compile_mlx"]:
		lib_inc += " -L" + params["folder_mlx"] + " -lmlx"
	if params["library"]:
		lib_inc += " " + params["library"]

	return lib_inc

def phony(params: dict) -> str:
	"""
	Build phony rules according to 42 rules
	"""
	phony = "all re clean fclean norm bonus"

	if params["library_libft"]:
		phony += " libft"
	if params["library_mlx"] and params["compile_mlx"]:
		phony += " minilibx"

	return phony
