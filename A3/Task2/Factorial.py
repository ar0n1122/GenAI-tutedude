def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    try:
        factorial(-3)
    except ValueError as e:
        assert str(e) == "Factorial is not defined for negative numbers."