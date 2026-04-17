from typing import Iterable, Tuple


def summarize_numbers(numbers: Iterable[float]) -> Tuple[float, float, float, float]:
    """Return sum, average, maximum, and minimum values for a sequence of numbers."""
    values = list(numbers)
    if not values:
        raise ValueError("The sequence must contain at least one number.")

    total = sum(values)
    average = total / len(values)
    maximum = max(values)
    minimum = min(values)

    return total, average, maximum, minimum


if __name__ == "__main__":
    sample_values = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, maximum, minimum = summarize_numbers(sample_values)

    print("total:", total)
    print("media:", average)
    print("maior:", maximum)
    print("menor:", minimum)
