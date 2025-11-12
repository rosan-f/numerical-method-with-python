import math

def fixed_point(g, x0, eps=1e-6):
    i = 0
    while True:
        x1 = g(x0)

        if abs(x1) > 1e6:
            print(f"Iterasi {i}: x = {x0:.6f}  divergen (nilai terlalu besar)\n")
            break

        selisih = abs(x1 - x0)
        print(f"Iterasi {i}: x = {x0:.6f}, |x1 - x0| = {selisih:.6f}")
        if selisih < eps or i > 100:
            break
        x0 = x1
        i += 1
    print(f"Hampiran akar = {x1:.6f}\n")

# (a) x = sqrt(2x + 3)
def g_a(x):
    return math.sqrt(2 * x + 3)

# (b) x = 3 / (x - 2)
def g_b(x):
    return 3 / (x - 2)

# (c) x = (x^2 - 3) / 2
def g_c(x):
    return (x**2 - 3) / 2


print("=== (a) x = sqrt(2x + 3) ===")
fixed_point(g_a, 4)

print("=== (b) x = 3 / (x - 2) ===")
fixed_point(g_b, 4)

print("=== (c) x = (x^2 - 3) / 2 ===")
fixed_point(g_c, 4)
