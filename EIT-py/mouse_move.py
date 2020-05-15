import numpy as np
from sklearn.linear_model import Ridge
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from scipy.optimize import minimize
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.tri import Triangulation
from matplotlib.patches import Polygon
np.set_printoptions(threshold=np.inf)
#读取数据
elems = np.loadtxt(r'D:\Proj\EIT\EIT-py\data\elems.csv', delimiter=",").astype(int)
nodes = np.loadtxt(r'D:\Proj\EIT\EIT-py\data\nodes.csv', delimiter=",")
J = np.loadtxt(r'D:\Proj\EIT\EIT-py\data\jacobian.csv', delimiter=",")
refedata = np.loadtxt(r'D:\Proj\EIT\EIT-py\data\refedata.csv', delimiter=",")
projdata = np.loadtxt(r'D:\Proj\EIT\EIT-py\data\projdata1.csv', delimiter=",")
z = projdata - refedata
#吉洪诺夫正则化求elem_data
clf1 = Ridge(alpha=0.001)
clf1.fit(J,z)
elem_data = clf1.coef_
elem_data = elem_data/np.max(np.abs(elem_data))
alphas = Normalize(0, 0.3, clip=True)(np.abs(elem_data))
elem_data = elem_data * alphas

match = np.loadtxt(r'D:\Proj\EIT\EIT-py\data\match.csv', delimiter=",").astype(int)
def motion_notify(event):
    if event.inaxes is None:
        tri = -1
    else:
        tri = trifinder(event.xdata, event.ydata)
    plt.title(np.around(elem_data[match[tri]], decimals=4))
    event.canvas.draw()

triang = Triangulation(nodes[:,0], nodes[:,1])
trifinder = triang.get_trifinder()
#成像
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1,aspect=1)
plt.triplot(triang,linewidth=0.6,color='black')
cmap = plt.cm.RdBu.reversed()
norm = matplotlib.colors.Normalize(vmin=-1, vmax=1)
for i in np.arange(576):
    xs = triang.x[elems[i] - 1]
    ys = triang.y[elems[i] - 1]
    polygon = Polygon(list(zip(xs, ys)), facecolor=cmap(norm(elem_data[i])))
    ax1.add_patch(polygon)
ax1.set_xticks([-1,1])
ax1.set_yticks([-1,1])
plt.axis('off')
fig.colorbar(matplotlib.cm.ScalarMappable(norm=norm, cmap="RdBu_r"), ax=ax1)

plt.gcf().canvas.mpl_connect('motion_notify_event', motion_notify)
plt.show()