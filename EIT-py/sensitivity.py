import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from matplotlib.colors import Normalize
from matplotlib.tri import Triangulation
from matplotlib.patches import Polygon
from scipy.interpolate import griddata

#elems = np.loadtxt('elems.csv', delimiter=",").astype(int)
#nodes = np.loadtxt('nodes.csv', delimiter=",")
fig = plt.figure()
#ax = fig.add_subplot(aspect=1)
elems = np.array([[  1,   2,   3],
       [  1,   4,   3],
       [  1,   4,   5],
       [  1,   2,   5],
       [  7,   2,   3],
       [  9,   4,   3],
       [ 11,   4,   5],
       [ 13,   2,   5],
       [  7,   2,   6],
       [  7,   8,   3],
       [  9,   4,  10],
       [  9,   8,   3],
       [ 11,   4,  10],
       [ 11,  12,   5],
       [ 13,   2,   6],
       [ 13,  12,   5],
       [  7,  15,   6],
       [  7,   8,  16],
       [  9,  19,  10],
       [  9,   8,  18],
       [ 11,  21,  10],
       [ 11,  12,  22],
       [ 13,  25,   6],
       [ 13,  12,  24],
       [ 14,  15,   6],
       [  7,  15,  16],
       [ 17,   8,  16],
       [ 20,  19,  10],
       [  9,  19,  18],
       [ 17,   8,  18],
       [ 20,  21,  10],
       [ 11,  21,  22],
       [ 23,  12,  22],
       [ 14,  25,   6],
       [ 13,  25,  24],
       [ 23,  12,  24],
       [ 14,  15,  27],
       [ 28,  15,  16],
       [ 17,  29,  16],
       [ 20,  19,  33],
       [ 32,  19,  18],
       [ 17,  31,  18],
       [ 20,  21,  35],
       [ 36,  21,  22],
       [ 23,  37,  22],
       [ 14,  25,  41],
       [ 40,  25,  24],
       [ 23,  39,  24],
       [ 14,  26,  27],
       [ 28,  15,  27],
       [ 28,  29,  16],
       [ 17,  29,  30],
       [ 20,  34,  33],
       [ 32,  19,  33],
       [ 32,  31,  18],
       [ 17,  31,  30],
       [ 20,  34,  35],
       [ 36,  21,  35],
       [ 36,  37,  22],
       [ 23,  37,  38],
       [ 14,  26,  41],
       [ 40,  25,  41],
       [ 40,  39,  24],
       [ 23,  39,  38],
       [ 43,  26,  27],
       [ 28,  44,  27],
       [ 28,  29,  45],
       [ 46,  29,  30],
       [ 51,  34,  33],
       [ 32,  50,  33],
       [ 32,  31,  49],
       [ 48,  31,  30],
       [ 53,  34,  35],
       [ 36,  54,  35],
       [ 36,  37,  55],
       [ 56,  37,  38],
       [ 61,  26,  41],
       [ 40,  60,  41],
       [ 40,  39,  59],
       [ 58,  39,  38],
       [ 43,  26,  42],
       [ 43,  44,  27],
       [ 28,  44,  45],
       [ 46,  29,  45],
       [ 46,  47,  30],
       [ 51,  34,  52],
       [ 51,  50,  33],
       [ 32,  50,  49],
       [ 48,  31,  49],
       [ 48,  47,  30],
       [ 53,  34,  52],
       [ 53,  54,  35],
       [ 36,  54,  55],
       [ 56,  37,  55],
       [ 56,  57,  38],
       [ 61,  26,  42],
       [ 61,  60,  41],
       [ 40,  60,  59],
       [ 58,  39,  59],
       [ 58,  57,  38],
       [ 43,  63,  42],
       [ 43,  44,  64],
       [ 65,  44,  45],
       [ 46,  66,  45],
       [ 46,  47,  67],
       [ 51,  73,  52],
       [ 51,  50,  72],
       [ 71,  50,  49],
       [ 48,  70,  49],
       [ 48,  47,  69],
       [ 53,  75,  52],
       [ 53,  54,  76],
       [ 77,  54,  55],
       [ 56,  78,  55],
       [ 56,  57,  79],
       [ 61,  85,  42],
       [ 61,  60,  84],
       [ 83,  60,  59],
       [ 58,  82,  59],
       [ 58,  57,  81],
       [ 62,  63,  42],
       [ 43,  63,  64],
       [ 65,  44,  64],
       [ 65,  66,  45],
       [ 46,  66,  67],
       [ 68,  47,  67],
       [ 74,  73,  52],
       [ 51,  73,  72],
       [ 71,  50,  72],
       [ 71,  70,  49],
       [ 48,  70,  69],
       [ 68,  47,  69],
       [ 74,  75,  52],
       [ 53,  75,  76],
       [ 77,  54,  76],
       [ 77,  78,  55],
       [ 56,  78,  79],
       [ 80,  57,  79],
       [ 62,  85,  42],
       [ 61,  85,  84],
       [ 83,  60,  84],
       [ 83,  82,  59],
       [ 58,  82,  81],
       [ 80,  57,  81],
       [ 62,  63,  87],
       [ 88,  63,  64],
       [ 65,  89,  64],
       [ 65,  66,  90],
       [ 91,  66,  67],
       [ 68,  92,  67],
       [ 74,  73,  99],
       [ 98,  73,  72],
       [ 71,  97,  72],
       [ 71,  70,  96],
       [ 95,  70,  69],
       [ 68,  94,  69],
       [ 74,  75, 101],
       [102,  75,  76],
       [ 77, 103,  76],
       [ 77,  78, 104],
       [105,  78,  79],
       [ 80, 106,  79],
       [ 62,  85, 113],
       [112,  85,  84],
       [ 83, 111,  84],
       [ 83,  82, 110],
       [109,  82,  81],
       [ 80, 108,  81],
       [ 62,  86,  87],
       [ 88,  63,  87],
       [ 88,  89,  64],
       [ 65,  89,  90],
       [ 91,  66,  90],
       [ 91,  92,  67],
       [ 68,  92,  93],
       [ 74, 100,  99],
       [ 98,  73,  99],
       [ 98,  97,  72],
       [ 71,  97,  96],
       [ 95,  70,  96],
       [ 95,  94,  69],
       [ 68,  94,  93],
       [ 74, 100, 101],
       [102,  75, 101],
       [102, 103,  76],
       [ 77, 103, 104],
       [105,  78, 104],
       [105, 106,  79],
       [ 80, 106, 107],
       [ 62,  86, 113],
       [112,  85, 113],
       [112, 111,  84],
       [ 83, 111, 110],
       [109,  82, 110],
       [109, 108,  81],
       [ 80, 108, 107],
       [115,  86,  87],
       [ 88, 116,  87],
       [ 88,  89, 117],
       [118,  89,  90],
       [ 91, 119,  90],
       [ 91,  92, 120],
       [121,  92,  93],
       [129, 100,  99],
       [ 98, 128,  99],
       [ 98,  97, 127],
       [126,  97,  96],
       [ 95, 125,  96],
       [ 95,  94, 124],
       [123,  94,  93],
       [131, 100, 101],
       [102, 132, 101],
       [102, 103, 133],
       [134, 103, 104],
       [105, 135, 104],
       [105, 106, 136],
       [137, 106, 107],
       [145,  86, 113],
       [112, 144, 113],
       [112, 111, 143],
       [142, 111, 110],
       [109, 141, 110],
       [109, 108, 140],
       [139, 108, 107],
       [115,  86, 114],
       [115, 116,  87],
       [ 88, 116, 117],
       [118,  89, 117],
       [118, 119,  90],
       [ 91, 119, 120],
       [121,  92, 120],
       [121, 122,  93],
       [129, 100, 130],
       [129, 128,  99],
       [ 98, 128, 127],
       [126,  97, 127],
       [126, 125,  96],
       [ 95, 125, 124],
       [123,  94, 124],
       [123, 122,  93],
       [131, 100, 130],
       [131, 132, 101],
       [102, 132, 133],
       [134, 103, 133],
       [134, 135, 104],
       [105, 135, 136],
       [137, 106, 136],
       [137, 138, 107],
       [145,  86, 114],
       [145, 144, 113],
       [112, 144, 143],
       [142, 111, 143],
       [142, 141, 110],
       [109, 141, 140],
       [139, 108, 140],
       [139, 138, 107],
       [115, 147, 114],
       [115, 116, 148],
       [149, 116, 117],
       [118, 150, 117],
       [118, 119, 151],
       [152, 119, 120],
       [121, 153, 120],
       [121, 122, 154],
       [129, 163, 130],
       [129, 128, 162],
       [161, 128, 127],
       [126, 160, 127],
       [126, 125, 159],
       [158, 125, 124],
       [123, 157, 124],
       [123, 122, 156],
       [131, 165, 130],
       [131, 132, 166],
       [167, 132, 133],
       [134, 168, 133],
       [134, 135, 169],
       [170, 135, 136],
       [137, 171, 136],
       [137, 138, 172],
       [145, 181, 114],
       [145, 144, 180],
       [179, 144, 143],
       [142, 178, 143],
       [142, 141, 177],
       [176, 141, 140],
       [139, 175, 140],
       [139, 138, 174],
       [146, 147, 114],
       [115, 147, 148],
       [149, 116, 148],
       [149, 150, 117],
       [118, 150, 151],
       [152, 119, 151],
       [152, 153, 120],
       [121, 153, 154],
       [155, 122, 154],
       [164, 163, 130],
       [129, 163, 162],
       [161, 128, 162],
       [161, 160, 127],
       [126, 160, 159],
       [158, 125, 159],
       [158, 157, 124],
       [123, 157, 156],
       [155, 122, 156],
       [164, 165, 130],
       [131, 165, 166],
       [167, 132, 166],
       [167, 168, 133],
       [134, 168, 169],
       [170, 135, 169],
       [170, 171, 136],
       [137, 171, 172],
       [173, 138, 172],
       [146, 181, 114],
       [145, 181, 180],
       [179, 144, 180],
       [179, 178, 143],
       [142, 178, 177],
       [176, 141, 177],
       [176, 175, 140],
       [139, 175, 174],
       [173, 138, 174],
       [146, 147, 183],
       [184, 147, 148],
       [149, 185, 148],
       [149, 150, 186],
       [187, 150, 151],
       [152, 188, 151],
       [152, 153, 189],
       [190, 153, 154],
       [155, 191, 154],
       [164, 163, 201],
       [200, 163, 162],
       [161, 199, 162],
       [161, 160, 198],
       [197, 160, 159],
       [158, 196, 159],
       [158, 157, 195],
       [194, 157, 156],
       [155, 193, 156],
       [164, 165, 203],
       [204, 165, 166],
       [167, 205, 166],
       [167, 168, 206],
       [207, 168, 169],
       [170, 208, 169],
       [170, 171, 209],
       [210, 171, 172],
       [173, 211, 172],
       [146, 181, 221],
       [220, 181, 180],
       [179, 219, 180],
       [179, 178, 218],
       [217, 178, 177],
       [176, 216, 177],
       [176, 175, 215],
       [214, 175, 174],
       [173, 213, 174],
       [146, 182, 183],
       [184, 147, 183],
       [184, 185, 148],
       [149, 185, 186],
       [187, 150, 186],
       [187, 188, 151],
       [152, 188, 189],
       [190, 153, 189],
       [190, 191, 154],
       [155, 191, 192],
       [164, 202, 201],
       [200, 163, 201],
       [200, 199, 162],
       [161, 199, 198],
       [197, 160, 198],
       [197, 196, 159],
       [158, 196, 195],
       [194, 157, 195],
       [194, 193, 156],
       [155, 193, 192],
       [164, 202, 203],
       [204, 165, 203],
       [204, 205, 166],
       [167, 205, 206],
       [207, 168, 206],
       [207, 208, 169],
       [170, 208, 209],
       [210, 171, 209],
       [210, 211, 172],
       [173, 211, 212],
       [146, 182, 221],
       [220, 181, 221],
       [220, 219, 180],
       [179, 219, 218],
       [217, 178, 218],
       [217, 216, 177],
       [176, 216, 215],
       [214, 175, 215],
       [214, 213, 174],
       [173, 213, 212],
       [223, 182, 183],
       [184, 224, 183],
       [184, 185, 225],
       [226, 185, 186],
       [187, 227, 186],
       [187, 188, 228],
       [229, 188, 189],
       [190, 230, 189],
       [190, 191, 231],
       [232, 191, 192],
       [243, 202, 201],
       [200, 242, 201],
       [200, 199, 241],
       [240, 199, 198],
       [197, 239, 198],
       [197, 196, 238],
       [237, 196, 195],
       [194, 236, 195],
       [194, 193, 235],
       [234, 193, 192],
       [245, 202, 203],
       [204, 246, 203],
       [204, 205, 247],
       [248, 205, 206],
       [207, 249, 206],
       [207, 208, 250],
       [251, 208, 209],
       [210, 252, 209],
       [210, 211, 253],
       [254, 211, 212],
       [265, 182, 221],
       [220, 264, 221],
       [220, 219, 263],
       [262, 219, 218],
       [217, 261, 218],
       [217, 216, 260],
       [259, 216, 215],
       [214, 258, 215],
       [214, 213, 257],
       [256, 213, 212],
       [223, 182, 222],
       [223, 224, 183],
       [184, 224, 225],
       [226, 185, 225],
       [226, 227, 186],
       [187, 227, 228],
       [229, 188, 228],
       [229, 230, 189],
       [190, 230, 231],
       [232, 191, 231],
       [232, 233, 192],
       [243, 202, 244],
       [243, 242, 201],
       [200, 242, 241],
       [240, 199, 241],
       [240, 239, 198],
       [197, 239, 238],
       [237, 196, 238],
       [237, 236, 195],
       [194, 236, 235],
       [234, 193, 235],
       [234, 233, 192],
       [245, 202, 244],
       [245, 246, 203],
       [204, 246, 247],
       [248, 205, 247],
       [248, 249, 206],
       [207, 249, 250],
       [251, 208, 250],
       [251, 252, 209],
       [210, 252, 253],
       [254, 211, 253],
       [254, 255, 212],
       [265, 182, 222],
       [265, 264, 221],
       [220, 264, 263],
       [262, 219, 263],
       [262, 261, 218],
       [217, 261, 260],
       [259, 216, 260],
       [259, 258, 215],
       [214, 258, 257],
       [256, 213, 257],
       [256, 255, 212],
       [223, 267, 222],
       [223, 224, 268],
       [269, 224, 225],
       [226, 270, 225],
       [226, 227, 271],
       [272, 227, 228],
       [229, 273, 228],
       [229, 230, 274],
       [275, 230, 231],
       [232, 276, 231],
       [232, 233, 277],
       [243, 289, 244],
       [243, 242, 288],
       [287, 242, 241],
       [240, 286, 241],
       [240, 239, 285],
       [284, 239, 238],
       [237, 283, 238],
       [237, 236, 282],
       [281, 236, 235],
       [234, 280, 235],
       [234, 233, 279],
       [245, 291, 244],
       [245, 246, 292],
       [293, 246, 247],
       [248, 294, 247],
       [248, 249, 295],
       [296, 249, 250],
       [251, 297, 250],
       [251, 252, 298],
       [299, 252, 253],
       [254, 300, 253],
       [254, 255, 301],
       [265, 313, 222],
       [265, 264, 312],
       [311, 264, 263],
       [262, 310, 263],
       [262, 261, 309],
       [308, 261, 260],
       [259, 307, 260],
       [259, 258, 306],
       [305, 258, 257],
       [256, 304, 257],
       [256, 255, 303],
       [266, 267, 222],
       [223, 267, 268],
       [269, 224, 268],
       [269, 270, 225],
       [226, 270, 271],
       [272, 227, 271],
       [272, 273, 228],
       [229, 273, 274],
       [275, 230, 274],
       [275, 276, 231],
       [232, 276, 277],
       [278, 233, 277],
       [290, 289, 244],
       [243, 289, 288],
       [287, 242, 288],
       [287, 286, 241],
       [240, 286, 285],
       [284, 239, 285],
       [284, 283, 238],
       [237, 283, 282],
       [281, 236, 282],
       [281, 280, 235],
       [234, 280, 279],
       [278, 233, 279],
       [290, 291, 244],
       [245, 291, 292],
       [293, 246, 292],
       [293, 294, 247],
       [248, 294, 295],
       [296, 249, 295],
       [296, 297, 250],
       [251, 297, 298],
       [299, 252, 298],
       [299, 300, 253],
       [254, 300, 301],
       [302, 255, 301],
       [266, 313, 222],
       [265, 313, 312],
       [311, 264, 312],
       [311, 310, 263],
       [262, 310, 309],
       [308, 261, 309],
       [308, 307, 260],
       [259, 307, 306],
       [305, 258, 306],
       [305, 304, 257],
       [256, 304, 303],
       [302, 255, 303]])
nodes = np.array([[ 0.0000e+00,  0.0000e+00],
       [ 0.0000e+00,  8.3333e-02],
       [ 8.3333e-02,  5.1027e-18],
       [ 1.0205e-17, -8.3333e-02],
       [-8.3333e-02, -1.5308e-17],
       [ 0.0000e+00,  1.6667e-01],
       [ 1.1785e-01,  1.1785e-01],
       [ 1.6667e-01,  1.0205e-17],
       [ 1.1785e-01, -1.1785e-01],
       [ 2.0411e-17, -1.6667e-01],
       [-1.1785e-01, -1.1785e-01],
       [-1.6667e-01, -3.0616e-17],
       [-1.1785e-01,  1.1785e-01],
       [ 0.0000e+00,  2.5000e-01],
       [ 1.2500e-01,  2.1651e-01],
       [ 2.1651e-01,  1.2500e-01],
       [ 2.5000e-01,  1.5308e-17],
       [ 2.1651e-01, -1.2500e-01],
       [ 1.2500e-01, -2.1651e-01],
       [ 3.0616e-17, -2.5000e-01],
       [-1.2500e-01, -2.1651e-01],
       [-2.1651e-01, -1.2500e-01],
       [-2.5000e-01, -4.5924e-17],
       [-2.1651e-01,  1.2500e-01],
       [-1.2500e-01,  2.1651e-01],
       [ 0.0000e+00,  3.3333e-01],
       [ 1.2756e-01,  3.0796e-01],
       [ 2.3570e-01,  2.3570e-01],
       [ 3.0796e-01,  1.2756e-01],
       [ 3.3333e-01,  2.0411e-17],
       [ 3.0796e-01, -1.2756e-01],
       [ 2.3570e-01, -2.3570e-01],
       [ 1.2756e-01, -3.0796e-01],
       [ 4.0822e-17, -3.3333e-01],
       [-1.2756e-01, -3.0796e-01],
       [-2.3570e-01, -2.3570e-01],
       [-3.0796e-01, -1.2756e-01],
       [-3.3333e-01, -6.1232e-17],
       [-3.0796e-01,  1.2756e-01],
       [-2.3570e-01,  2.3570e-01],
       [-1.2756e-01,  3.0796e-01],
       [ 0.0000e+00,  4.1667e-01],
       [ 1.2876e-01,  3.9627e-01],
       [ 2.4491e-01,  3.3709e-01],
       [ 3.3709e-01,  2.4491e-01],
       [ 3.9627e-01,  1.2876e-01],
       [ 4.1667e-01,  2.5513e-17],
       [ 3.9627e-01, -1.2876e-01],
       [ 3.3709e-01, -2.4491e-01],
       [ 2.4491e-01, -3.3709e-01],
       [ 1.2876e-01, -3.9627e-01],
       [ 5.1027e-17, -4.1667e-01],
       [-1.2876e-01, -3.9627e-01],
       [-2.4491e-01, -3.3709e-01],
       [-3.3709e-01, -2.4491e-01],
       [-3.9627e-01, -1.2876e-01],
       [-4.1667e-01, -7.6540e-17],
       [-3.9627e-01,  1.2876e-01],
       [-3.3709e-01,  2.4491e-01],
       [-2.4491e-01,  3.3709e-01],
       [-1.2876e-01,  3.9627e-01],
       [ 0.0000e+00,  5.0000e-01],
       [ 1.2941e-01,  4.8296e-01],
       [ 2.5000e-01,  4.3301e-01],
       [ 3.5355e-01,  3.5355e-01],
       [ 4.3301e-01,  2.5000e-01],
       [ 4.8296e-01,  1.2941e-01],
       [ 5.0000e-01,  3.0616e-17],
       [ 4.8296e-01, -1.2941e-01],
       [ 4.3301e-01, -2.5000e-01],
       [ 3.5355e-01, -3.5355e-01],
       [ 2.5000e-01, -4.3301e-01],
       [ 1.2941e-01, -4.8296e-01],
       [ 6.1232e-17, -5.0000e-01],
       [-1.2941e-01, -4.8296e-01],
       [-2.5000e-01, -4.3301e-01],
       [-3.5355e-01, -3.5355e-01],
       [-4.3301e-01, -2.5000e-01],
       [-4.8296e-01, -1.2941e-01],
       [-5.0000e-01, -9.1849e-17],
       [-4.8296e-01,  1.2941e-01],
       [-4.3301e-01,  2.5000e-01],
       [-3.5355e-01,  3.5355e-01],
       [-2.5000e-01,  4.3301e-01],
       [-1.2941e-01,  4.8296e-01],
       [ 0.0000e+00,  5.8333e-01],
       [ 1.2980e-01,  5.6871e-01],
       [ 2.5310e-01,  5.2557e-01],
       [ 3.6370e-01,  4.5607e-01],
       [ 4.5607e-01,  3.6370e-01],
       [ 5.2557e-01,  2.5310e-01],
       [ 5.6871e-01,  1.2980e-01],
       [ 5.8333e-01,  3.5719e-17],
       [ 5.6871e-01, -1.2980e-01],
       [ 5.2557e-01, -2.5310e-01],
       [ 4.5607e-01, -3.6370e-01],
       [ 3.6370e-01, -4.5607e-01],
       [ 2.5310e-01, -5.2557e-01],
       [ 1.2980e-01, -5.6871e-01],
       [ 7.1438e-17, -5.8333e-01],
       [-1.2980e-01, -5.6871e-01],
       [-2.5310e-01, -5.2557e-01],
       [-3.6370e-01, -4.5607e-01],
       [-4.5607e-01, -3.6370e-01],
       [-5.2557e-01, -2.5310e-01],
       [-5.6871e-01, -1.2980e-01],
       [-5.8333e-01, -1.0716e-16],
       [-5.6871e-01,  1.2980e-01],
       [-5.2557e-01,  2.5310e-01],
       [-4.5607e-01,  3.6370e-01],
       [-3.6370e-01,  4.5607e-01],
       [-2.5310e-01,  5.2557e-01],
       [-1.2980e-01,  5.6871e-01],
       [ 0.0000e+00,  6.6667e-01],
       [ 1.3006e-01,  6.5386e-01],
       [ 2.5512e-01,  6.1592e-01],
       [ 3.7038e-01,  5.5431e-01],
       [ 4.7140e-01,  4.7140e-01],
       [ 5.5431e-01,  3.7038e-01],
       [ 6.1592e-01,  2.5512e-01],
       [ 6.5386e-01,  1.3006e-01],
       [ 6.6667e-01,  4.0822e-17],
       [ 6.5386e-01, -1.3006e-01],
       [ 6.1592e-01, -2.5512e-01],
       [ 5.5431e-01, -3.7038e-01],
       [ 4.7140e-01, -4.7140e-01],
       [ 3.7038e-01, -5.5431e-01],
       [ 2.5512e-01, -6.1592e-01],
       [ 1.3006e-01, -6.5386e-01],
       [ 8.1643e-17, -6.6667e-01],
       [-1.3006e-01, -6.5386e-01],
       [-2.5512e-01, -6.1592e-01],
       [-3.7038e-01, -5.5431e-01],
       [-4.7140e-01, -4.7140e-01],
       [-5.5431e-01, -3.7038e-01],
       [-6.1592e-01, -2.5512e-01],
       [-6.5386e-01, -1.3006e-01],
       [-6.6667e-01, -1.2246e-16],
       [-6.5386e-01,  1.3006e-01],
       [-6.1592e-01,  2.5512e-01],
       [-5.5431e-01,  3.7038e-01],
       [-4.7140e-01,  4.7140e-01],
       [-3.7038e-01,  5.5431e-01],
       [-2.5512e-01,  6.1592e-01],
       [-1.3006e-01,  6.5386e-01],
       [ 0.0000e+00,  7.5000e-01],
       [ 1.3024e-01,  7.3861e-01],
       [ 2.5652e-01,  7.0477e-01],
       [ 3.7500e-01,  6.4952e-01],
       [ 4.8209e-01,  5.7453e-01],
       [ 5.7453e-01,  4.8209e-01],
       [ 6.4952e-01,  3.7500e-01],
       [ 7.0477e-01,  2.5652e-01],
       [ 7.3861e-01,  1.3024e-01],
       [ 7.5000e-01,  4.5924e-17],
       [ 7.3861e-01, -1.3024e-01],
       [ 7.0477e-01, -2.5652e-01],
       [ 6.4952e-01, -3.7500e-01],
       [ 5.7453e-01, -4.8209e-01],
       [ 4.8209e-01, -5.7453e-01],
       [ 3.7500e-01, -6.4952e-01],
       [ 2.5652e-01, -7.0477e-01],
       [ 1.3024e-01, -7.3861e-01],
       [ 9.1849e-17, -7.5000e-01],
       [-1.3024e-01, -7.3861e-01],
       [-2.5652e-01, -7.0477e-01],
       [-3.7500e-01, -6.4952e-01],
       [-4.8209e-01, -5.7453e-01],
       [-5.7453e-01, -4.8209e-01],
       [-6.4952e-01, -3.7500e-01],
       [-7.0477e-01, -2.5652e-01],
       [-7.3861e-01, -1.3024e-01],
       [-7.5000e-01, -1.3777e-16],
       [-7.3861e-01,  1.3024e-01],
       [-7.0477e-01,  2.5652e-01],
       [-6.4952e-01,  3.7500e-01],
       [-5.7453e-01,  4.8209e-01],
       [-4.8209e-01,  5.7453e-01],
       [-3.7500e-01,  6.4952e-01],
       [-2.5652e-01,  7.0477e-01],
       [-1.3024e-01,  7.3861e-01],
       [ 0.0000e+00,  8.3333e-01],
       [ 1.3036e-01,  8.2307e-01],
       [ 2.5751e-01,  7.9255e-01],
       [ 3.7833e-01,  7.4251e-01],
       [ 4.8982e-01,  6.7418e-01],
       [ 5.8926e-01,  5.8926e-01],
       [ 6.7418e-01,  4.8982e-01],
       [ 7.4251e-01,  3.7833e-01],
       [ 7.9255e-01,  2.5751e-01],
       [ 8.2307e-01,  1.3036e-01],
       [ 8.3333e-01,  5.1027e-17],
       [ 8.2307e-01, -1.3036e-01],
       [ 7.9255e-01, -2.5751e-01],
       [ 7.4251e-01, -3.7833e-01],
       [ 6.7418e-01, -4.8982e-01],
       [ 5.8926e-01, -5.8926e-01],
       [ 4.8982e-01, -6.7418e-01],
       [ 3.7833e-01, -7.4251e-01],
       [ 2.5751e-01, -7.9255e-01],
       [ 1.3036e-01, -8.2307e-01],
       [ 1.0205e-16, -8.3333e-01],
       [-1.3036e-01, -8.2307e-01],
       [-2.5751e-01, -7.9255e-01],
       [-3.7833e-01, -7.4251e-01],
       [-4.8982e-01, -6.7418e-01],
       [-5.8926e-01, -5.8926e-01],
       [-6.7418e-01, -4.8982e-01],
       [-7.4251e-01, -3.7833e-01],
       [-7.9255e-01, -2.5751e-01],
       [-8.2307e-01, -1.3036e-01],
       [-8.3333e-01, -1.5308e-16],
       [-8.2307e-01,  1.3036e-01],
       [-7.9255e-01,  2.5751e-01],
       [-7.4251e-01,  3.7833e-01],
       [-6.7418e-01,  4.8982e-01],
       [-5.8926e-01,  5.8926e-01],
       [-4.8982e-01,  6.7418e-01],
       [-3.7833e-01,  7.4251e-01],
       [-2.5751e-01,  7.9255e-01],
       [-1.3036e-01,  8.2307e-01],
       [ 0.0000e+00,  9.1667e-01],
       [ 1.3046e-01,  9.0734e-01],
       [ 2.5825e-01,  8.7954e-01],
       [ 3.8080e-01,  8.3383e-01],
       [ 4.9559e-01,  7.7115e-01],
       [ 6.0029e-01,  6.9277e-01],
       [ 6.9277e-01,  6.0029e-01],
       [ 7.7115e-01,  4.9559e-01],
       [ 8.3383e-01,  3.8080e-01],
       [ 8.7954e-01,  2.5825e-01],
       [ 9.0734e-01,  1.3046e-01],
       [ 9.1667e-01,  2.5967e-16],
       [ 9.0734e-01, -1.3046e-01],
       [ 8.7954e-01, -2.5825e-01],
       [ 8.3383e-01, -3.8080e-01],
       [ 7.7115e-01, -4.9559e-01],
       [ 6.9277e-01, -6.0029e-01],
       [ 6.0029e-01, -6.9277e-01],
       [ 4.9559e-01, -7.7115e-01],
       [ 3.8080e-01, -8.3383e-01],
       [ 2.5825e-01, -8.7954e-01],
       [ 1.3046e-01, -9.0734e-01],
       [ 5.1934e-16, -9.1667e-01],
       [-1.3046e-01, -9.0734e-01],
       [-2.5825e-01, -8.7954e-01],
       [-3.8080e-01, -8.3383e-01],
       [-4.9559e-01, -7.7115e-01],
       [-6.0029e-01, -6.9277e-01],
       [-6.9277e-01, -6.0029e-01],
       [-7.7115e-01, -4.9559e-01],
       [-8.3383e-01, -3.8080e-01],
       [-8.7954e-01, -2.5825e-01],
       [-9.0734e-01, -1.3046e-01],
       [-9.1667e-01, -1.6839e-16],
       [-9.0734e-01,  1.3046e-01],
       [-8.7954e-01,  2.5825e-01],
       [-8.3383e-01,  3.8080e-01],
       [-7.7115e-01,  4.9559e-01],
       [-6.9277e-01,  6.0029e-01],
       [-6.0029e-01,  6.9277e-01],
       [-4.9559e-01,  7.7115e-01],
       [-3.8080e-01,  8.3383e-01],
       [-2.5825e-01,  8.7954e-01],
       [-1.3046e-01,  9.0734e-01],
       [ 0.0000e+00,  1.0000e+00],
       [ 1.3053e-01,  9.9144e-01],
       [ 2.5882e-01,  9.6593e-01],
       [ 3.8268e-01,  9.2388e-01],
       [ 5.0000e-01,  8.6603e-01],
       [ 6.0876e-01,  7.9335e-01],
       [ 7.0711e-01,  7.0711e-01],
       [ 7.9335e-01,  6.0876e-01],
       [ 8.6603e-01,  5.0000e-01],
       [ 9.2388e-01,  3.8268e-01],
       [ 9.6593e-01,  2.5882e-01],
       [ 9.9144e-01,  1.3053e-01],
       [ 1.0000e+00,  6.1232e-17],
       [ 9.9144e-01, -1.3053e-01],
       [ 9.6593e-01, -2.5882e-01],
       [ 9.2388e-01, -3.8268e-01],
       [ 8.6603e-01, -5.0000e-01],
       [ 7.9335e-01, -6.0876e-01],
       [ 7.0711e-01, -7.0711e-01],
       [ 6.0876e-01, -7.9335e-01],
       [ 5.0000e-01, -8.6603e-01],
       [ 3.8268e-01, -9.2388e-01],
       [ 2.5882e-01, -9.6593e-01],
       [ 1.3053e-01, -9.9144e-01],
       [ 1.2246e-16, -1.0000e+00],
       [-1.3053e-01, -9.9144e-01],
       [-2.5882e-01, -9.6593e-01],
       [-3.8268e-01, -9.2388e-01],
       [-5.0000e-01, -8.6603e-01],
       [-6.0876e-01, -7.9335e-01],
       [-7.0711e-01, -7.0711e-01],
       [-7.9335e-01, -6.0876e-01],
       [-8.6603e-01, -5.0000e-01],
       [-9.2388e-01, -3.8268e-01],
       [-9.6593e-01, -2.5882e-01],
       [-9.9144e-01, -1.3053e-01],
       [-1.0000e+00, -1.8370e-16],
       [-9.9144e-01,  1.3053e-01],
       [-9.6593e-01,  2.5882e-01],
       [-9.2388e-01,  3.8268e-01],
       [-8.6603e-01,  5.0000e-01],
       [-7.9335e-01,  6.0876e-01],
       [-7.0711e-01,  7.0711e-01],
       [-6.0876e-01,  7.9335e-01],
       [-5.0000e-01,  8.6603e-01],
       [-3.8268e-01,  9.2388e-01],
       [-2.5882e-01,  9.6593e-01],
       [-1.3053e-01,  9.9144e-01]])
triang = Triangulation(nodes[:,0], nodes[:,1])
#ax.triplot(triang,linewidth=0.6,color='black')
cmap = plt.cm.RdBu.reversed()
norm = matplotlib.colors.Normalize(vmin=-1, vmax=1)

refedata = np.loadtxt(r'D:\Proj\EIT\EIT-py\data\refedata.csv', delimiter=",")
projdata = np.loadtxt(r'D:\Proj\EIT\EIT-py\data\projdata1.csv', delimiter=",")
proj = projdata-refedata
jacobian = np.loadtxt(r'D:\Proj\EIT\EIT-py\data\jacobian.csv', delimiter=",")

"""灵敏度归一化
W = np.zeros((576,576))
for i in np.arange(576):
    j2 = jacobian**2
    j2 = j2.sum(axis=0)
    j2 = j2 ** (-0.5)
    W[i,i] = j2[i]
A = np.dot(W, np.linalg.pinv(np.dot(jacobian, W)))
elem_data = np.dot(A, proj)"""
inv_j = np.linalg.pinv(jacobian)
elem_data = np.dot(inv_j, proj)
elem_data = elem_data/np.max(np.abs(elem_data))
alphas = Normalize(0, 0.5, clip=True)(np.abs(elem_data))###########
elem_data = elem_data * alphas##########
#norm = matplotlib.colors.Normalize(vmin=np.min(elem_data), vmax=np.max(elem_data))

#ax.cla()
"""单元填充图"""
ax1 = fig.add_subplot(2,2,1,aspect=1)
ax1.set_xticks([-1,1])
ax1.set_yticks([-1,1])
for i in np.arange(576):
    xs = triang.x[elems[i] - 1]
    ys = triang.y[elems[i] - 1]
    polygon = Polygon(list(zip(xs, ys)), facecolor=cmap(norm(elem_data[i])))
    ax1.add_patch(polygon)

"""求elem坐标中心点，作为已知导入"""
point = np.zeros((576, 2))
for i in np.arange(576):
    xs = triang.x[elems[i] - 1]
    ys = triang.y[elems[i] - 1]
    p = np.array(list(zip(xs, ys)))
    point[i] = np.mean(p, axis=0)
"""插值热图"""
ax2 = fig.add_subplot(2,2,2,aspect=1)
ax2.set_xticks([])
ax2.set_yticks([])
grid_x, grid_y = np.mgrid[-1:1:50j, -1:1:50j]
#img = griddata(point, elem_data, (grid_x, grid_y), method='cubic',fill_value = 0)
img = griddata(point, elem_data, (grid_x, grid_y), method='cubic')
#ax2.imshow(img, aspect=1, cmap=matplotlib.cm.RdBu.reversed(), vmin=np.min(elem_data), vmax=np.max(elem_data), origin='lower', interpolation='bicubic')
ax2.imshow(img, aspect=1, cmap=matplotlib.cm.RdBu.reversed(), norm = norm, origin='lower', interpolation='bicubic')

"""等值线填充"""
ax3 = fig.add_subplot(2,2,3,aspect=1)
ax3.set_xticks([])
ax3.set_yticks([])
ax3.tricontour(point[:,0], point[:,1], elem_data, levels=5, linewidths=0.5, colors='k')
cntr3 = ax3.tricontourf(point[:,0], point[:,1], elem_data, cmap="RdBu_r", norm = norm, levels=5)

"""等值线轮廓"""
ax4 = fig.add_subplot(2,2,4,aspect=1)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.tricontour(point[:,0], point[:,1], elem_data, cmap="RdBu_r", norm = norm, levels=6, linewidths=0.5)

plt.show()