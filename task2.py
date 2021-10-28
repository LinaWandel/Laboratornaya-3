import math
import numpy as np
from numpy import linalg as LA

class Matrix:
    def __init__(self, frmatrix, scmatrix):
        self.frmatrix, self.scmatrix = frmatrix, scmatrix
    def compare(self):
        if LA.det(self.frmatrix) > LA.det(self.scmatrix):
            print("Первая матрица больше")
        elif LA.det(self.frmatrix) < LA.det(self.scmatrix):
            print("Вторая матрица больше")
        else: print("Матрицы равны")
        
    def summ(self):
        res = [[self.frmatrix[i][j] + self.scmatrix[i][j]  for j in range
(len(self.frmatrix[0]))] for i in range(len(self.frmatrix))] 
        print("Сумма матриц = ", res)
        
    def multiply(self):
        temp = frmatrix.dot(scmatrix) 
        temp2 = scmatrix.dot(frmatrix) 
        print("Первая х Вторая = ", temp)
        print("Вторая х Первая = ", temp2)
first = ([500,900], [100,400])
second = ([5,8], [10,4])
mtrx = Matrix(first, second)
mtrx.compare()
mtrx.summ()