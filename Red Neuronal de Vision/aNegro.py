from PIL import Image
import numpy as np
datos=[0 for i in range(136)]
numero =1
while numero <136:
    width = 300
    height = 220
    foto = Image.open('C:\\Users\\an\\Desktop\\Pruebas\\Imagenes\\Imag\\'+ str(numero) + '.jpg')
    datos[numero-1] = np.array(foto.getdata())
     
    #para el calculo del promedio se utilizara la division entera con el operador de division doble "//" para evitar decimales
    promedio = [(datos[x][0] + datos[x][1] + datos[x][2]) // 3 for x in range(len(datos))]
     '''
  
     '''
    imagen_gris = Image.new('L', foto.size)
    '''
    Se genera un nueva foto solo teniendo encuenta la iluminancia de la imagen 
    '''
    imagen_gris.putdata(promedio)
    im = imagen_gris.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
    im.save('C:\\Users\\an\\Desktop\\Pruebas\\Imagenes\\ima\\BN'+ str(numero) + '.png')
     '''
     Ya que las imagenes tienen tamaños de 640*480 y estan en RGB(0-254) se normazila el los valores a 0-1 
     y se recude la imagen a una tamaño de 300*220 
     
    foto.close()
    imagen_gris.close()
    print(str(numero))
    numero=numero+1
    