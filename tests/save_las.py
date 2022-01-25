import laspy
import numpy as np

def saveLasFromPoints(filePath, interpolatedPoints):
    """
    Function for saving las file from interpolated points

    Parameters:
        filePath (str): las file path with filename for saving
        interpolatedPoints (numpy array): numpy (n, 3) array containing (x, y, z)

    Returns:
        void
    """
    header = laspy.LasHeader(point_format=3, version="1.2")
    header.add_extra_dim(laspy.ExtraBytesParams(name="random", type=np.int32))
    header.offsets = np.min(interpolatedPoints, axis=0)
    header.scales = np.array([0.0001, 0.0001, 0.0001])

    las = laspy.LasData(header)

    las.x = np.array(interpolatedPoints[:, 0])
    las.y = np.array(interpolatedPoints[:, 1])
    las.z = np.array(interpolatedPoints[:, 2])

    las.write(filePath)