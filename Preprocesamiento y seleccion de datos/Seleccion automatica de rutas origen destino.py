import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np
#Funcion para establecer los transmilenios que debe tomar el pasajero para ir de un origen a un destino.
def buscarruta(origen,destino):
    tomar=""
    origen=origen.lower()
    destino=destino.lower()
    for i in range(139):
        a=0
        for j in range(buses[i].shape[0]):
            s = buses[i][j].lower()
            if s.find(origen) == -1:
                
            else:
                a=1
            if (s.find(destino) == -1):
                afg=1
            else:
                if(a==1):
                    a=2
                #Existe el origen en la ruta"
                
        if (a==2):
            tomar=buses_nombre[i]
            print(tomar+str(i))
    if (tomar==""):
        torigen=[]
        tdestino=[]
        for i in range(139):
            for j in range(buses[i].shape[0]):
                s = buses[i][j].lower()
                if s.find(origen) == -1:
                    afg=1
                else:
                    torigen=np.append(torigen,i)
                if s.find(origen) == -1:
                    afg=1
                else:
                    tdestino=np.append(tdestino,i)
        for i in range(torigen.shape[0]):
            for j in range(tdestino.shape[0]):
                if((buses[i]==buses[j]).any() and i!=j):
                    print('tomar '+str(buses_nombre[i])+' y luego '+str(buses_nombre[j]))
                    
                    
            
identificacion= genfromtxt('validacion.csv',encoding='utf8',delimiter=",",dtype=(str))
estacion = genfromtxt('Validacion_Troncal_20180716.csv',encoding='utf8',delimiter=";",usecols=(8),dtype=(str),skip_header=1)
identificacion = genfromtxt('Validacion_Troncal_20180716.csv',encoding='utf8',delimiter=";",usecols=(13),skip_header=1)
identificacion=identificacion[np.argsort(identificacion[:,2])]
batch=20
b=np.array([])
c=0
for j in range(batch):
    print('batch actual '+str(j))
    batchinicio=int((identificacion.shape[0]/batch)*j)
    batchfin=int((identificacion.shape[0]/batch)*(j+1))
    idbatch=identificacion[batchinicio:batchfin,2]
    i=0
    while (i <(batchfin-batchinicio)):
        print('dato '+str(i+batchinicio))
        a=np.where(idbatch==idbatch[i])[0]
        if(a.shape[0]!=2):
            print('borro '+str(a+batchinicio))
            b=np.append(b,a+batchinicio)
        i+=1
    b=np.array(list(set(b)))
identificacion=np.delete(identificacion,b,0)
np.savetxt("validaciones.csv", identificacion, delimiter=",")

buses={}
buses_csv=genfromtxt('buses.csv',encoding='utf8',delimiter=",",dtype=(str))
ruta_ant=""
ind=-1
buses_nombre=[]
for i in range(buses_csv.shape[0]):
    ruta=buses_csv[i,0]
    if(ruta==ruta_ant):
        buses[ind]=np.append(buses[ind],buses_csv[i,1])
    else:
        ind+=1
        buses_nombre=np.append(buses_nombre,ruta)
        ruta_ant=ruta
        buses[ind]=np.array([])
        buses[ind]=np.append(buses[ind],buses_csv[i,1])


identificacion=identificacion[np.argsort(identificacion[:,1])]
estaciones={}
n_estaciones=[]
est_ant=""
ind=-1
for i in range(identificacion.shape[0]):
    print(str(i))
    est=identificacion[i,2]
    if(est==est_ant):
        estaciones[ind]=np.vstack((estaciones[ind],identificacion[i]))
    else:
        ind+=1
        n_estaciones=np.append(n_estaciones,est)
        est_ant=est
        estaciones[ind]=identificacion[i]
        


