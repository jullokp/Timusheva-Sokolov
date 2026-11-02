def calculate_stats(numbers):
    if not numbers:
        return None

    total = sum(numbers)
    average = total / len(numbers)

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    variance = sum((x - average) ** 2 for x in numbers) / n
    std_dev = variance ** 0.5

    return {
        "sum": total,
        "average": average,
        "min": min(numbers),
        "max": max(numbers),
        "median": median,
        "std_dev": std_dev,
    }


if __name__ == "__main__":
    print(calculate_stats([1, 2, 3, 4, 5])) #вывод
    print(calculate_stats([]))  # None

