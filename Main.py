def secant_method(f, x1, x2, tolerance=1e-10, max_iterations=100):
    iteration = 0
    while True:
        fx1 = f(x1) 
        fx2 = f(x2)
        x_new = x2 - fx2 * (x2 - x1) / (fx2 - fx1)
        iteration += 1
        print(f"Iteration {iteration}: x = {x_new}")
        if abs(fx2) < tolerance or iteration >= max_iterations:
            break
        x1, x2 = x2, x_new
    return x_new

def main():
    # Input function f(x)
    expression = input("Enter the function f(x) in Python syntax (e.g., 'x**2 - 2*x - 5'): ")
    f = lambda x: eval(expression)
    
    # Input initial guesses
    x1 = float(input("Enter initial guess 1 (x1): "))
    x2 = float(input("Enter initial guess 2 (x2): "))
    
    # Call secant method
    root = secant_method(f, x1, x2)
    print("Approximately", root)

if __name__ == "__main__":
    main()