def point_in_circle(x, y, a, b, R):
    if (x - a)**2 + (y - b)**2 <= R**2:
        return True
    else:
        return False

a = 0  
b = 0 
R = 5

p1, p2 = 1, 1
f1, f2 = 4, 4
l1, l2 = 0, 6

points = [(p1, p2), (f1, f2), (l1, l2)]
points_inside = 0

for point in points:
    if point_in_circle(point[0], point[1], a, b, R):
        points_inside += 1

print(f"Кількість точок, що лежать всередині кола: {points_inside}")
