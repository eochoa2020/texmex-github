#!/usr/bin/python3

import sys

with open("./recetas.md", "r") as file:
    content = file.read()
    print(content)

sys.exit()