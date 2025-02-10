import math
def reg_pol_area(sides = int, side_lenght = float):
    return  sides * (side_lenght**2) * (1/(4*math.tan(math.pi/sides)))

print(reg_pol_area(4,3))