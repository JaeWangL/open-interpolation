import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from scipy.interpolate import griddata

def interpolation(xValues, yValues, zValues, denseNum = 1000, method='linear', showPlot = False):
    """
    Function for interpolation with given 3d points

    Parameters:
        xValues (numpy array): numpy number (n, 1) array for x
        yValues (numpy array): numpy number (n, 1) array for y
        zValues (numpy array): numpy number (n, 1) array for z
        denseNum (num): number of how much split values
        method ('linear' | 'nearest' | 'cubic'): interpolation method

    Returns:
        points: interpolated (n, 3) array containing (x, y, z)
    """
    x_dense = np.linspace(min(xValues), max(xValues), denseNum)
    y_dense =  np.linspace(min(yValues), max(yValues), denseNum)
    X, Y = np.meshgrid(x_dense, y_dense)
    Z = griddata(np.array(np.column_stack((xValues, yValues))), np.array(zValues), (X, Y), method=method)

    if showPlot == True:
        # NOTE: show DSM
        plt.subplot(111)
        plt.hexbin(X.ravel(), Y.ravel(), C=Z.ravel(), cmap=cm.jet, bins=None)
        plt.axis([X.min(), X.max(), Y.min(), Y.max()])

        # NOTE: show 3d point clouds
        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        surf = ax.plot_wireframe(X, Y, Z)
        plt.show()

    return np.column_stack((X.ravel(), Y.ravel(), Z.ravel()))