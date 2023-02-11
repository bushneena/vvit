a = float(input(""))
b = float(input(""))
c = float(input(""))
d = b * b - 4 * a * c
if d < 0:
    print("Corney net")
if d == 0:
    print("X = ", (-b / 2 / a))
if d > 0:
    print("X1 = ", ((-b + d ** 0.5) / 2 / a))
    print("X2 = ", ((-b - d ** 0.5) / 2 / a))