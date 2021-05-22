# This is a sample Python script.
try:
    get_ipython().magic(u'load_ext autoreload')
    get_ipython().magic(u'autoreload 2')
    print(1)
except:
    print('NOT IPYTHON')

import logging
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.ndimage.filters import gaussian_filter
from tifffile.tifffile import imsave

import caiman as cm
from caiman.utils.visualization import nb_view_patches3d
import caiman.source_extraction.cnmf as cnmf
from caiman.paths import caiman_datadir

import tiffstack2avi

import bokeh.plotting as bpl
bpl.output_notebook()
logging.basicConfig(format=
                          "%(relativeCreated)12d [%(filename)s:%(funcName)20s():%(lineno)s] [%(process)d] %(message)s",
                    # filename="/tmp/caiman.log",
                    level=logging.DEBUG)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def caiman_test():
    # Use a breakpoint in the code line below to debug your script.
    list_dir = []

    tiffstack2avi.convert('images')

    for i in range(500):
        dir = 'images/image0'
        if int(i/1000) == 0:
            dir = dir + '0'
            if int(i/100) == 0:
                dir = dir + '0'
                if int(i/10) == 0:
                    dir = dir + '0'
        dir = dir + str(i)
        dir = dir + '.tif'
        list_dir.append(dir)
    print(list_dir)
    single_movie = cm.load_movie_chain(list_dir)

    #print( single_movie.shape )
    single_movie.play(magnification=2, fr=30, q_min=0.1, q_max=99.75)

    # plt.imshow(np.mean(single_movie, 0))
    # plt.imshow(np.std(single_movie, 0))
    # plt.plot( np.mean(single_movie, axis=(1, 2)) )

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("HELLO")
    #caiman_test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
