from tests.interpolation import interpolation
from tests.load_txt import loadFromTxt
from tests.save_las import saveLasFromPoints

def main():
    points = loadFromTxt(r'./tests/xyz_utm58s_no_edge.txt')
    points_interpolated = interpolation(points[:, 0], points[:, 1], points[:, 2],  showPlot=True)
    saveLasFromPoints(r'./output.las', points_interpolated)

if __name__ == '__main__':
    main()