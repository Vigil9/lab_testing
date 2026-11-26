def factorial(n: int) -> int:
    """Повертає факторіал невід'ємного цілого числа n."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_even(n: int) -> bool:
    """Перевіряє, чи є число парним."""
    return n % 2 == 0