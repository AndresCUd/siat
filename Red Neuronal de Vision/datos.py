# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:58:44 2018

@author: an
"""
 
from numpy import genfromtxt
import pandas as pd

D =genfromtxt('Matriz_distancias_servicios_troncales.csv',delimiter=';',encoding='utf-8') 

df = pd.read_excel('Matriz_distancias_servicios_troncales.xlsx')
file= ('Matriz_distancias_servicios_troncales.xlsx') 
xl = pd.ExcelFile(file)
df = xl.parse('Hoja1')
Linea =df.loc['Nombre_linea']
C={}
D[0,3]=0
Ruta=D[:,3]

#while Ruta[1] == Ruta[1+i]:
 #       C[Ruta[1]]={D}
    
    
    