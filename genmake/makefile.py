#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    makefile.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: atrouill <atrouill@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/24 16:05:18 by atrouill          #+#    #+#              #
#    Updated: 2021/01/24 16:05:19 by atrouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import genmake.config as config
import genmake.build_rules as build_rules

def	generate_makefile(params: dict) -> str:

	config.BUILDER['target'] = params["target"]
	config.BUILDER["src_dir"] = params["src_folder"]
	config.BUILDER["inc_dir"] = params["inc_folder"]
	config.BUILDER["bin_dir"] = params["bin_folder"]
	config.BUILDER["lib"] = build_rules.lib_inc(params)
	config.BUILDER["all_rules"] = build_rules.all(params)
	config.BUILDER["clean_rules"] = build_rules.clean(params)
	config.BUILDER["fclean_rules"] = build_rules.fclean(params)
	config.BUILDER["rules"] = build_rules.lib(params)
	config.BUILDER["phony"] = build_rules.phony(params)

	content = '''\
#Compiler and Linker
CC			:= clang-9

#The Target Binary Program
TARGET			:= {target}

BUILD			:= release

include sources.mk

#The Directories, Source, Includes, Objects, Binary and Resources
SRCDIR			:= {src_dir}
INCDIR			:= {inc_dir}
BUILDDIR		:= obj
TARGETDIR		:= {bin_dir}
SRCEXT			:= c
DEPEXT			:= d
OBJEXT			:= o

OBJECTS			:= $(patsubst $(SRCDIR)/%,$(BUILDDIR)/%,$(SOURCES:.$(SRCEXT)=.$(OBJEXT)))

#Flags, Libraries and Includes
cflags.release		:= -Wall -Werror -Wextra
cflags.debug		:= -Wall -Werror -Wextra -DDEBUG -ggdb -fsanitize=address -fno-omit-frame-pointer
CFLAGS			:= $(cflags.$(BUILD))
LIB			:= {lib}
INC			:= -I$(INCDIR) -I/usr/local/include
INCDEP			:= -I$(INCDIR)

# Colors
C_RESET			:= \\033[0m
C_PENDING		:= \\033[0;36m
C_SUCCESS		:= \\033[0;32m

# Multi platforms
ECHO			:= echo

# Escape sequences (ANSI/VT100)
ES_ERASE		:= "\\033[1A\\033[2K\\033[1A"
ERASE			:= $(ECHO) $(ES_ERASE)

# hide STD/ERR and prevent Make from returning non-zero code
HIDE_STD		:= > /dev/null
HIDE_ERR		:= 2> /dev/null || true

GREP			:= grep --color=auto --exclude-dir=.git
NORMINETTE		:= norminette `ls`

#Defauilt Make
all: {all_rules}
	@$(ERASE)
	@$(ECHO) "$(TARGET)\\t\\t[$(C_SUCCESS)✅$(C_RESET)]"
	@$(ECHO) "$(C_SUCCESS)All done, compilation successful! 👌 $(C_RESET)"

#Remake
re: fclean all

#Make the Directories
directories:
	@mkdir -p $(TARGETDIR)
	@mkdir -p $(BUILDDIR)

#Clean only Objecst
clean:
{clean_rules}

#Full Clean, Objects and Binaries
fclean: clean
{fclean_rules}

#Pull in dependency info for *existing* .o files
-include $(OBJECTS:.$(OBJEXT)=.$(DEPEXT))

#Link
$(TARGET): $(OBJECTS)
	$(CC) -o $(TARGETDIR)/$(TARGET) $^ $(LIB)

#Compile
$(BUILDDIR)/%.$(OBJEXT): $(SRCDIR)/%.$(SRCEXT)
	@mkdir -p $(dir $@)
	@$(ECHO) "$(TARGET)\\t\\t[$(C_PENDING)⏳$(C_RESET)]"
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<
	@$(CC) $(CFLAGS) $(INCDEP) -MM $(SRCDIR)/$*.$(SRCEXT) > $(BUILDDIR)/$*.$(DEPEXT)
	@$(ERASE)
	@$(ERASE)
	@cp -f $(BUILDDIR)/$*.$(DEPEXT) $(BUILDDIR)/$*.$(DEPEXT).tmp
	@sed -e 's|.*:|$(BUILDDIR)/$*.$(OBJEXT):|' < $(BUILDDIR)/$*.$(DEPEXT).tmp > $(BUILDDIR)/$*.$(DEPEXT)
	@sed -e 's/.*://' -e 's/\\\\$$//' < $(BUILDDIR)/$*.$(DEPEXT).tmp | fmt -1 | sed -e 's/^ *//' -e 's/$$/:/' >> $(BUILDDIR)/$*.$(DEPEXT)
	@rm -f $(BUILDDIR)/$*.$(DEPEXT).tmp

{rules}

norm:
	@$(NORMINETTE) | $(GREP) -v "Not a valid file" | $(GREP) "Error\|Warning" -B 1 || true

#Non-File Targets
.PHONY: {phony}
\
'''

	return content.format(**config.BUILDER)
