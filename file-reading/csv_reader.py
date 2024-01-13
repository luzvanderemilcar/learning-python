filename = input("Enter csv file name : ").strip()
filename += ".csv"
separator = ","
filename_Is_Fine = False

 # Open the file  
try:
    file_handle = open(filename)
    filename_Is_Fine = True
except:
    print(f"File {filename} Can Not Be Opened")
    quit()

# For loop processing, line by line
if filename_Is_Fine:
    data_array = []
    for line in file_handle:
        data-row = line.split(separator)
        data_array.append(data-row)
    
    header_row = data_array[0]
    data_rows = data_array[1:]
    
    # list to object conversion 
    data_objects_array = []
    i = 0
    for data in data_array:
        j = 0
        for key in header_row:
            data_objects_array[i][key] = data[j]
            j++
        i++    
        
    