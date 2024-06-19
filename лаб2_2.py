import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

a1 = float(input("Введіть перший катет першого трикутника: "))
b1 = float(input("Введіть другий катет першого трикутника: "))
a2 = float(input("Введіть перший катет другого трикутника: "))
b2 = float(input("Введіть другий катет другого трикутника: "))

hypotenuse1 = hypotenuse(a1, b1)
hypotenuse2 = hypotenuse(a2, b2)

if hypotenuse1 > hypotenuse2:
    print(f"Гіпотенуза першого трикутника ({hypotenuse1}) більша за гіпотенузу другого ({hypotenuse2})")
elif hypotenuse1 < hypotenuse2:
    print(f"Гіпотенуза другого трикутника ({hypotenuse2}) більша за гіпотенузу першого ({hypotenuse1})")
else:
    print(f"Гіпотенузи обох трикутників однакові ({hypotenuse1})")
