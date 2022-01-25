import numpy as np

def loadFromTxt(filePath, delimiter=' '):
    """
    Function for loading txt file

    Parameters:
        filePath (str): txt file path with filename

    Returns:
        points: simple numpy (n, 3) array containing (x, y, z)
    """
    points = np.loadtxt(filePath, delimiter=delimiter)

    return points
