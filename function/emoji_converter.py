def emoji_converter(string):
    words = string.split(" ")
    emojis = {
        ":)" : "😀",
        ":(" : "😞"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
    
    
message = input(">")
print(emoji_converter(message))
