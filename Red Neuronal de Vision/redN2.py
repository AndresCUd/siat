# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 07:07:02 2018

@author: an
"""
'''
Librerias necesarias  para el manejo de redes neuronales 
'''
import tensorflow as tf
from tensorflow import keras
## Capa

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(480,640)),
    keras.layers.Dense(108, activation=tf.nn.relu),
    keras.layers.Dense(5, activation=tf.nn.softmax)
])
'''Se genrar una RN con una entrada de 480*640 y dos capas de nueronas 
una de 100 para la entrada y ya que se tienen 5 posibles salidas (Niveles)
se toma una capara de salida de 5 neuronas '''
model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
'''
Se especifican el metodo de obtimizaxion para la red neruronal  asi como la funcion objetico
y como se realizarian los cambios sobres esta
'''
#

model.fit(Ima, Label, epochs=10) 
'''
Entrena la Red neuronal en base a la informacion que se tenga
 '''