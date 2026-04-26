"""Module for prime number verification."""


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def run_tests() -> None:
    test_cases = [
        (2, True),
        (3, True),
        (4, False),
    ]
    
    for number, expected in test_cases:
        result = is_prime(number)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_prime({number}): {result} (expected: {expected})")


if __name__ == "__main__":
    run_tests()