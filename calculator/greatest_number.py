# Find the largest number in a Set
number_list = [12, 34, 23, 2, 0, 5, 25]
def find_max(list):
    largest_number = None
    for number in list:
        if largest_number is None or number > largest_number:
            largest_number = number
    return largest_number
number = find_max(number_list)
print(number)

