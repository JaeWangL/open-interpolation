from tests.interpolation import interpolation
from tests.load_las import loadFromLas
from tests.load_txt import loadFromTxt
from tests.save_las import saveLasFromPoints
from tests.save_txt import saveTxtFromPoints

def testLas(filePath):
    points = loadFromTxt(filePath)
    points_interpolated = interpolation(points[:, 0], points[:, 1], points[:, 2], showPlot=False)
    saveLasFromPoints(r'./output.las', points_interpolated)

def testTxt(filePath):
    points = loadFromTxt(filePath)
    points_interpolated = interpolation(points[:, 0], points[:, 1], points[:, 2], showPlot=False)
    saveTxtFromPoints(r'./output.txt', points_interpolated)

if __name__ == '__main__':
    testLas(r'./data/xyz_utm58s_no_edge.txt')
    testTxt(r'./data/xyz_utm58s_no_edge.txt')