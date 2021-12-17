#!/bin/usr/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    args.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: atrouill <atrouill@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/24 13:49:19 by atrouill          #+#    #+#              #
#    Updated: 2021/01/24 13:49:20 by atrouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import genmake.config as config
import argparse

def	parse_args():
	parser = argparse.ArgumentParser(description=config.DESC)
	parser = argparse.ArgumentParser(prog=config.PROG)
	parser.add_argument('--remake',
		dest="remake",
		default=False,
		action="store_true",
		help='Delete and reconstruct Makefile'
	)
	parser.add_argument('--version',
		action='version',
		version='%(prog)s v' + config.VERSION
	)
	args = parser.parse_args()

	return args

