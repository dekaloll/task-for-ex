import math
import sys

try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
except IndexError:
    print("Need all 2 arguments with filepath")
    exit(1)

def lenght_between(cycle_x, cycle_y, point_x, point_y):
    lenght = math.sqrt((point_x - cycle_x) ** 2 + (point_y - cycle_y) ** 2)
    return lenght

def out_in_on(lenth, r):
        if length == r:
            return 0
        elif length < r:
            return 1
        else:
            return 2

with open(file1) as file:
    cycle = ([line.rstrip() for line in file])
    try:
        x = float(cycle[0].split(' ')[0])
        y = float(cycle[0].split(' ')[1])
        r = float(cycle[1].split(' ')[0])
        if r < 0:
            raise ValueError

    except ValueError:
        print("Need valid numbers")
        exit(1)


with open(file2) as file:
    point_of_cycle = ([line.rstrip() for line in file])
    i = 0
    for point in point_of_cycle:
        point = point.split(' ')
        try:
            point_x = float(point[0])
            point_y = float(point[1])
        except ValueError:
            print("Not valid numbers")
            continue
        i += 1

        # #проверка диапозона координат точки
        # if math.pow(10,-38) < float(point[0]) and float(point[0]) < math.pow(10, 38):
        #     if math.pow(10,-38) < float(point[1]) and float(point[1]) < math.pow(10, 38):
        #         #решение
        #         length = lenght_between(float(x), float(y), float(point[0]), float(point[1]))
        #         print(out_in_on(length, float(r)))

        # ТЗ по примеру, без проверки диапозона координат точек(как в примере)
        length = lenght_between(x, y, point_x, point_y)
        print(out_in_on(length, float(r)))

        if i > 100:
            break




