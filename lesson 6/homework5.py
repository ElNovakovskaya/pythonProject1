from myfuncion import perim
from myfuncion import get_int_from_user

print("Длины сторон треугольника:")
a = get_int_from_user("a = ")
b = get_int_from_user("b = ")
c = get_int_from_user("c = ")

perim(a, b, c)


print(f'My file name is {__name__}')