from numpy import genfromtxt
import numpy as np
import csv
#Debido a que la base de datos es demasiado grande se divide en batches
identificacion= genfromtxt('Validacion_Troncal_20180716.csv',encoding='utf8',delimiter=";",usecols=(1,8,13),skip_header=1,dtype=(str))
identificacion=identificacion[np.argsort(identificacion[:,2])]
batch=2000
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
with open("validacion.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(identificacion)