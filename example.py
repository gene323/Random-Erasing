import os
from PIL import Image
from random_erase import get_random_eraser

PATH = ""
imgf = os.listdir(PATH)
labelf = os.listdir(PATH)
l = len(imgf)

eraser = get_random_eraser(mode='I+ORE')

for i in range(l):
	filename = ''
	Image.fromarray(eraser(imgf[i], labelf[i])).save(filename)
