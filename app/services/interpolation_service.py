import numpy as np
from scipy.interpolate import griddata

def getInterpolatedPoints(xValues, yValues, zValues, denseNum = 1000, method='linear', removeNan = True):
    x_dense = np.linspace(min(xValues), max(xValues), denseNum)
    y_dense =  np.linspace(min(yValues), max(yValues), denseNum)
    X, Y = np.meshgrid(x_dense, y_dense)
    Z = griddata(np.array(np.column_stack((xValues, yValues))), np.array(zValues), (X, Y), method=method)

    interpolatedPoints = np.column_stack((X.ravel(), Y.ravel(), Z.ravel()))
    if removeNan == True:
        return interpolatedPoints[~np.isnan(interpolatedPoints).any(axis=1)]
    
    return interpolatedPoints
