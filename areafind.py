from math import pi
from random import *

ci = 0
a = 0
x = random()
y = random()

for i in range(10000):
    if (x*x) + (y*y) < 1:
        ci += 1
    a += 1

    x = random()
    y = random()

print(pi / 4, ":", 1, " ≒ ", ci, ":", a)
print("원 안의 점 갯수 나와야하는 값 : ",(pi / 4) * a)
print(ci / a * 4)
print("파이 : ", pi)
