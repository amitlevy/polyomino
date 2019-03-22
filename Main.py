import numpy as np

class Poly:
    def __init__(self,size):
        self.size = size
        self.emptyrow = [False for i in range(size)]
        self.data = [self.emptyrow[:] for i in range(size)]
        self.middle = (size-1)//2
        self.data[self.middle][self.middle] = True

    def set(self,i,j,data):
        self.data[i][j] = bool(data)

    def display(self):
        for row in self.data:
            for item in row:
                if item:
                    print('■',end=' ')
                else:
                    print('□',end=' ')
            print()

    def is_legal(self,i,j):
        if self.data[i-1][j] or self.data[i][j-1] or self.data[i+1][j] or self.data[i][j+1]:
            return True
        return False
    
    def is_poly(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j]:
                    if not self.is_legal(i,j):
                        return False
        return True

    def rotate(self):
       self.data = np.rot90(self.data)

    def center(self):
        size = self.size
        min_i = size-1
        for i in range(size):
            if self.data[i] != self.emptyrow:
                min_i = i
                break
        min_j = size-1
        for j in range(size):
            for row in self.data:
                if row[j] != False:
                    min_j = j
                    break
            if min_j != size-1:
                break
        max_i = 0
        for i in reversed(range(size)):
            if self.data[i] != self.emptyrow:
                max_i = i
                break
        max_j = 0
        for j in reversed(range(size)):
            for row in self.data:
                if row[j] != False:
                    max_j = j
                    break
            if max_j != 0:
                break

        result = self.data[min_i:max_i+1]
        for i in range(max_i+1-min_i):
            result[i] = result[i][min_j:max_j+1]
        return result                

def is_equiv(poly1,poly2):
    result = False
    pcenter = poly1.center()
    for i in range(4):
        if pcenter == poly2.center():
            result = True
        poly2.rotate()
    return result

def generate(polies):
    result = []
    for poly in polies:
        for i in range(poly.size):
            for j in range(poly.size):
                pass
              
                    
