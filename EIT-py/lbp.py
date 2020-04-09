import numpy as np
from scipy.interpolate import griddata
np.set_printoptions(threshold=np.inf)
def lbp_new(proj):
    """利用28个投影数据构成的投影阵proj进行反投影成像"""
    proj = np.hstack([proj[0:7],0,proj[7:13],0,0,proj[13:18],0,0,0,proj[18:22],0,0,0,0,proj[22:25],0,0,0,0,0,proj[25:27],0,0,0,0,0,0,proj[27],0,0,0,0,0,0,0])
    proj = proj.reshape(8,7)
    for i in range(7):
        for j in np.arange(0,i+1):
            proj[i+1,j] = proj[j,i]
    f = np.zeros((33, 33))
    grid_x, grid_y = np.mgrid[1:33:33j, 1:33:33j]
    s_list = [[16, 32], [27, 27], [32, 16], [27, 5], [16, 0], [5, 5], [0, 16], [5, 27]]
    p_list = [[16, 32], [27, 27], [32, 16], [27, 5], [16, 0], [5, 5], [0, 16], [5, 27]]
    i = 0
    j = 0
    for s in s_list:
        points = np.array([])
        values = np.array([])
        for p in p_list:
            if p == s:
                continue
            elif s[0] > p[0]:
                x = np.arange(p[0], s[0]+1)
                y = np.linspace(p[1], s[1], num=np.size(x), endpoint = True, retstep = False, dtype = None)
                y = np.rint(y).astype(int)
            else:
                x = np.arange(s[0], p[0]+1)
                y = np.linspace(s[1], p[1], num=np.size(x), endpoint=True, retstep=False, dtype=None)
                y = np.rint(y).astype(int)
            for n in np.arange(np.size(x)):
                points = np.append(points, ([x[n], y[n]]))
                values = np.append(values, proj[i,j])
            j = j + 1
            if j == 7: j = 0
        points = points.reshape(-1, 2)  # points重构为列为2的矩阵
        f = f + griddata(points, values, (grid_x, grid_y), method='linear', fill_value=0)
        i = i + 1
    return f/8
