import scipy.io as scio
import pandas as pd
import numpy as np
import math
import csv


def group(data):

    num = np.zeros([36, 18], dtype=np.int32)
    r, a = np.shape(data)
    group = np.zeros((36, 18, 200), dtype=np.int32)
    for k in range(r):
        a, b = math.floor(data[k][1] / 10), math.floor((math.floor(data[k][2]) / 10) + 9)
        num[a, b] += 1
        c = num[a, b]
        group[a, b, c] = k
    return group


def getNonezero(group):
    num = np.zeros([36, 18], dtype=np.int32)
    for i in range(36):
        for j in range(18):
            a = np.nonzero(group[i][j])
            # print(a)


def locationMatrix(matrix):
    ans = []
    for element in matrix:
        if element != 0:
            ans.append(element)
    return ans


def LocationMatrix(data):
    a = {}
    Lmatrix = {}
    Lambda = {}
    for i in range(36):
        for j in range(18):
            a[(i, j)] = locationMatrix(groups[i, j])
    for i in range(36):
        for j in range(18):
            location = np.zeros([10, 10], dtype=np.int32)
            for ele in a[(i, j)]:
                b, c = math.floor(data[ele][1] - 10*i), math.floor(data[ele][2] - 10*(j-9))
                location[b, c] = 1
                Lmatrix[(i, j)] = location
            if not a[(i, j)]:
                Lmatrix[(i, j)] = np.zeros([10, 10])
    for i in range(36):
        for j in range(18):
            s, u, v = np.linalg.svd(Lmatrix[(i, j)])
            Lambda[(i, j)] = u

    return a, Lmatrix, Lambda


def given(map):
    location = np.zeros([10, 10], dtype=np.int32)
    for i in range(12):
        b, c = math.floor(map[i][0]/46.193)-1, math.floor(map[i][1]/49.509)-1
        location[b, c] = 1
        LmatrixMAP = location
    s, u, v = np.linalg.svd(LmatrixMAP)
    return u


def dotMax(Lambda, u):
    for i in range(36):
        for j in range(18):
            dot[(i, j)]=np.dot(u, Lambda[(i, j)])
    # print(dot)
    a = max(dot.values())
    return list(dot.keys())[list(dot.values()).index(a)]


data = scio.loadmat('Annex1 Simple catalog.mat')['star_data']
groups = group(data)
getNonezero(groups)
a, Lmatrix, Lambda = LocationMatrix(data)

Lambda[6, 10] = np.zeros([10, 1])
Lambda[8, 9] = np.zeros([10, 1])
Lambda[13, 4] = np.zeros([10, 1])


mapp = [[11.22,68.58],
[42.37,277.23],
[131.74,324.91],
[202.12,115.63],
[241.29,480.2],
[327.02,219.08],
[334.61,130.37],
[357.63,344.18],
[370.56,88.89],
[400.67,80.41],
[439.67,224.07],
[442.85,198.43]]





print(Lambda[8 ,9])
u = given(mapp)
dot = {}
print(u)
print(dotMax(Lambda, u))
print(a[11, 5])



