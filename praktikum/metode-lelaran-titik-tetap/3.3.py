def g(x):
    return (-x**3 + 3) / 6

def fixed_point(g, x0, eps=1e-6, max_iter=20):
    print(f"\n=== x0 = {x0} ===")
    print(f"{'r':<3}{'x_r':<15}{'x_(r+1)':<15}")
    for r in range(max_iter):
        x1 = g(x0)
        print(f"{r:<3}{x0:<15.6f}{x1:<15.6f}")
        if abs(x1 - x0) < eps:
            print(f"\nHampiran akar = {x1:.6f} (konvergen)\n")
            return
        x0 = x1
        if abs(x0) > 1e6:
            print("\nNilai terlalu besar  divergen!\n")
            return
    print("\nBelum konvergen setelah iterasi maksimum.\n")

x0_values = [0.5, 1.5, 2.2, 2.7]

for x0 in x0_values:
    fixed_point(g, x0)
