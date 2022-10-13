"""from termcolor2 import c

print(c("Some text").white.on_blue.underline)
print("Datorika")
print(c("Jauna rindkopa").red)
print()

import wikipedia
wikipedia.set_lang("lv")
print(wikipedia.summary('Riga'))
print()

import pyperclip
pyperclip.copy("ifgjdfgkdfngfjkg")
pyperclip.paste()

import emojis
emojified = emojis.encode(":snake: :boot: :yellow_heart:  :innocent:!")
print(emojified)
  
from PIL import Image

def bilde():
    datne="bilde.jpg"
    with Image.open(datne) as im:
        print(datne, im.format, f"{im.size}x{im.mode}")
        im.show()
        izmers=(100,100)
        im.thumbnail(izmers)
        im.save("bilde-maza.jpg",im.format)
        im.show()
        
bilde()"""


from bs4 import BeautifulSoup
import requests


def apstrada_lapu(url):
    r=requests.get(url)
    html=r.textsoup=BeautifulSoup(html, 'html.parser')
    return soup

html=apstrada_lapu("https://www.tvnet.lv")
print(html.head.title.text)

"""import matplotlib.pyplot as plt
import numpy as np

def linijas():
    ypoints=np.array(np.random.randint(100, size=(10)))
    ypoints2=np.array(np.random.randint(100, size=(10)))
    ypoints3=np.array(np.random.randint(100, size=(60)))

    plt.plot(ypoints, 'o-')
    plt.plot(ypoints2, '+:r')
    plt.plot(ypoints3, '')
    plt.show()

linijas()"""

