filename = input("Enter file name : ").strip()
is_Fine = False
lookup_characters = "@gmail.com"
default_text  = '''
        From: example@gmail.com
        To: example2@gmail.com
        Cc: example3@gmail.com
       '''
characters = input("Enter the your search:_ ")
if len(characters.strip()) > 0:
    lookup_characters = characters
try:
    file_handle = open(filename)
    is_Fine = True
except:
    print(f"File {filename} Can Not Be Opened")
    text_content = input("Paste here your text content:_ ")
    if len(text_content.strip()) > 0:
        default_text = text_content
    # quit()
    
    count=0
    index=0
    while index < len(default_text):
        if lookup_characters not in default_text[index:]:
            break
        index = default_text.find(lookup_characters, index) + len(lookup_characters)
        count += 1
    print(f"'{lookup_characters}' is {count} times referenced in\n{default_text}")
    
# For loop for processing
if is_Fine:
    count = 0
    for line in file_handle:
        if lookup_characters not in line:
            continue 
        count +=1
    print(f"'{lookup_characters}' is {count} times referenced")