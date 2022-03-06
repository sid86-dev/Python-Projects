import pywhatkit as pwt
import os

p = pwt.image_to_ascii_art(f"{os.getcwd()}/cat.jpg")

print(p)