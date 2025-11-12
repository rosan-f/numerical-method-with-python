import math

def f(x): return math.log(x) + x**2 - 4
def df(x): return (1/x) + 2*x

x0 = 1.5
tol = 1e-4

while True:
    x1 = x0 - f(x0)/df(x0)
    galat = abs((x1 - x0)/x1)
    print(f"x = {x1:.6f}, f(x) = {f(x1):.6f}, galat = {galat:.6f}")
    if galat < tol:
        break
    x0 = x1

print(f"Akar hampiran = {x1:.6f}")
