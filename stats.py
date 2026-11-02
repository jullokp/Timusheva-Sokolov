def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return {
        "sum": total,
        "average": average,
        "min": min(numbers),
        "max": max(numbers),
    }


if __name__ == "__main__":
    print(calculate_stats([1, 2, 3, 4, 5]))
