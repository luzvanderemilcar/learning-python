def find_max(numbers):
    max_processed = numbers[0]
    for num in numbers:
        if num > max_processed:
            max_processed = num
    return max_processed


