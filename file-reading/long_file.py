filename = "m_inbox.txt"
keyword = "From:"
# create a handle with read permission
try:
    ftext = open(filename, "r")
    # Read file as a whole long string
    long_text = ftext.read()
except:
    print(f"File {filename} Can Not Be Opened !")
    quit()
    
# while loop to handle string processing
count=0
index=0
while index < len(long_text):
    if keyword not in long_text[index:]:
        break
    index = long_text.find(keyword, index) + len(keyword)
    count += 1
print(f"'{keyword}' is {count} times referenced in\n{long_text}"