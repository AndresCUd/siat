import skimage.io as io
from PIL import Image
import numpy as np
from skimage import io
numero =1
cr=0
n=0
I=np.matrix([[0 for i in range(3)]for j in range(135)])
Label=np.zeros(135)
D=0
Ima=np.zeros((135,480,640))
while numero <136:
    cr=0
    n=0
    #foto = Image.open('C:\\Users\\an\\Desktop\\Pruebas\\Imagenes\\imf\\BN'+ str(numero) +'.jpg')
    foto = Image.open('C:\\Users\\an\\Desktop\\Pruebas\\Imagenes\\Imag\\'+ str(numero) +'.jpg')
    '''
    Cargar Imagenes necesarias para la deteccion de personas en la estacion 
    '''
    datos = list(foto.getdata())
    while n < len(datos):
        if datos[n][0] >datos[n][2]+10 :
          cr=cr+1
        n=n+1
    if cr <7000:
        Tipo=1
    elif cr >7000 and cr <=10000:
        Tipo=2
    elif cr >10000 and cr <=13000:
        Tipo=3
    elif cr >13000 and cr <=16000:
        Tipo=4
    elif cr >16000 :
        Tipo=5
        
        '''
       Asigna un identificador en base a al gunas caracteristicas de la imagen generando 
       asi niveles para la cantidad de personas en espera
        '''
    I[numero-1,:] = [len(datos)-cr,cr,numero] 
     #Toma las caracteriticas de la Imagenes para la RN 
     
    Ima[numero-1][:][:]= image=foto.convert('L')
    #Toma la ilumnancia de la imagen recibida  para alimentar la RN'''
    Label[numero-1]=Tipo-1 
    #Vector con los niveles de personas  en la estacion por imagen '''
    numero =numero +1


