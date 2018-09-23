Proyecto SIAT

Seleccion y preprocesamiento de datos
En este documento se explica como se seleccionaron los datos y su respectivo preprocesamiento para luego llevarlos
al diseño e implementacion de una red neuronal que pueda reconstruir las paradas de las rutas.

De la base de datos de validaciones suministrada por Transmilenio se escogieron 3 columnas:
-Fecha de ingreso: para saber el momento exacto del ingreso y introducir la variable tiempo al problema la cual es muy importante.
-Estacion: para saber el lugar en el cual el pasajero al sistema y asi poder evaluar los puntos de mayor conflicto entre otros.
-Id de la tarjeta: para saber que usuario ingreso y si accede mas de una vez al dia

De la base de datos de rutas se escogieron la siguientes columnas:
-Nombre de la ruta
-Paradas de la ruta

Estos datos se preparan para la red neuronal convirtiendolos en numeros, escogiendo etiquetas aleatorias para las estaciones, 
y para los nombres de las rutas, el resto de datos se trabaja en el mismo formato.
