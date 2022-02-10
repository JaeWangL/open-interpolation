import os.path
import laspy
import numpy as np
from fastapi import UploadFile
from io import BytesIO, StringIO
from typing import IO, Iterator

def checkValidExtensions(filename: str) -> bool:
    extensions = os.path.splitext(filename)[1]
    validExtensions = ['txt', 'las']
    
    return any(x in extensions for x in validExtensions)

def pointsFromLas(file: IO):
    las = laspy.read(file)
    print('Points from data:', len(las.points))
    ground_points = las.classification == 2

    return ground_points

def pointsFromTxt(file: IO, delimiter=' '):
    points = np.loadtxt(file, delimiter=delimiter)

    return points

def readPointsFile(file: UploadFile):
    extensions = os.path.splitext(file.filename)[1]

    points = None
    if 'txt' in extensions:
        points = pointsFromTxt(file.file)
    if 'las' in extensions:
        points = pointsFromLas(file.file)

    return points

def pointsToLas(interpolatedPoints) -> Iterator[str]:
    outFileAsStr = BytesIO()
    header = laspy.LasHeader(point_format=3, version="1.2")
    header.add_extra_dim(laspy.ExtraBytesParams(name="random", type=np.int32))
    header.offsets = np.min(interpolatedPoints, axis=0)
    header.scales = np.array([0.0001, 0.0001, 0.0001])

    las = laspy.LasData(header)

    las.x = np.array(interpolatedPoints[:, 0])
    las.y = np.array(interpolatedPoints[:, 1])
    las.z = np.array(interpolatedPoints[:, 2])

    las.write(outFileAsStr)

    return iter([outFileAsStr.getvalue()])

def pointsToTxt(interpolatedPoints) -> Iterator[str]:
    outFileAsStr = StringIO()
    np.savetxt(outFileAsStr, interpolatedPoints, '%.5f')

    return iter([outFileAsStr.getvalue()])
