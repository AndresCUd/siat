# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 22:51:57 2018

@author: an
"""

import numpy as np
import matplotlib.pyplot as plt

plt.ion() # decimos de forma explícita que sea interactivo

y = [] # los datos que vamos a dibujar y a actualizar

# el bucle infinito que irá dibujando
while True:
    y.append(np.random.randn(1)) # añadimos un valor aleatorio a la lista 'y'

    # Estas condiciones las he incluido solo para dibujar los últimos 
    # 10 datos de la lista 'y' ya que quiero que en el gráfico se 
    # vea la evolución de los últimos datos
    if len(y) <= 10:
        plt.plot(y)
    else:
        plt.plot(y[-10:])

    plt.pause(0.05) # esto pausará el gráfico
    plt.cla() # esto limpia la información del axis (el área blanca donde
              # se pintan las cosas.