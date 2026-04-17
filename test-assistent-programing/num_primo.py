"""Module for prime number verification."""


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    A prime number is a natural number greater than 1 that has no positive 
    divisors other than 1 and itself.
    
    Args:
        n: The number to check.
        
    Returns:
        True if the number is prime, False otherwise.
        
    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
    """
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
    """Run test cases for the is_prime function."""
    test_cases = [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (1, False),
        (0, False),
    ]
    
    print("Testing is_prime function:")
    for number, expected in test_cases:
        result = is_prime(number)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_prime({number}): {result} (expected: {expected})")


def get_user_number() -> int:
    """Prompt the user until a valid integer is entered."""
    while True:
        user_input = input("Digite um número inteiro: ")
        try:
            return int(user_input)
        except ValueError:
            print("Entrada inválida. Por favor, informe um número inteiro válido.")


def main() -> None:
    """Prompt the user and print whether the number is prime."""
    number = get_user_number()
    if is_prime(number):
        print(f"O número {number} é primo.")
    else:
        print(f"O número {number} não é primo.")


if __name__ == "__main__":
    main()