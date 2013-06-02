from urllib2 import urlopen
import random
import os
import ctypes

width = random.randint(200,500)
height = width-random.randint(1,100)

url = 'http://placekitten.com/{0}/{1}'.format(str(width),str(height))
kitten = urlopen(url).read()

os.chdir('C:/Users/Public')
with open('kitten.bmp' , 'wb') as f: f.write(kitten)
f.close()

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "kitten.bmp" , 0)
