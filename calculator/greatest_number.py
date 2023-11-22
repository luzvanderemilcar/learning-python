# Find the largest number in a Set
number_list = [12, 34, 23, 2, 0, 5, 25]
def find_max(list):
    largest_number_processed = None
    for number in list:
        if largest_number_processed is None or number > largest_number_processed:
            largest_number_processed = number
    return largest_number_processed
number = find_max(number_list)
print(number)
