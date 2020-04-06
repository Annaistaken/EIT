import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MyFigure(FigureCanvas):
    def __init__(self, width, height, dpi):
        index_ls = ['AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'CD', 'CE', 'CF',
                         'CG', 'CH', 'DE', 'DF', 'DG', 'DH', 'EF', 'EG', 'EH', 'FG', 'FH', 'GH']
        notate = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        theta = [2 * np.pi / 4, 1 * np.pi / 4, 0 * np.pi / 4, 7 * np.pi / 4, 6 * np.pi / 4, 5 * np.pi / 4,
                      4 * np.pi / 4, 3 * np.pi / 4]
        self.fig = plt.figure(figsize=(width, height), dpi=dpi)
        gs = GridSpec(2, 2)
        self.ax1 = self.fig.add_subplot(gs[0, :])
        plt.xticks(range(28), index_ls)
        plt.yticks([])
        self.ax2 = self.fig.add_subplot(gs[1, 0])
        plt.axis('off')
        self.ax3 = self.fig.add_subplot(gs[1, 1], projection='polar')
        for i in np.arange(8):
            plt.annotate(notate[i], xy=(theta[i], 1), xytext=(theta[i], 1.1), xycoords='data')
        plt.axis('off')
        super(MyFigure,self).__init__(self.fig)