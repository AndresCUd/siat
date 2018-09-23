# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 09:05:18 2018

@author: an
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.animation as animation

 
foto1 = Image.open('C:\\Users\\an\\Desktop\\Pruebas\\imagen1.PNG')
foto2 = Image.open('C:\\Users\\an\\Desktop\\Pruebas\\imagen2.PNG')
foto3 = Image.open('C:\\Users\\an\\Desktop\\Pruebas\\imagen3.PNG')
foto4 = Image.open('C:\\Users\\an\\Desktop\\Pruebas\\imagen4.PNG')
foto5 = Image.open('C:\\Users\\an\\Desktop\\Pruebas\\imagen5.PNG')

objects = ('Bajo', 'Medio Bajo', 'Medio', 'Medio Alto', 'Alto')
y_pos = np.arange(len(objects))
performance1 = [[0,2,4,3,1],[10,8,6,4,2],[10,8,6,4,2],[10,8,6,4,2], [10,8,6,4,2]]

fig, ax = plt.subplots()

def animate(i):
    plt.cla()
    plt.subplot(211)
    plt.bar(y_pos, performance1, align='center', alpha=0.75)
    plt.xticks(y_pos, objects)
    plt.ylabel('Pertenencia')
    plt.title('Clasificacion / Prediccion')
    plt.subplot(212)
    plt.imshow(foto1)
    
    plt.cla()
    plt.subplot(211)
    plt.bar(y_pos, performance2, align='center', alpha=0.75)
    plt.xticks(y_pos, objects)
    plt.ylabel('Pertenencia')
    plt.title('Clasificacion / Prediccion')
    plt.subplot(212)
    plt.imshow(foto2)
    return 0

ani = animation.FuncAnimation(fig, animate, 100, repeat=False, blit=True)
plt.show()