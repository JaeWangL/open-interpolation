import laspy
import numpy as np

def loadFromLas(filePath):
    """
    Function for loading las file

    Parameters:
        filePath (str): las file path with filename

    Returns:
        points: simple numpy (n, 3) array containing (x, y, z)
    """
    las = laspy.read(filePath)
    return np.vstack((las.x, las.y, las.z)).transpose()
