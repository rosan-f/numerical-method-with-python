def f(x): return x**3 - 2*x - 5
def df(x): return 3*x**2 - 2

x0 = 2
tol = 1e-3

while True:
    x1 = x0 - f(x0)/df(x0)
    galat = abs((x1 - x0)/x1)
    print(f"x = {x1:.6f}, f(x) = {f(x1):.6f}, galat = {galat:.6f}")
    if galat < tol:
        break
    x0 = x1

print(f"Akar hampiran = {x1:.6f}")
