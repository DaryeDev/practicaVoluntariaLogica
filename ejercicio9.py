import copy # Lo usaremos para poder hacer una copia, no vinculante, de la matriz original a la hora de hacer su complementaria.
from collections.abc import Sequence # Lo usaremos para crear una clase similar a una lista.

class MatrizC(Sequence):
    # Creación de un par de excepciones a la hora de la creación del objeto tipo MatrizC.
    class EmptyMatrixException(Exception):
        pass
    
    class NotSquareMatrixException(Exception):
        pass
    
    def __init__(self, numbers=[]):
        if len(numbers) == 0: # Si la matriz está vacía, mandaremos error...
            raise self.EmptyMatrixException("La matriz debe de tener elementos.")
        elif not all(len(row) == len(numbers) for row in numbers): #... y si la matriz no es cuadrada, también.
            raise self.NotSquareMatrixException("La matriz dada debe ser cuadrada. Comprueba que su número de filas equivale al número de columnas.")
        else:
            self.matrix = numbers
    
    def __str__(self) -> str:
        return str(self.matrix)
    
    def __getitem__(self, i):
        return self.matrix[i]
    
    def __len__(self):
        return len(self.matrix)
    
    # Apartado A.
    def complementaria(self, i, j):
        matrizComplementaria = copy.deepcopy(self.matrix)
        del matrizComplementaria[i]
        for fila in range(len(matrizComplementaria)):
            del matrizComplementaria[fila][j]
        return MatrizC(matrizComplementaria)
    
    def determinante(self):
        if len(self.matrix) == 1:
            return self.matrix[0][0]
        elif len(self.matrix) == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            determinante = 0
            for j in range(len(self.matrix)):
                submatriz = self.complementaria(0, j)
                signo = (-1) ** j
                determinante += signo * self.matrix[0][j] * MatrizC(submatriz).determinante()
            return determinante
    
    # Apartado B.
    def productoMatricial(self, matriz):
        return [[sum(self.matrix[i][k] * matriz[k][j] for k in range(len(self.matrix))) for j in range(len(matriz[0]))] for i in range(len(self.matrix))]
    
    def potenciaMatricial(self, n):
        if n == 0:
            return [[1 if i == j else 0 for j in range(len(self.matrix))] for i in range(len(self.matrix))] # Si el exponente es 0, devolveremos la matriz identidad...
        if n == 1:
            return self.matrix # ..., si es uno, devolveremos la propia matriz... 
        elif n % 2 == 0:
            submatriz = self.potenciaMatricial(n/2)
            return MatrizC(submatriz).productoMatricial(submatriz)
        else:
            submatriz = self.potenciaMatricial((n-1)/2)
            return self.productoMatricial(MatrizC(submatriz).productoMatricial(submatriz))


print("Test determinante:")
m = MatrizC([[1, 3, 9], [2, 5, 7], [1, 2, 3]])
c = m.complementaria(1, 1)
d = m.determinante()
print("Matriz:", m)
print("Matriz Complementaria (1, 1):", c)
print("Determinante:", d)
print("====================================================")
m = MatrizC([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print("Test potencias:")
print("Matriz:", m)
print("Elevado a 0", m.potenciaMatricial(0))
print("Elevado a 1", m.potenciaMatricial(1))
print("Elevado a 2", m.potenciaMatricial(2))
print("Elevado a 3", m.potenciaMatricial(3))
print("Elevado a 4", m.potenciaMatricial(4))