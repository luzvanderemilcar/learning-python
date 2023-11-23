filename = input("Enter file name : ").strip()
filename_Is_Fine = False
lookup_characters = "@gmail.com"
main_text  = '''
        From: example@gmail.com
        To: example2@gmail.com
        Cc: example3@gmail.com
       '''
characters = input("Enter your search:_ ")
if len(characters.strip()) > 0:
    lookup_characters = characters
try:
    file_handle = open(filename)
    filename_Is_Fine = True
except:
    print(f"File {filename} Can Not Be Opened")
    text_content = input("Paste your text content:_ ")
    if len(text_content.strip()) > 0:
        main_text = text_content
    # quit()
    
    # while loop processing the whole text
    count=0
    index=0
    while index < len(main_text):
        if lookup_characters not in main_text[index:]:
            break
        index = main_text.find(lookup_characters, index) + len(lookup_characters)
        count += 1
    print(f"'{lookup_characters}' is {count} times referenced in\n{main_text}")
    
# For loop processing, line by line
if filename_Is_Fine:
    count = 0
    for line in file_handle:
        if lookup_characters not in line:
            continue 
        count +=1
    print(f"'{lookup_characters}' is {count} times referenced")