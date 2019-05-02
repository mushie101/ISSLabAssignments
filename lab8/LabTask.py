#!/usr/bin/env python

# Lab - 8 Task

class Matrix:
    ar = []
    def __init__(self, *dims, **kw):
        self.dims = dims
        kk = kw.get("mat", None)
        self.mat = []
        if kk:
            self.mat = kk
        else:
            lol = []
            for i in range(dims[1]):
                lol.append(0)
            for j in range(dims[0]):
                self.mat.append(lol)
    
    def __getitem__(self, x):
        if type(self.mat[0]) == list:
            return Matrix(mat=self.mat[x])
        else:
            return self.mat[x]
    
    def __str__(self):
        return str(self.mat)
    
    def __add__(self, bcl):
        a = []
        for i in range(len(self.mat)):
            lol = []
            for j in range(len(self.mat[0])):
                lol.append(self.mat[i][j])
            a.append(lol)
        b = bcl.mat
        for i in range(len(b)):
            for j in range(len(b[0])):
                a[i][j] += b[i][j]
        return a

    def __sub__(self, bcl):
        a = []
        for i in range(len(self.mat)):
                lol = []
                for j in range(len(self.mat[0])):
                        lol.append(self.mat[i][j])
                a.append(lol)
        b = bcl.mat
        for i in range(len(b)):
            for j in range(len(b[0])):
                a[i][j] -= b[i][j]
        return a

    def __pow__(self, bcl):
        a = []
        for i in range(len(self.mat)):
                lol = []
                for j in range(len(self.mat[0])):
                        lol.append(self.mat[i][j])
                a.append(lol)
        b = bcl.mat
        for i in range(len(b)):
            for j in range(len(b[0])):
                a[i][j] *= b[i][j]
        return a

    def __floordiv__(self, bcl):
        a = []
        for i in range(len(self.mat)):
                lol = []
                for j in range(len(self.mat[0])):
                        lol.append(self.mat[i][j])
                a.append(lol)
        b = bcl.mat
        for i in range(len(b)):
            for j in range(len(b[0])):
                a[i][j] /= b[i][j]
        return a

    def __lt__(self, bcl):
        a = []
        for i in range(len(self.mat)):
                lol = []
                for j in range(len(self.mat[0])):
                        lol.append(self.mat[i][j])
                a.append(lol)
        b = bcl.mat
        for i in range(len(b)):
            for j in range(len(b[0])):
                a[i][j] = (a[i][j] < b[i][j])
        return a

    def __le__(self, bcl):
        a = []
        for i in range(len(self.mat)):
                lol = []
                for j in range(len(self.mat[0])):
                        lol.append(self.mat[i][j])
                a.append(lol)
        b = bcl.mat
        for i in range(len(b)):
            for j in range(len(b[0])):
                a[i][j] = (a[i][j] <= b[i][j])
        return a

    def __gt__(self, bcl):
        a = []
        for i in range(len(self.mat)):
                lol = []
                for j in range(len(self.mat[0])):
                        lol.append(self.mat[i][j])
                a.append(lol)
        b = bcl.mat
        for i in range(len(b)):
            for j in range(len(b[0])):
                a[i][j] = (a[i][j] > b[i][j])
        return a

    def __ge__(self, bcl):
        a = []
        for i in range(len(self.mat)):
                lol = []
                for j in range(len(self.mat[0])):
                        lol.append(self.mat[i][j])
                a.append(lol)
        b = bcl.mat
        for i in range(len(b)):
            for j in range(len(b[0])):
                a[i][j] = (a[i][j] >= b[i][j])
        return a

    def __eq__(self, bcl):
        a = []
        for i in range(len(self.mat)):
                lol = []
                for j in range(len(self.mat[0])):
                        lol.append(self.mat[i][j])
                a.append(lol)
        b = bcl.mat
        for i in range(len(b)):
            for j in range(len(b[0])):
                a[i][j] = (a[i][j] == b[i][j])
        return a

    def __ne__(self, bcl):
        a = []
        for i in range(len(self.mat)):
                lol = []
                for j in range(len(self.mat[0])):
                        lol.append(self.mat[i][j])
                a.append(lol)
        b = bcl.mat
        for i in range(len(b)):
            for j in range(len(b[0])):
                a[i][j] = (a[i][j] != b[i][j])
        return a

    def __mul__(self, bcl):
        ans = []
        for i in range(len(self.mat)):
                lol = []
                for j in range(len(bcl.mat[0])):
                        lol.append(0)
                ans.append(lol)
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                su = 0
                for k in range(len(self.mat[0])):
                    su += self.mat[i][k] * bcl.mat[k][j]
                ans[i][j] = su
        return ans
        
    
    def transpose(self):
        tr = []
        for j in range(len(self.mat[0])):
            l = []
            for i in range(len(self.mat)):
                l.append(self.mat[i][j]) 
            tr.append(l)
        return tr

    pass
    
m = Matrix(2, 3, mat=[[1, 2, 3], [4, 5, 6]])
print(m[1][0])
print(m)
print(m ** Matrix(2, 2, mat=[[1, 2, 3], [4, 5, 6]]))
print(m.transpose())
#print(m != Matrix(3, 2, mat=[[10, 10], [3, 20], [6, 100]]))
print(m * Matrix(3, 2, mat=[[1, 1], [1, 1], [1, 1]]))


class Vector(Matrix):
    def __getitem__(self, x):
        return self.mat[x][0]
    
    def __mod__(self, bcl):
        c = []
        for i in range(len(self.mat)):
            c.append(self.mat[i][0] * bcl.mat[i][0])
        return sum(c)
    
    def transpose(self):
        return "Error, transpose not defined for vector."
    
    def norm(self):
        n = 0
        for i in range(len(self.mat)):
            n += self.mat[i][0]**2
        n = n**(1/2)
        return n

v = Vector(1, 3, mat=[[2], [3], [4]])
print(v%Vector(1, 3, mat=[[1], [1], [0]]))
v = Vector(1, 2, mat=[[3], [5]])
print(v.norm())

