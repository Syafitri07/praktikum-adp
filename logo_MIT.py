import os
from termcolor import colored, cprint

os.system ("cls")

# Baris pertama
for i in range (1):
    cprint(" "*3, "white", "on_red", end="")
    print(" "*2, end="")
    cprint(" "*3, "white", "on_red", end="")
    print(" "*2, end="")
    cprint(" "*3, "white", "on_red", end="")
    print(" "*2, end="")
    cprint(" "*3, "white", "on_red", end="")
    print(" "*2, end="")
    cprint(" "*7, "white", "on_red", end="")
    print()

# Baris kedua
for j in range (1):
    cprint(" "*3, "white", "on_red", end="")
    print(" "*2, end="")
    cprint(" "*3, "white", "on_red", end="")
    print(" "*2, end="")
    cprint(" "*3, "white", "on_red", end="")
    print(" "*2, end="")

    # Kolom keempat dan kelima kosong
    cprint(" "*3, end="")
    print(" "*2, end="")

    print()

# Baris ketiga dan keempat
for k in range (2):
    cprint(" "*3, "white", "on_red", end="")
    print(" "*2, end="")
    cprint(" "*3, "white", "on_red", end="")
    print(" "*2, end="")
    cprint(" "*3, "white", "on_red", end="")
    print(" "*2, end="")
    cprint(" "*3, "white", "on_dark_grey", end="")
    print(" "*2, end="")
    cprint(" "*3, "white", "on_red", end="")
    print()

# Baris kelima dan keenam
for l in range (2):
    cprint(" "*3, "white", "on_red", end="")
    print(" "*2, end="")

    # Kolom kedua kosong
    cprint(" "*3, end="")
    print(" "*2, end="")

    cprint(" "*3, "white", "on_red", end="")
    print(" "*2, end="")
    cprint(" "*3, "white", "on_dark_grey", end="")
    print(" "*2, end="")
    cprint(" "*3, "white", "on_red", end="")
    print()
