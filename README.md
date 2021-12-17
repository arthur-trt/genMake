# genMake

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/0-percent-optimized.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/contains-technical-debt.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/powered-by-overtime.svg)](https://forthebadge.com)

[![PyPI download month](https://img.shields.io/pypi/dm/genmake.svg)](https://pypi.python.org/pypi/genmake/) [![PyPi version](https://badgen.net/pypi/v/genmake/)](https://pypi.com/project/genmake)

Disclaimer:

This is my first real Python project. I am not a Python developer, and the code is certainly not the cleanest. This project was developed according to my needs, and if you need more features I would be happy to integrate them if possible. I think it may be useful to others so I'll share it but without any guarantee.

## Description

This project allows to generate a Makefile compatible with the rules of school 42. It also allows to update the name of the sources in a fully automated way.

![genmake](https://github.com/arthur-trt/genMake/raw/main/assets/genmake.gif)


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
or on 42 iMac MacOS :
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

### Thanks to :
- [Tart3mpion](https://github.com/Tart3mpion) for special support
- [tp0ns](https://github.com/tp0ns) for joy and amelioration idea
- [clbouche](https://github.com/clbouche) for joy and special skill in communication
- [Ccommiss](https://github.com/Ccommiss) for nothing but i appreciate you
- [EliasAachach](https://github.com/EliasAachach) special thanks to you best bro ❤️
