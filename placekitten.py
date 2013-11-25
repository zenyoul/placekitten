from requests import get
from random import randint
from os import environ

if environ["PROCESSOR_ARCHITECTURE"] == "x86":
    import win32api as winapi,win32con as wincon,win32gui as wingui
    version = 32
else:
    import win64api as winapi, win64con as wincon, win64gui as wingui

x = randint(300,1000)
y = x-randint(0,100)
url = "http://placekitten.com/{0}/{1}".format(x,y)

path = "kitten.png"

r = get(url, stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)

key = key = winapi.RegOpenKeyEx(wincon.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,wincon.KEY_SET_VALUE)
winapi.RegSetValueEx(key, "WallpaperStyle", 0, wincon.REG_SZ,"0")
winapi.RegSetValueEx(key, "TileWallpaper", 0, wincon.REG_SZ,"0")
wingui.SystemParametersInfo(wincon.SPI_SETDESKWALLPAPER, path, 1+2)
