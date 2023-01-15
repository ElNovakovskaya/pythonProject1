

print("Длины сторон треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))



if a + b > c and b + c > a and a + c > b:
   print("True")
else:
   print("False")

#param_triangle()
P = (a + b + c)
p = (a + b + c) / 2
s = pow(p * (p - a) * (p - b) * (p - c), 1 / 2)

print(f"Площадь треугольника со сторонами {a}, {b}, {c} составляет: {s}, периметр составляет:{P}")

else:
   print(f"Треугольник со сторонами {a}, {b}, {c} существовать не может")

