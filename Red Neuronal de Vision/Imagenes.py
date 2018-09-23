# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 22:05:09 2018

@author: an
"""

from __future__ import division   # fuerza aritmética no entera
from PIL import Image                 # funciones para cargar y manipular imágenes
import numpy as np                # funciones numéricas (arrays, matrices, etc.)
import matplotlib.pyplot as plt   # funciones para representación gráfica

from scipy import ndimage
I = Image.open("20_09_2018 5_59_59 a.m. (UTC-05_00) 1315.jpg")
#I.show()

 im = np.zeros((256, 256))
 im[64:-64, 64:-64] = 1
 im = ndimage.rotate(im, 15, mode='constant')
 im = ndimage.gaussian_filter(im, 8)
 
ax1 = fig.add_subplot(121)  # left side
ax2 = fig.add_subplot(122) 
ax1.imshow(Imagenes[i])
ax2.imshow(Resultados[i])
 plt.legend()

# Show the plot
plt.show()