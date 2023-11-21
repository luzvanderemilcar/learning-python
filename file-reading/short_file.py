filename = "m_inbox.txt"
# create a handle with read permission
try:
    ftext = open(filename, "r")
except:
    print(f"File {filename} Can Not Be Opened !")
    quit()
# for in expression to handle line
keyword = "From:"
count = 0
for line in ftext:
    if line.startswith(keyword):
        count += 1
        print(line.rstrip())
#plural according to count number
if count > 1:
    numerous = "s"
    action_third_person = ""
else: 
    numerous = ""
    action_third_person = "s"
print(f"{count} line{numerous} start{action_third_person} with {keyword}")
    