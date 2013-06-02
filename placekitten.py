from urllib2 import urlopen
import random
import os
import ctypes

width = random.randint(200,500)
height = width-100

url = 'http://placekitten.com/' + str(width) + '/' + str(height)
kitten = urlopen(url).read()

os.chdir('C:/Users/Public')
f = open('kitten.bmp' , 'wb')
f.write(kitten)
f.close()

SPI_SETDESKWALLPAPER = 20 # According to http://support.microsoft.com/default.aspx?scid=97142

ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "kitten.bmp" , 0)
