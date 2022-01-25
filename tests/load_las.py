import laspy

def loadFromLas(filePath):
    """
    Function for loading las file

    Parameters:
        filePath (str): las file path with filename

    Returns:
        points: simple numpy (n, 3) array containing (x, y, z)
    """
    las = laspy.read(filePath)
    print('Points from data:', len(las.points))
    ground_points = las.classification == 2
    print(ground_points)
