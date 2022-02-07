import os.path
import numpy as np
from fastapi import UploadFile
from typing import IO

def checkValidExtensions(filename: str) -> bool:
    extensions = os.path.splitext(filename)[1]
    validExtensions = ['txt', 'las']
    
    return any(x in extensions for x in validExtensions)

def pointsFromTxt(file: IO, delimiter=' '):
    points = np.loadtxt(file, delimiter=delimiter)

    return points

def readPointsFile(file: UploadFile):
    extensions = os.path.splitext(file.filename)[1]
    if 'txt' not in extensions:
        return None

    points = pointsFromTxt(file.file)

    return points
