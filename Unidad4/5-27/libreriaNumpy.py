# pip install numpy, codigo para instalar la libreria
import numpy as np

arr = np.array([1, 2, 3])  # array de 1 dimension
arr1 = np.array([[4, 6], [6, 7]])  # array de 2 dimensiones
arr2 = np.arange(24)
arr3 = np.arange(24).reshape(2, 12)  # 2 filas, de 12 columnas
arr4 = np.array([[i for i in range(1, 11)], [-j for j in range(1, 11)]])

print(arr)
# print(arr3)
# for num in arr3.flat:
# print(num)

# print(np.__version__)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])  # array de 3 dimensiones
# print(arr)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# ndim indica el numero de dimensiones
print(a.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print("El numero de dimensiones es: ", arr.ndim)
