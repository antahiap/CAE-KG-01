
import networkx as nx
import numpy as np
import pandas as pd
from sklearn.metrics import jaccard_score
from scipy.spatial import distance
import itertools
import statistics
from sklearn.decomposition import PCA
import random
from scipy.cluster.hierarchy import centroid
from sklearn.cluster import KMeans
from sklearn import svm
from fractions import Fraction


def assg1():
    # # final exam
    beta = 0.5  # 0.5
    M = np.array([
        [0, 1 / 2, 1 / 2, 0],
        [0, 0, 1 / 2, 1 / 2],
        [0, 0 , 0 , 1],
        [1, 0, 0, 0]
    ])    
    rt = np.array([1, 1, 1, 1])

    # M = np.array([
    #     [1 / 2, 1 / 2, 0],
    #     [1 / 2, 0, 0],
    #     [0, 1 / 2, 0]
    # ])
    # r = np.array([1 / 3, 1 / 3, 1 / 3])

    N = M.shape[0]
    A = beta * M + (1 - beta) / N * np.ones([N, N])
    cs = 1 
    rt = cs / N * np.ones([N, 1])
    print(rt)
    
    for i in range(0, 100):
        print(i, rt, rt.shape, A.shape)
        rt1 = np.dot(A, rt)
        rt = rt1
        input('enter to continue')
    return

    # q2
    M = np.array([
        [0, 0, 0],
        [1 / 2, 0, 0],
        [1 / 2, 1, 1],
    ])
    # sample
    # M = np.array([
    #     [0.5, 0.5, 0],
    #     [0.5, 0, 0],
    #     [0, 0.5, 1],
    # ])

    # q3 
    M = np.array([
        [0, 0, 1],
        [1 / 2, 0, 0],
        [1 / 2, 1, 0]
    ])

    beta = 1  # 0.85  # 0.7
    cs = 3
    N = M.shape[0]
    
    A = beta * M + (1 - beta) / N * np.ones([N, N])
    print(A)

    rt = cs / N * np.ones([N, 1])

    for i in range(0, 100):
        print(i, rt, rt.shape, A.shape)
        rt1 = np.dot(A, rt)
        rt = rt1
        input('enter to continue')
    a, b, c = rt
    print(a + b)
    print(a + c)
    print(b + c)
    print(a + b)


def assg2():

    Ns = 0.5
    Ms = 0.2

    for ri in range(1, 25):
        try:
            MN = ((1 - 0.5 ** ri) ** (24 / ri)) / (1 - (1 - 0.2 ** ri) ** (24 / ri))
            print(ri, MN)
        except:
            continue

    # from the interval pick the roof of the r

    # q3
    sh_1 = ks.shingleset_list("ABRACADABRA", [2])
    sh_2 = ks.shingleset_list("BRICABRAC", [2])

    union = list(set(sh_1) | set(sh_2))
    print(union, len(union))

    print(sh_1, len(sh_1))
    print(sh_2, len(sh_2))

    c = 0
    for i in sh_1:
        if i in sh_2:
            c += 1
            print (i, c)


def assg3():

    # q1
    u = [1, 0.25, 0, 0, 0.5, 0]
    v = [0.75, 0, 0, 0.2, 0.4, 0]
    w = [0, 0.1, 0.75, 0, 0, 1]

    # print('u,v:', np.dot(u, v) / np.linalg.norm(u) / np.linalg.norm(v)) 
    # print('u,w:', np.dot(u, w) / np.linalg.norm(u) / np.linalg.norm(w)) 
    # print('w,v:', np.dot(w, v) / np.linalg.norm(w) / np.linalg.norm(v)) 

    # q2

    meas = np.array([
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    ])

    # for i in itertools.combinations(range(0, len(meas)), 2):
    #     # print(i)
    #     print((1 - jaccard_score(meas[i[0]], meas[i[1]])) * 7)
    
    # q3
    for i in itertools.combinations(range(0, len(meas)), 2):
        u, v = meas[i[0]], meas[i[1]]
        # print(np.linalg.norm((u - v), ord=1))

    # q4
    meas = [
        'he', 'she', 'his', 'hers'
    ]

    for i in itertools.combinations(range(0, len(meas)), 2):
        u, v = meas[i[0]], meas[i[1]]
        print(editdistance.eval(u, v))


def assg5():

    # q1
    # N = 100,000; M = 100,000,000; S = 1,200,000,000 
    # N = 30,000; M = 200,000,000; S = 1,800,000,000 
    # for N, M in [
    #     [5e4, 40e6],  # [40000, 60e6],
    #     [30e3, 100e6],
    #     [30e3, 200e6],  # [10e3, 50e6],
    #     [100e3, 40e6]  # [100e3, 100e6]
    # ]:
    #     print('-----------------')
    #     print('tri:', (2 * N ** 2 + N) / 1e6)
    #     print('tab:', (M * 12 + N) / 1e6) 
    
    # q2
    '''
        The number of infrequent pairs per bucket on the first pass will be about P divided by the number of buckets.

        A pair can only be a candidate pair for the second pass if it is in a frequent bucket. For the values of P and S found in this question, that can only occur if the bucket contains one of the 1,000,000 frequent pairs.

        You must use a hash table to count candidate pairs on the second pass of PCY. This hash table takes 12 bytes per candidate pair.'''

    # S = 1,000,000,000; P = 10,000,000,000 
    # for s in [1e9, 200e6, 100e6]:
        # print((s - 250e3) / 12 - 1e6)
    # for p in [10e9, 400e6, 20e9, 120e6]:
    for p in [4e8, 2e8, 12e7, 16e8]:
        print((250e3 * 4 + (1e6 + p)) / 1e6)   

    # q4
    # {A,B,C,D,E,F,G,H}
    #  {A,B}, {A,C}, {A,D}, {B,C}, {E}, {F}. 
    # G,H


def assg6():

    A = np.array([
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    ])

    f = np.array([
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0],
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        ], dtype=float)
    # f = np.zeros([10, 3], dtype=float)
    for u, row in enumerate(A):
        s1 = np.zeros([1, 3])
        s2 = np.zeros([1, 3])
        s22 = np.zeros([1, 3])
        for v, a in enumerate(row):
            if a == 1:
                fuv_e = np.exp(-np.dot(f[u], f[v].T))
                s1 = s1 + f[v] * (fuv_e / (1 - fuv_e))
                s22 = s22 + f[v]
            
            s2 = s2 + f[v]
        d = (s1 - (s2 - f[u] - s22))[0]
        # print(f[u], s1)
        f[u, :] = (f[u] + (0.2 * d))
        # print(f[u])
        f[f < 0] = 0
        # print(f[u], s1)
        print(f)
        # break


def assg7():
    # q 
    s = 0
    e = []
    for j in range(1, 11):
        e.append(j)

    el = []
    for y in range(0, 7):
        el += e
        # print(el)
    el = el + [x for x in range(1, 6)]
    print(len(el))
    print(el)
    # el = ['a', 'b', 'c', 'b', 'd', 'a', 'c', 'd', 'a', 'b', 'd', 'c', 'a', 'a', 'b']

    for l, m, n in [
        # [14, 35, 42],
        # [37, 46, 55],
        # [25, 34, 47],
        # [3, 45, 72]
        [22, 42, 62],  # selected
        [31, 32, 44],
        [4, 31, 72],
        [14, 35, 42]
        # [3, 8, 13]
    ]:
        kl = el[l - 1]
        km = el[m - 1]
        kn = el[n - 1]
        print(kl, km, kn)

        cl = el[l - 1:].count(kl)
        cm = el[m - 1:].count(km)
        cn = el[n - 1:].count(kn)
        # print(cl, cm, cn)
        
        xx = [
            len(el) * (2 * cl - 1),
            len(el) * (2 * cm - 1),
            len(el) * (2 * cn - 1)]
        print(xx, statistics.median(xx))
        print(sum(xx) / len(xx))

    print(5 * 7 ** 2 + 5 * 8 ** 2)
        # break

    # q5 

    n = [ 1e11, 1e9, 1e14, 1e9]
    t = [999, 1000, 1, 999]

    n = [1e9, 1e13, 1e12, 1e14]
    t = [999, 99, 100, 0]

    for i in range(0, 4):
        print(
            (n[i] / 1e8 * 100 * (t[i] + 1) * 100) / 1e10
        )


def assg8():

 # q1

    '''
    Possible error: you normalized by rows, but did not normalize by columns.
    Possible error: You computed both the row and column averages first, and then subtracted both from each entry. You must compute row averages first and subtract the row average from each entry in that row. Then start with the new matrix to compute column averages and subtract those averages from the elements in the column.
    '''

    movies = np.asarray([
        [1, 2, 3, 4, 5],
        [2, 3, 2, 5, 3],
        [5, 5, 5, 3, 2]
    ])
    movie_r = []
    for r in movies:
        avg_r = sum(r) / len(r)
        movie_r.append(r - avg_r)
    movie_r = np.array(movie_r)
    # print(movie_r)

    # c_ave = []
    # for c0 in movies.T:
    #     c_ave.append(sum(c0) / len(c0))

    movie_c = []
    for i, c in enumerate(movie_r.T):
        # movie_c.append(c - c_ave[i])
        # print(len(c))
        avg_c = [sum(c) / len(c)]
        movie_c.append(c - avg_c)
    movie_c = np.array(movie_c)
    # print(movie_c.T * 3)
    # answer, There are more 1's than 0's.  - incorrect
            # The entry (A,Q) is -3.  - incorrect
            # The entry (B,M) is -1/3. 

 # q2
    alpha = [0, 0.5, 1, 2]
    for a in alpha:
        items0 = np.asarray([
            [1, 0, 1, 0, 1, 2 * a],
            [1, 1, 0, 0, 1, 6 * a],
            [0, 1, 0, 1, 0, 2 * a]
        ])
        items = items0 - items0.mean(axis=1, keepdims=True)
        print('------------------')
        print(a)
        items[:, -1] = items[:, -1] * a
        for ri, rj in itertools.combinations(range(0, len(items)), 2):
            theta = np.dot(items[ri], items[rj]) / np.linalg.norm(items[ri]) / np.linalg.norm(items[rj])
            print(ri, rj, theta)
    return
    # False: For α = 2, A is closer to C than B is. 
    # False: For α = 0.5, B is closer to C than A is.  - incorrect

 # q3
    '''
    Incorrect: Hint: start by replacing 3,4, and 5 by 1 and 1, 2, and blank by 0. Each column is a set -- those rows in which it has a 1. For example, column b is the set {A,B} and column g is {A,C}. Next, compute the Jaccard distance between each pair of columns. For example, the Jaccard distance between b and g is 1 minus the Jaccard simlarity of {A,B} and {A,C}. The similarity is 1/3, because the size of the intersection is 1 and the size of the union is 3. Start the clustering by merging the pair of items with the smallest distance (greatest similarity).
    '''
    u_matrix = np.asarray([
        [4, 5, 0, 5, 1, 0, 3, 2],
        [0, 3, 4, 3, 1, 2, 1, 0],
        [2, 0, 1, 3, 0, 4, 5, 3]
    ])

    u_matrix[np.where(u_matrix < 3)] = 0
    u_matrix[np.where(u_matrix >= 3)] = 1
    
    jsim = []
    pair = []
    items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    for r in itertools.combinations(range(0, u_matrix.shape[1]), 2):
        ri, rj = r
        jsim.append(distance.jaccard(
            u_matrix[:, ri],
            u_matrix[:, rj]
        ))
        pair.append(r)
    
    jsim = np.array(jsim)
    pair = np.array(pair)
    
    cs = items
    cls0 = items
    sim_min = [1 for x in range(0, len(items))]
    while len(cls0) > 4:
        ids = np.argmin(jsim)
        pm = pair[ids]
        print(np.argmin(jsim), pm)

        cs[pm[0]] = cs[pm[0]] + cs[pm[1]]
        cs[pm[1]] = ''
        sim_min[pm[0]] = min(jsim[ids], sim_min[pm[0]], sim_min[pm[1]])
        # print(i, p)
        print(cs, sim_min)

        cls0 = [x for x in cs if x != '']
        jsim[ids] = 20
        # print(jsim)
        print(cls0)

    # {a,b,d,g} 

    # q4


def assg10():

# q1
    # answer 4, 64
            # 36, 100
    points = np.asarray([x ** 2 for x in range(1, 11)])
    k = 2
    diff = 2
    # print(points.shape)
    for i, p in enumerate(points):
        if i + 1 == points.shape[0]:
            break
        sen0 = points[:i + 1]
        sen1 = points[i + 1:]
        print(sen0, sen1)

        cen0 = sum(sen0) / len(sen0)
        cen1 = sum(sen1) / len(sen1)
        # print(cen0, cen1)

        dists = np.asarray([
            abs(cen0 - points),
            abs(cen1 - points)])
        print(np.argmin(dists, axis=0))
        print('--------------------------')
   
    # return

    # points = np.asarray([x ** 2 for x in range(1, 11)]).reshape(-1, 1)
    # kmeans = KMeans(n_clusters=2, init='random', n_init=10, algorithm='auto').fit(points)
    # print(points[np.where(1 == kmeans.labels_)])
    # print(points[np.where(0 == kmeans.labels_)])
    # print(kmeans.cluster_centers_)

    # for cp in points:
    #     points = [x ** 2 for x in range(1, 11)]
    #     points.remove(cp)
    #     c2 = [np.mean(np.asarray(points))][0]
    #     c2i = np.argmin(np.abs(np.asarray(points) - c2))
    #     clus = [[cp, cp], [points[c2i]] + points ]
    #     points = [x ** 2 for x in range(1, 11)]
    
    #     # print(clus)

    #     diff = 2        
    #     centroid = np.asarray(
    #             [clus[0][0], clus[1][0]])
    #     # print(cp)

    #     while diff > 0.0001:
    #         # points = [x ** 2 for x in range(1, 11)]

    #         # clus = [[] for ki in range(0, k)]

    #         # for ki in range(0, k):
    #         # #     # i = random.choice(points)
    #         #     i = centroid[ki]
    #         #     # points.remove(i)
    #         #     # clus[ki].append(i)
    #         #     clus[ki].append(i)

    #         points = np.asarray(points)
    #         while points.shape[0] > 0:
    #             for ki in range(0, k):
    #                 dist = (points - clus[ki][0]) ** 2
    #                 pi = np.argmin(dist)

    #                 clus[ki].append(points[pi])

    #                 # if len(clus[ki]) > 2:
    #                 #     # print(clus[ki])
    #                 #     cki0 = (clus[ki][0] + points[pi]) / (len(clus[ki]) - 1)
    #                 #     cki = np.argmin(np.asarray(clus[ki][1:]) - cki0) + 1
    #                 #     # print(cki, clus[ki], cki0)
    #                 #     clus[ki][0] = clus[ki][cki]
    #                 #     # input('wait')
    #                 # else:
    #                 #     print(clus)
    #                 points = np.delete(points, pi)
    #                 # print(points)
    #                 # print(clus)

    #         centroid_old = centroid
    #         centroid = np.asarray(
    #             [clus[0][0], clus[1][0]])
    #         diff = sum((centroid - centroid_old) ** 2)
    #         diff = 0
    #         # print(diff)
    #         # input('wait')
    #     # print(clus)
    #     # print('------------------------')
    #     # input('wait')

# q2
    # answer, q2 51, 18
    #         q4 57, 5
    # anwer, q2 61, 8
            # q4 53, 15
    c = np.asarray([
        [0 , 0], [100, 40]
    ])

    test_points = np.asarray([
        # [50, 18],
        # [51, 18],
        # [66, 5],
        # [56, 15],
        # [56, 15],
        # [54, 8],
        # [61, 8],
        # [52, 13],
        [55, 5],
        [53, 10],
        [53, 18],
        [56, 13],
    ]) 
    test_points = np.asarray([
    # #     [57, 5],
    # #     [61, 10],
    # #     [53, 10],
    # #     [50, 18],
    #     [53, 15],
    #     [58, 13],
    #     [54, 8],
    #     [50, 18],
        [61, 10],
        [55, 5],
        [53, 15],
        [56, 15],
    ]) 

    for p in test_points:
        n20 = np.linalg.norm((c[0] - p), ord=2)
        n10 = np.linalg.norm((c[0] - p), ord=1)
        
        n21 = np.linalg.norm((c[1] - p), ord=2)
        n11 = np.linalg.norm((c[1] - p), ord=1)

        print(n10 < n11, n20 > n21)
        print(p)

# q3
    # answer manual, 12.5 wrong
    # answer, 42.5
    '''
    Incorrect: Suggestions:

    - Remember that initially, each point is in a cluster by itself.
    - Keep a list of the centroids after each merge step.
    - Pick the closest centroids to merge.
    - When merging, remember to weight each centroid by the number of points in its current cluster.
    '''

    p3 = np.asarray(
        [1, 4, 9, 16, 25, 36, 49, 64], dtype=float
    )
    clus = [[1], [4], [9], [16], [25], [36], [49], [64]]
    
    # clus = np.asarray(range(0, len(p3)))
    cen = np.asarray(
        [1, 4, 9, 16, 25, 36, 49, 64], dtype=float
    )
    
    while len(cen) > 2:
        diff = []
        for i in range(0, len(cen) - 1):
            diff.append(abs(cen[i] - cen[i + 1]))
        
        diff = np.asarray(diff)
        id0 = np.argmin(diff)
        # print(id0)
        # print(diff)
        clus[id0] += clus[id0 + 1]
        clus.pop(id0 + 1)
        # print(clus)

        cids = clus[id0]
        cen[id0] = sum(cids) / len(cids)
        cen = np.delete(cen, [id0 + 1])
    
        # print(cen)
        # print('-------------------')

# q5
    '''
    wrong answer: The probability that both A and C are correct is 8% 
    Incorrect: Hint: we can assign each of x, y, and z to A, B, or C in 27 possible ways. However, we can organize them into a small number of groups of assignments that "look" the same and have the same probability. For example, one group is the assignment where one of x, y, and z goes into B and the other two go into the same one of A and C. Analyze each of these groups to see if A and/or C is "correct."
    '''
    # points5 = np.asarray([
    #     [0, 0], [10, 10]
    # ])
    # from scipy.cluster.hierarchy import dendrogram, linkage
    # from matplotlib import pyplot as plt

    # linked = linkage(X, 'single')

    # labelList = range(1, 11)

    # plt.figure(figsize=(10, 7))
    # dendrogram(linked,
    #             orientation='top',
    #             labels=labelList,
    #             distance_sort='descending',
    #             show_leaf_counts=True)
    # plt.show()


def assg11():
    # q1
    '''
    yyxx
    '''

    # q2
    '''
    AB, BC, CD, DE, EF, FG, GH, AH, ADG, ADF 
    ABCDEFGH
    
    dumb = 7
    AB,BC,CD, DE,EF,FG,GH 7

    # simple
    AB,BC,CD, DE,EF,FG,GH 7

    # Largest first
    ADG, ADF, AB, BC, DE, GH, 6

    # Most help
    ADG, BC, EF, GH 4
    '''
    d = 7
    s = 7
    l = 6
    m = 4
    print([x / m for x in [d, s, l]])

    # q3
    '''
    a0-b0   a1-b1
    a1-b2   a2-b3
    a2-b4   a2-b0
    a3-b1   a3-b2
    a4-b3   a4-b4

    a3-b2 and a4-b4
    a4-b3 and a3-b1
    '''

    # q4
    def getitems(ctrb0, ctrb):
        c1 = np.max(ctrb[0, :])
        c10 = np.where(ctrb0[0, :] == c1)[0][0]
        c1 = np.where(ctrb[0, :] == c1)[0][0]

        ctrb23 = np.delete(ctrb, c1, 1) 
        c2 = np.max(ctrb23[1, :])
        c20 = np.where(ctrb0[1, :] == c2)[0][0]
        c2 = np.where(ctrb[1, :] == c2)[0][0]

        ctrb3 = np.delete(ctrb23, c2, 1) 
        c3 = np.max(ctrb3[2, :])
        c30 = np.where(ctrb0[2, :] == c3)[0][0]

        sel = [c10, c20, c30]

        return(sel)

    name = ['A', 'B', 'C', 'D', 'E']
    B = np.array([1.0, 2.0, 3.0, 4.0, 5.0])

    check = True
    ctr = np.array([
       [0.015, 0.016, 0.017, 0.018, 0.019],
       [0.010, 0.012, 0.014, 0.015, 0.016],
       [0.005, 0.006, 0.007, 0.008, 0.010]
    ])
    bid = np.array([0.10, 0.09, 0.08, 0.07, 0.06])

    ctrb0 = ctr * bid
    ctrb = ctrb0
    print(ctrb0)

    sel = getitems(ctrb0, ctrb)
    count = np.array([0 for x in name])
    b0 = np.array([0.0 for x in name])
    count_old = np.zeros_like(count)
    b0_old = np.zeros_like(b0)
    rml = []
    while check:
        count_old[:] = count[:]
        b0_old[:] = b0[:]
        for i, s in enumerate(sel):
            b0[s] = b0[s] + bid[s]  # ctr[i, s]
            count[s] = count[s] + 1

        cc1 = np.where(count > 101)[0]
        cc2 = np.where(b0 > B)[0]
        if cc1.size > 0:
            rml.append(cc1[0])
            count[:] = count_old[:]
            b0[:] = b0_old[:]
        if cc2.size > 0:
            rml.append(cc2[0])
            count[:] = count_old[:]
            b0[:] = b0_old[:]
            i = sel.index(cc2)
            tc = count[cc2] / ctr[i, cc2]
            c = [int(tc * ctr[i, s]) for i, s in enumerate(sel)]
            print(c)
            count[sel] = c
            print(count)
            
            input('wait')
        if ctrb.shape[1] > len(rml):
            ctrb = np.delete(ctrb0, rml, 1) 
            sel = getitems(ctrb0, ctrb)
            print(sel)

        else:
            check = False
        # check = False
    print(count)


def assg12():
    # q5  (3.9, 4.3) Incorrect: This point is closer to the negative point (3,3) than to either of the positive points.
    # answer (4.2, 1.9) 

    point = np.asarray([
        [1, 4], [3, 3], [3, 1],
        [3, 6], [5, 3]
    ])
    sign = [-1, -1, -1, 1, 1]

    check = np.asarray([
        [4.2, 1.9], [2.2, 4.7], [3.9, 4.1], [3.6, 4.1] 
    ])
    check = np.asarray([
        [2.6, 4.4],
        [4.3, 1.6],
        [4.1, 4.1],
        [2.2, 4.7]
    ])

    check = [
        [2.6, 4.4],
        [3.9, 4.3],
        [4.1, 4.1],
        [3.6, 4.1]
    ]

    for c in check:
        dif = point - c
        dist = np.linalg.norm(dif, axis=1)
        print(sign[np.argmin(dist)])
    # q4 
    # answer:  The attribute A1 gives a better split than the attribute, A3. 
    '''Incorrect: In the case of binary classification, the Gini Index can be calculated as one minus the sum of the squares of probability of positive examples and negative examples, independently in a subset of training examples.

    For example, there are 5 positive and 3 negative examples in the training set of 8 examples. Accordingly, the p(+) is 5/8 and the p(-)is 3/8; the impurity of the given set of training examples as a whole is thus computed as 1 - 34/64 = 15/32.

    In order to estimate the goodness of a particular attribute, the training examples are grouped into partitions based on the distinct values of the attribute; the impurity of these partitions is then estimated separately. The weighted sum of impurities of these partitions indicates the degree of impurity still present even after applying the attribute for classification. Finally, the goodness of the attribute for a split is the difference between the impurities before and after applying the attribute for partitioning the training set.

    After computing the goodness of attributes A1 and A3, you can see that attribute A1 does not give a better split than attribute A3.'''

    # answer, A1 doesn't provide the best

    # q3
        # [55, 118] wrong, check the classifies

    data = [
        [55, 118], [38, 115],
        [33, 22], [43, 83]
    ]
    data = [
        [64, 37], [44, 105],
        [55, 118], [50, 30]
    ]
    data = [
        [50, 90], [42, 57],
        [43, 83], [55, 20]
    ]
    data = [
        [64, 37],
        [29, 97],
        [55, 63],
        [25, 125],
    ]
    for d in data:
        a = d[0]
        s = d[1]
        if a < 45:
            if s < 110:
                print(d, 'not buy')
            else:
                print(d, 'buy')
        else:
            if s < 75:
                print(d, 'not buy')
            else:
                print(d, 'buy')
    # q2
    # pos line y=-x/3 + 17/3  -move to (7,2)--> y=-x/3 + 13/3   --mean the c--> 10      line: y+x/3-5       scale:2/3 the line
    # neg line y=-x/4 + 15/4  -move to (8,3)--> y=-x/4 + 5      --mean the c--> 35/8    line: y+x/4-35/8    sclae:8/5
    pts = [
        [5, 4], [8, 3],
        [3, 3]   , [7, 2]
    ]
    y = [1, 1, -1, -1]

    for p in pts:
        print((p[1] * 3 / 2 + (p[0] / 2) - 15 / 2))
    for p in pts:
        print((p[1] * 8 / 5 + p[0] * 2 / 5 - 7))
        # print(p[1] + p[0]/3 -5)

    '''
    Incorrect: You may have the correct method, but have forgotten to scale the vector w so that the value of w.x+b is exactly +1 for the closest positive point and exactly -1 for the closest negative point. Here is an outline of how to work this problem.

    Start by finding the lines through the two positive points and through the two negative points. Put these lines in slope-intercept form. That is, if v is the vertical axis and u the horizontal axis, write the equation of the line as v=c+au.
    Find the parallel line through the closer of the points on the other side. Remember that parallel lines have the same slope; only the intercept c can change.
    Having found the proper parallel line, find the line midway between them by averaging their intercepts --- the c values.
    Now, write the equation of this line as w.x+b=0.
    Scale the constants w=(w1,w2) and b, so that for positive x, the left side w.x+b is at least 1, but is exactly 1 for the closest (to the boundary) of the positive points. Also, the left side must be at most -1 for negative points, but must be exactly -1 for the closest of them.'''

    print('-------------')
    print('q1')
    
    a = [-1 / 3, -3 / 5, -7 / 8, -1 / 4]
    b = [6, 6, 7, 4]

    a = [-7 / 8, -4 / 9, -3 / 4, -1 / 4]
    b = [7, 5, 8, 4]

    a = [-4 / 9, -2 / 5, -3 / 10, -7 / 8]
    b = [5, 5 , 4, 7]

    a = [-1 / 3, -3 / 4, -1 / 4, -2 / 9]
    b = [6, 8, 4, 5]

    for i in range(0, 4):
        # err = (
        #     (7 * a + b - 2) ** 2 + 
        #     (8 * a + b - 3) ** 2 + 
        #     (3 * a + b - 3) ** 2 + 
        #     (5 * a + b - 4) ** 2)
        
        # da = (
        #     (7 * a + b - 2) * 2 * 7 + 
        #     (8 * a + b - 3) * 2 * 8 + 
        #     (3 * a + b - 3) * 2 * 3 + 
        #     (5 * a + b - 4) * 2 * 5)

        # db = (
        #     (7 * a + b - 2) * 2 + 
        #     (8 * a + b - 3) * 2 + 
        #     (3 * a + b - 3) * 2 + 
        #     (5 * a + b - 4) * 2)

        err = (
            (7 * a[i] + b[i] - 2) ** 2 + 
            (8 * a[i] + b[i] - 3) ** 2 + 
            (3 * a[i] + b[i] - 3) ** 2 + 
            (5 * a[i] + b[i] - 4) ** 2)

        # a = a + da
        # b = b + db

        print(err)
        # print(a, b)


def assg13():
    # q1
    ''' (3,9) '''
    m = np.asarray([
        [1, 	2, 	3, 	4],
        [5, 	6, 	7, 	8],
        [9, 	10, 	11, 	12],
        [13, 	14, 	15, 	16],
    ])
    v = np.asarray([1, 2, 3, 4])
    print(m * v)

    # q2
    '''(2, [(R,1), (S,3)]) '''

    # q3
    ''''The output of the second Map function has x+z different keys. > wrong
    Incorrect: Hint: The input to the second Map function consists of pairs. The first component, j, of each pair, is a column number of M and a row number of N. On the list forming the second component of this pair is one element giving the product mijnjk, along with the values of i and k. The job of the second Map function is to turn each of these elements into one key-value pair whose key is (i,k) and whose value is mijnjk.

    The output of the first Reduce function has pairs with lists of length 1.
    

    '''

    # q4
    '''The output of the Map function has 2y pairs with each key. > right
    The input to the Reduce function has pairs with lists of length 2(x+z).  >wrong
        The keys that are output from Map, and therefore are input to Reduce, correspond to a row of M and a column of N.
        The elements associated with a given key (i,k) are all the elements of the i-th row of M and all the elements of the k-th column of N.
    '''


def assg15():
    # final exam
    h = [1, 1, 1, 1]
    A = np.array([
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ])    

    for i in range(0, 10):
        print(i)
        a = np.dot(A.T, h)
        # a = a / np.max(a)

        h = np.dot(A, a)
        # h = h / np.max(h)
    
        print(a)
        print(h)
        print('-------------')
    
    return

    # q1, N = 1 billion, k = 2, x = 0.75, 107GB
    n = 1e9
    print(n)
    k = 2
    x = 0.75
    print(
        (n * 23 * (1 + (1 - x) / k) + (k + 1) * n) * 4e-9 
        # (20 * n * 4 * +(1 - x) / 2 * n + (k + 1) * n) * 10e-9
        )
    return

    # q4, c = 0.46 
    '''
    H ere is an outline of the solution. Use w as the PageRank of each second-tier page and z as the PageRank of each supporting page. You can write three equations, one for y in terms of z, one for w in terms of y, and one for z in terms of w. For example, y equals x (the PageRank from outside) plus all the untaxed PageRank of each of the m supporting pages (a total of βzm), plus its share of the tax (which is (1-β)/n). Discover the equations for w and z, then substitute these in the equation for y to get an equation for y in terms of itself, from which you can solve for y.
    '''
    print(0.85 / (1 + 0.85))
    # return

    # q3, λμ = 1.618
    '''
    [x y] = lam * mu *L*L.T [x, y]
    This equation can be expanded into two scalar equations involving x and y, with coefficients that involve λμ. Rewrite each equation to have y alone on one side, and a multiple of x (involving λμ) on the other side. The two multiples must be the same, which lets you solve for λμ. With that, you can get the ratio of x to y.
    '''
    
    A = np.array([
        [1, 1],
        [0, 1]
    ])

    h = [1 , 1]

    print(0.381 / (1 - 2 * 381))
    # return

    for i in range(0, 10):
        print(i)
        a = np.dot(A.T, h)
        a = a / np.max(a)

        h = np.dot(A, a)
        h = h / np.max(h)
    
        print(a)
        print(h)
        print('-------------')
    
    # return

    # q2, The final estimate of the authority of 4 is 1/5. 
    A = np.asarray([
        [0, 1, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ])

    h = [1, 1, 1, 1]
    a = np.dot(A.T , h) 
    a = a / np.max(a)

    h = np.dot(A, a)
    h = h / np.max(h)

    a = np.dot(A.T , h) 
    a = a / np.max(a)

    h = np.dot(A, a)
    h = h / np.max(h)

    print(h)
    print(a)


def gradientDescent(x, y, theta, alpha, m, numIterations):
    xTrans = x.transpose()
    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        # avg cost per example (the 2 in 2*m doesn't really matter here.
        # But to be consistent with the gradient, I include it)
        cost = np.sum(loss ** 2) / (2 * m)
        print("Iteration %d | Cost: %f" % (i, cost))
        # avg gradient per example
        gradient = np.dot(xTrans, loss) / m
        # update
        theta = theta - alpha * gradient
    return theta


def genData(numPoints, bias, variance):
    import random
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)
    # basically a straight line
    for i in range(0, numPoints):
        # bias feature
        x[i][0] = 1
        x[i][1] = i
        # our target variable
        y[i] = (i + bias) + random.uniform(0, 1) * variance
    return x, y


def assg9():
    #  final 
    M = np.array([
        [1, 2],
        [3, 4],
        [5, 6]
    ])
    f = np.sum(M ** 2)
    print(np.sum(M ** 2, axis=0) / f)

    print(1 + 4 + 9 + 16 + 25 + 36)
    return

    # q4
    M = np.asarray([
        [1, 1],
        [2, 2],
        [3, 4]
    ])
    # print(np.matmul(M.T, M))

    # q5
    M = np.asarray([
        [1, 2 , 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ])

    f = np.sum(M ** 2)
    print(np.sum(M ** 2, axis=0) / f)
    print(np.sum(M ** 2, axis=1) / f)
    for r in M:
        print(r)


def PCA_itr():
    sig = np.cov(M)
    w, v = np.linalg.eig(sig)
    print(w)
    print(v)
    print(np.matmul(w, v))
    # gen 100 points with a bias of 25 and 10 variance as a bit of noise
    x = np.asarray([
        [1, 1],
        [2, 2],
        [3, 3]
    ])
    y = np.asarray([1, 2, 4])
    # print(x, y)
    # x, y = genData(100, 25, 10)
    m, n = np.shape(x)

    # print(x, y)

    print(m, n)
    numIterations = 100000
    alpha = 0.0005
    theta = np.ones(n)
    theta = gradientDescent(x, y, theta, alpha, m, numIterations)
    print(theta)


if __name__ == '__main__':

    # assg1()
    # assg2()
    # assg3()
    # assg5()
    # assg6()
    # assg7()
    # assg8()
    assg9()
    # assg10()
    # assg11()
    # assg12()
    # assg13()
    # assg15()
