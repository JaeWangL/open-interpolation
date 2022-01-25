from tests.interpolation import interpolation
from tests.load_las import loadFromLas
from tests.load_txt import loadFromTxt
from tests.save_las import saveLasFromPoints
from tests.save_txt import saveTxtFromPoints

def testLoadLas():
    loadFromLas(r'./output.las')

def testInterpolate():
    points = loadFromTxt(r'./tests/xyz_utm58s_no_edge.txt')
    points_interpolated = interpolation(points[:, 0], points[:, 1], points[:, 2], showPlot=True)
    saveTxtFromPoints(r'./output.txt', points_interpolated)

if __name__ == '__main__':
    testInterpolate()