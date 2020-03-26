import numpy as np
from scipy import interpolate
from scipy.interpolate import griddata

import matplotlib
import matplotlib.pyplot as plt

def lbp(proj):
    """利用28个投影数据构成的投影阵proj进行反投影成像"""
    f = []
    i = 0
    j = 0
    for n in np.arange(8):
        f.append(np.zeros((35, 35)))
    s_list = [[0, 17], [12, 12], [17, 0], [12, -12], [0, -17], [-12, -12], [-17, 0], [-12, 12]]
    p_list = [[0, 17], [12, 12], [17, 0], [12, -12], [0, -17], [-12, -12], [-17, 0], [-12, 12]]
    for s in s_list:
        for p in p_list:
            if p == s:
                continue
            else:
                if p[0] == s[0]:
                    for y in np.arange(-abs(s[1]) + 17, abs(s[1]) + 18):
                        f[i][s[0] + 17, y] = proj[i, j]
                else:
                    # z = lagrange(s, p)#拉格朗日插值
                    z = interpolate.interp1d([s[0], p[0]], [s[1], p[1]], kind='linear')
                    if s[0] > p[0]:
                        x = np.arange(p[0], s[0]+1)
                    else:
                        x = np.arange(s[0], p[0]+1)
                    y = np.rint(z(x))
                    y = y.astype(int)
                    x = [x0 + 17 for x0 in x]
                    y = [y0 + 17 for y0 in y]
                    f[i][x, y] = proj[i, j]
                j = j + 1
                if j == 7:j=0
        """f[i]插值"""
        try:
            points = np.array([])
            values = np.array([])
            for x in np.arange(35):
                for y in np.arange(35):
                    if f[i][x, y] != 0:
                        points = np.append(points, ([x, y]))
                        values = np.append(values, f[i][x, y])
            points = points.reshape(-1, 2)  # points重构为列为2的矩阵
            grid_x, grid_y = np.mgrid[1:35:35j, 1:35:35j]
            f[i] = griddata(points, values, (grid_x, grid_y), method='linear',fill_value = 0)
        except:
            pass
        """f[i]插值结束"""
        i = i + 1
    f_sum = np.zeros((35, 35))
    for f0 in f:
        f_sum = f_sum + f0
    #f_ave = f_sum / 8
    return f_sum
