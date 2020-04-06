def duplicate(numbers):
    if not numbers:
        return None

    for index, value in enumerate(numbers):
        while index != value:
            if value == numbers[value]:
                return value
            value, numbers[value] = numbers[value], value
    return None
