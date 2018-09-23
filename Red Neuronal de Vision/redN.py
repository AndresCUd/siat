# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 07:07:02 2018

@author: an
"""

import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

class_names = ['Poca','Medio-Baja','Media','Media -Alta','Alta']
plt.figure()
plt.imshow(foto)
plt.colorbar()
plt.grid(False)
plt.figure(figsize=(10,10))

## Capa

model = keras.Sequential([
    keras.layers.Dense(100, activation=tf.nn.relu,
                       input_shape=(2,)),
    keras.layers.Dense(80, activation=tf.nn.relu),
    keras.layers.Dense(6, activation=tf.nn.softmax)
])
model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
#
trainI=I[2:-1,0:2]
model.fit(trainI, Label, epochs=10)