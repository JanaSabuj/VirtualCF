import os

fname = open('template.txt', "r")
txt = fname.read().strip()
fname.close()
print(txt)
