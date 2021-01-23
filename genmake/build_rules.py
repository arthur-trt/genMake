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

def	clean_rules(rules: dict, params: dict):
	"""
	Build clean rules for Makefile
	"""
	rules["clean"] = "\t@$(RM) -rf $(BUILDDIR)\n"

	if params["library_libft"] == "y":
		rules["clean"] += "\t@make $@ -s -C " + params["folder_libft"] + "\n"
	if params["library_mlx"] == "y" and params["compile_mlx"] == "y":
		rules["clean"] += "\t@make $@ -s -C " + params["folder_mlx"] + "\n"

	return rules

def	fclean_rules(rules: dict, params: dict):
	"""
	Build fclean rules for Makefile
	"""
	rules["fclean"] = ""

	if params["bin_folder"] == ".":
		rules["fclean"] += "\t@$(RM) -rf $(TARGET)\n"
	else:
		rules["fclean"] += "\t@$(RM) -rf $(TARGETDIR)\n"
	if params["library_libft"] == "y":
		rules["fclean"] += "\t@make $@ -s -C " + params["folder_libft"] + "\n"

	return rules

def lib_rules(rules: dict, params: dict):
	"""
	Build rules for make lib
	"""
	rules["rules"] = ""

	if params["library_libft"] == "y":
		rules["rules"] += "libft:\n"
		rules["rules"] += "\t@make -s -C " + params["folder_libft"] + "\n"
	if params["library_mlx"] == "y" and params["compile_mlx"] == "y":
		rules["rules"] += "\nminilibx:\n"
		rules["rules"] += "\t@make -s -C " + params["folder_mlx"] + "\n"

	return rules

def all_rules(rules: dict, params: dict):
	"""
	Build rules for all with all lib
	"""
	rules["all_rules"] = "directories"

	if params["library_libft"] == "y":
		rules["all_rules"] += " libft"
	if params["library_mlx"] == "y" and params["compile_mlx"] == "y":
		rules["all_rules"] += " minilibx"
	rules["all_rules"] += " $(TARGET)"

	return rules

def lib_inc(rules: dict, params: dict):
	"""
	Build lib inc for linker settings
	"""
	rules["lib_inc"] = ""

	if params["library_libft"] == "y":
		rules["lib_inc"] += " -L" + params["folder_libft"] + " -lftprintf"
	if params["library_mlx"] == "y" and params["compile_mlx"] == "y":
		rules["lib_inc"] += " -L" + params["folder_mlx"] + " -lmlx"
	if params["library"]:
		rules["lib_inc"] += " " + params["library"]

	rules["lib_inc"] += "\n"

	return rules

def build_rules(params):
	"""
	Create rules str according to user information
	"""
	rules = dict()

	clean_rules(rules, params)
	fclean_rules(rules, params)
	lib_rules(rules, params)
	all_rules(rules, params)
	lib_inc(rules, params)

	return rules










