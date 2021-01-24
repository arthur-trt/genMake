#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    config.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: atrouill <atrouill@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/24 15:24:16 by atrouill          #+#    #+#              #
#    Updated: 2021/01/24 15:24:17 by atrouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

PROG="genmake"
VERSION="0.3"
DESC="Generate Makefile for C Project of 42 School"

BUILDER=dict()
BUILDER["target"] = str()
BUILDER["src_dir"] = str()
BUILDER["inc_dir"] = str()
BUILDER["bin_dir"] = str()
BUILDER["lib"] = str()
BUILDER["all_rules"] = str()
BUILDER["clean_rules"] = str()
BUILDER["fclean_rules"] = str()
BUILDER["rules"] = str()
BUILDER["phony"] = str()
