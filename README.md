# genMake

Disclaimer:

This is my first real Python project. I am not a Python developer, and the code is certainly not the cleanest. This project was developed according to my needs, and if you need more features I would be happy to integrate them if possible. I think it may be useful to others so I'll share it but without any guarantee.

## Description

This project allows to generate a Makefile compatible with the rules of school 42. It also allows to update the name of the sources in a fully automated way.

![genmake](assets/genmake.gif)


### Usage
```
genmake -h
usage: genmake [-h] [--version] [--remake]

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
  --remake    Delete and reconstruct Makefile
```

## Makefile
The Makefile will support the `libftprintf` and `minilibx` libraries (standard to 42). There is also a DEBUG rule as well as norm.
The Makefile will use GCC on MacOS and clang-9 on Linux

### Usage of makefile
```
make
make bonus
make BUILD=debug
make BUILD=valgrind
make re
make clean
make fclean
make libft
make minilibx
make norm
```

If you use the Debug rule, the following parameters will be added during compilation :
```
-DDEBUG -ggdb -fsanitize=address -fno-omit-frame-pointer
```
The valgrind rule is the same as above, but without fsanitize

## Installation
To install it just do :
```
pip3 install genmake
```
or on 42 iMac :
```
python3 -m pip install --user genmake
```

If the command is not available even after installation, please check that `$HOME/.local/bin` is in the PATH. If it is not the case you can add this to your `.zshrc` :
```
export PATH=$HOME/.local/bin:$PATH
```
or on 42 iMac :
```
export PATH=$HOME/Library/Python/3.7/bin:$PATH
```

## Upgrade
To update, this command is enough:
```
pip3 install genmake -U
```
or on 42 iMac :
```
pip3 install --user --upgrade genmake
```

### Known problems :
- The code is not clean
- Many parameters are hard-coded, it would be necessary to create a configuration file.
- You will tell me :D
