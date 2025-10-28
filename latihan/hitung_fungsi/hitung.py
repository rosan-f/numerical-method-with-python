def rumus1(x):
    return ((-x**3) + 3) / 6

def rumus2(x_lama, x_baru):
    return abs((x_baru - x_lama) / x_baru)

def rumus3(x):
    return (2 * x**2) + (3 * x) - 4

def rumus4(a, b):
    return (a + b) / 2

def rumus5():
    a, b, c = 2, 3, -4
    D = b**2 - 4*a*c
    if D < 0:
        return "tidak ada akar riil"
    akar1 = (-b + D**0.5) / (2*a)
    akar2 = (-b - D**0.5) / (2*a)
    return akar1, akar2

print("Rumus 1:", rumus1(1))
print("Rumus 2:", rumus2(0.8, 1.0))
print("Rumus 3:", rumus3(1))
print("Rumus 4:", rumus4(0, 2))
print("Rumus 5:", rumus5())
