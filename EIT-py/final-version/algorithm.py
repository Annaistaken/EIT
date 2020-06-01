import numpy as np
from scipy.optimize import minimize
from sklearn.linear_model import Ridge

# 反投影矩阵
lbp_B = np.loadtxt(r'D:\Proj\EIT\EIT-py\data\lbp_B_python.csv', delimiter=",")

# 灵敏度矩阵
S = np.loadtxt(r'D:\Proj\EIT\EIT-py\data\jacobian_python.csv', delimiter=",")
inv_S = np.linalg.pinv(S)

# 灵敏度归一化——A矩阵
W = np.zeros((576, 576))
S2 = ((S ** 2).sum(axis=0)) ** (-0.5)
row,col = np.diag_indices(W.shape[0])
W[row,col] = S2
A = np.dot(W, np.linalg.pinv(np.dot(S, W)))

#迭代计算的初始值
x0 = np.zeros(576)

def lbp(proj_d):
    """线性反投影算法"""
    #将28个边界值补全(8*7)
    proj56 = np.hstack([proj_d[0:7],
                        proj_d[7:13], proj_d[0],
                        proj_d[13:18], proj_d[1], proj_d[7],
                        proj_d[18:22], proj_d[2], proj_d[8], proj_d[13],
                        proj_d[22:25], proj_d[3], proj_d[9], proj_d[14], proj_d[18],
                        proj_d[25:27], proj_d[4], proj_d[10], proj_d[15], proj_d[19], proj_d[22],
                        proj_d[27], proj_d[5], proj_d[11], proj_d[16], proj_d[20], proj_d[23], proj_d[25],
                        proj_d[6], proj_d[12], proj_d[17], proj_d[21], proj_d[24], proj_d[26], proj_d[27]])
    elem_data = np.dot(lbp_B, proj56)  #通过提前计算好的反投影矩阵lbp_B来重建图像
    return elem_data

def svd(proj_d):
    """灵敏度矩阵法（求伪逆）"""
    elem_data = np.dot(inv_S, proj_d)  #提前计算灵敏度矩阵的伪逆
    return elem_data

def norm_sens(proj_d):
    """灵敏度矩阵归一化"""
    elem_data = np.dot(A, proj_d)  #提前计算A矩阵
    return elem_data

def cg(proj_d):
    """共轭梯度法"""
    paraList = [proj_d]  #将边界值proj_d作为额外参数传入
    elem = minimize(fun, x0, args=(paraList,), method='CG', jac=jac, options={'disp': False})
    return elem.x

def bfgs(proj_d):
    """BFGS拟牛顿法"""
    paraList = [proj_d]
    elem = minimize(fun, x0, args=(paraList,), method='BFGS', jac=jac, options={'disp': False})
    return elem.x

def slsqp(proj_d):
    """序列最小二乘算法"""
    paraList = [proj_d]
    elem = minimize(fun, x0, args=(paraList,), method='SLSQP', jac=jac, options={'disp': False})
    return elem.x

def lanczos(proj_d):
    """krylov子空间迭代法"""
    paraList = [proj_d]
    elem = minimize(fun, x0, args=(paraList,), method='trust-krylov', jac=jac, hess=hes, options={'disp': False})
    return elem.x

def tikhonov(proj_d):
    """Tikhonov正则化"""
    clf = Ridge(alpha=0.001)  #建立回归模型，正则化项系数为0.001
    clf.fit(S, proj_d)
    return clf.coef_

def fun(x, arg):
    """最小二乘目标函数"""
    para = list(arg)
    min = 0.5 * np.dot((np.dot(S, x) - para[0]).T, np.dot(S, x) - para[0])
    return min

def jac(x, arg):
    """目标函数一阶导——雅克比矩阵"""
    para = list(arg)
    return np.dot(S.T, np.dot(S, x) - para[0])

def hes(x, arg):
    """目标函数二阶导——海森矩阵"""
    return np.dot(S.T, S)

