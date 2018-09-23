'''Preprocesamiento de las variables'''
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np
import matplotlib.animation as animation

identificacion= genfromtxt('validacion.csv',delimiter=",",dtype=(str))
id2=identificacion
for i in range(id2.shape[0]):
    print(i)
    id2[i,0]=str(id2[i,0])[8:12]
identificacion=identificacion[np.argsort(identificacion[:,1])]
a={}
for j in range(4,23):
    a[j]=[]
    print('Hora '+str(j)+':00 a '+str(j+1)+':00 am')
    t=str(j)
    if len(str(j))==1:
        t='0'+str(j)
    for i in range(0,60):
        if len(str(i))==1:
            i='0'+str(i)
        a[j]=np.append(a[j],np.where(identificacion[:,0]==str(str(t)+str(i))))
    a[j]=np.array(a[j],dtype=int)
    plt.figure(figsize=(21,9))
    plt.hist(identificacion[a[j],1], bins=149)
    plt.ylim(ymax= 6000)
    plt.title('Hora '+str(j)+':00 a '+str(j+1)+':00 am',fontsize=40)
    plt.xticks(rotation='vertical',fontsize=5)
    plt.yticks(fontsize=10)
    plt.xlabel('Estaciones',fontsize=20)
    plt.ylabel('Validaciones por hora',fontsize=40)
    plt.show()
    plt.savefig(str(j)+'.jpg',)