import numpy as np

def saveTxtFromPoints(filePath, interpolatedPoints):
    """
    Function for saving txt file from interpolated points

    Parameters:
        filePath (str): las file path with filename for saving
        interpolatedPoints (numpy array): numpy (n, 3) array containing (x, y, z)

    Returns:
        void
    """
    np.savetxt(filePath, interpolatedPoints, '%.5f')
