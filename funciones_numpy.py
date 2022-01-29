import numpy as np

#Formas de crear arreglos (ndarray)

#con una lista de python
datos = np.array([1,2,3])
print(datos)

#con una lista multidimensional de python
datos = np.array([[1,2],[3,4]])
print(datos)

#con constantes

#ceros
datos = np.zeros((5,3))
print(datos)
print(datos.dtype)

datos = np.ones((4,3), dtype=np.int64)
print(datos)
print(datos.dtype)

#constantes arbitrarias
datos = np.ones((4,3)) * 3.5
datos = np.full((4,3), 3.5)
datos = np.empty((4,3))
datos.fill(7.4)
print(datos)

#secuencias incrementales
datos = np.arange(10)
#start, stop, step
datos = np.arange(3,15,0.5)
datos = np.linspace(0,10,11)
print(datos)
print(datos.shape)

#secuencias logaritmicas
#   10**0  10**2
#   1      100
datos = np.logspace(0,2,5)
print(datos)
print(datos.shape)

#Meshgrid
x = np.array([1,2,3,4,5], dtype = np.float64)
y = np.array([6,7,8])

XX,YY = np.meshgrid(x,y)
print(XX)
print(YY)

datos = np.ones_like(XX)
datos = np.zeros_like(XX)
datos = np.full_like(XX,3.8)

print(datos)

datos = np.identity(4)
print(datos)

datos = np.eye(4, k=1)
print(datos)

datos = np.diag(np.array([2,2,0,1]))
print(datos)