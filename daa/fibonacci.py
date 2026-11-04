def iterative(n):
    a, b = 0, 1
    steps = 0
    for _ in range(n):
        a, b = b, a + b
        steps += 1              # One loop-body execution = one step
    return a, steps
def recursive(n):
    if n <= 1:
        return n, 1             # Count this function call
    x, calls_x = recursive(n - 1)
    y, calls_y = recursive(n - 2)
    return x + y, 1 + calls_x + calls_y
if __name__ == "__main__":
    n = int(input("Enter n (0 to 30): "))
    if not 0 <= n <= 30:
        raise SystemExit("Use 0 to 30; naive recursion is slow for large n.")
    series = []
    a, b = 0, 1
    for _ in range(n + 1):
        series.append(a)
        a, b = b, a + b
    print("Series:", series)
    value, steps = iterative(n)
    print(f"Iterative: F({n}) = {value}; loop steps = {steps}")
    value, calls = recursive(n)
    print(f"Recursive: F({n}) = {value}; function calls = {calls}")
