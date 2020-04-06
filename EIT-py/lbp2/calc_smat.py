import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.path import Path
"""
def cmp(aa,bb):
    if aa<bb:
        return 1
    else:
        return -1
xx, yy = np.meshgrid(np.arange(-16,17), np.arange(-16,17))
xxx, yyy = xx.flatten(), yy.flatten()
xy = np.vstack((xxx,yyy)).T
S = [np.zeros((33, 33)) for i in range(8)]
a=16
s = [np.pi/2, np.pi/4, 0, -np.pi/4, -np.pi/2, -3*np.pi/4, np.pi, 3*np.pi/4]
delta = [0, 3*np.pi/8, 5*np.pi/8, 7*np.pi/8, 9*np.pi/8, 11*np.pi/8, 13*np.pi/8, 15*np.pi/8]
for n in np.arange(0, 8):
    xc = [0 for i in range(7)]
    yc = [0 for i in range(7)]
    xline1 = [0 for i in range(7)]
    yline1 = [0 for i in range(7)]
    xline2 = [0 for i in range(7)]
    yline2 = [0 for i in range(7)]
    xf = [0 for i in range(7)]
    yf = [0 for i in range(7)]
    for i in np.arange(0, 7):
        theta = np.arange(s[n] - delta[i], s[n] - delta[i + 1], -0.1)  # 7段弧长的角度分布
        xc[i] = a * np.cos(theta)  # 7段弧长的坐标分布
        yc[i] = a * np.sin(theta)
        xline1[i] = np.arange(xc[0][0], xc[i][0], 0.1 * cmp(xc[0][0], xc[i][0]))
        if cmp(xc[0][0], xc[i][0]) == 1:
            yline1[i] = np.interp(xline1[i], [xc[0][0], xc[i][0]], [yc[0][0], yc[i][0]])
        else:
            yline1[i] = np.interp(xline1[i], [xc[i][0], xc[0][0]], [yc[i][0], yc[0][0]])
        xline2[i] = np.arange(xc[0][0], xc[i][-1], 0.1 * cmp(xc[0][0], xc[i][-1]))
        if cmp(xc[0][0], xc[i][-1]) == 1:
            yline2[i] = np.interp(xline2[i], [xc[0][0], xc[i][-1]], [yc[0][0], yc[i][-1]])
        else:
            yline2[i] = np.interp(xline2[i], [xc[i][-1], xc[0][0]], [yc[i][-1], yc[0][0]])
        xf[i] = [nx for nx in np.concatenate((xline1[i], xc[i], xline2[i][::-1])) if nx != '']
        yf[i] = [ny for ny in np.concatenate((yline1[i], yc[i], yline2[i][::-1])) if ny != '']
        #p1 = plt.fill(xf[i], yf[i])
        xycrop = np.vstack((xf[i], yf[i])).T
        pth = Path(xycrop,closed=False)
        mask = pth.contains_points(xy)
        mask = mask.reshape((33,33))
        mask = np.flip(mask,0)
        mask = mask.astype('int')
        mask[mask==1] = i+1
        S[n] = S[n] + mask
    #colors = ['white', 'red', 'orange', 'yellow', 'green', 'purple', 'pink', 'blue']
    #bounds = [0, 1, 2, 3, 4, 5, 6, 7]
    #cmap = matplotlib.colors.ListedColormap(colors)
    #norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
    #plt.imshow(S[n], interpolation='none', cmap=cmap, norm=norm)
    #plt.show()
#保存S矩阵
#np.savetxt("s.txt",S) #缺省按照'%.18e'格式保存数据，以空格分隔
#np.loadtxt("s.txt")
np.savez("smat.npz",S0=S[0],S1=S[1],S2=S[2],S3=S[3],S4=S[4],S5=S[5],S6=S[6],S7=S[7])
"""
#投影并成像
proj = np.mat([[0, 0, 246, 1024, 246, 0, 0],
               [0, 0, 246, 1024, 246, 0, 0],
               [0, 0, 246, 1024, 246, 0, 0],
               [0, 0, 246, 1024, 246, 0, 0],
               [0, 0, 246, 1024, 246, 0, 0],
               [0, 0, 246, 1024, 246, 0, 0],
               [0, 0, 246, 1024, 246, 0, 0],
               [0, 0, 246, 1024, 246, 0, 0]])
backproj = np.zeros((33, 33))
S = [np.zeros((33, 33)) for i in range(8)]
D=np.load("smat.npz")
S[0] = D['S0']
S[1] = D['S1']
S[2] = D['S2']
S[3] = D['S3']
S[4] = D['S4']
S[5] = D['S5']
S[6] = D['S6']
S[7] = D['S7']
for i in range(8):
    for j in range(7):
        S[i][S[i] == j + 1] = proj[i, j]
    backproj = backproj + S[i]
plt.imshow(backproj, interpolation='none', cmap=matplotlib.cm.RdBu)
plt.show()


"""不用GUI的简易成像方法
img = lbp(proj)
#绘制热图
imgshow = plt.imshow(img.T, extent=(0, 35, 0, 35), cmap=matplotlib.cm.RdBu, origin='lower')
plt.ion()

while True:
    img = lbp(proj)
    imgshow.set_data(img.T)
    plt.pause(0.1)

plt.ioff()
plt.show()
"""