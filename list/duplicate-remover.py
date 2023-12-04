my_list = [0, 3, 5, 6, 7, 5, 3, 5, 8, 9]
new_list = []
for item in my_list:
    if item in new_list:
        continue
    else:
        new_list.append(item)
print(new_list)