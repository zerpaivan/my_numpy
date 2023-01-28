# importar libreria de numpy
import numpy as np
# np es una convencion para abreviar numpy

# Los datos contenidos en las arrays deben ser homogenos
# Los arrays son mas rapidos, y cosumen menos memoria que las listas.

# Un arrays es la estrutura de datos central en Numpy
# Es una cuadricula de valores que contiene informacion sobre datos

# ejemplo

a = np.array([1,2,3,4,5,6])
b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(type(a))
print(b)

print(b[0])

# ndarray significa un array N dimensional, es decir una matriz con cualquier numero de dimensiones
# 1D vector o array unidimensional
# 2D matriz o array bidimensional
# 3D o mas Tensor.

#  crear un array simple
simple_array = np.array([1,2.3])

# crear una array de ceros
cero_arrays = np.zeros(2)

# crear un array vacia (en realidad es array de contenido inicial aleatorio)
empty_array = np.empty(2)
print(empty_array)

# crear un array a partir de un intervalo(range)
# (np.arange(n1, n2, step size))
range_array = np.arange(0, 10, 2)
print(range_array)

# crear un array con valores espaciados linealmente
lineal_array= np.linspace(0, 10, num=5)
print(lineal_array)
