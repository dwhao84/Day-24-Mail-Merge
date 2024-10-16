#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
# for name in names:
all_the_names = []
# 找到Absolute File Path.
names = open("/Users/haodawei/Library/Mobile Documents/com~apple~CloudDocs/PyCharm Projects/Day-24-Mail-Merge/Input/Names/invited_names.txt", "r")
print(names.readline())

# for-Loop整個names。
for name in names:
    name = name.strip()
    print(name)
    all_the_names.append(name)

# 得到 ['Zuko', 'Appa', 'Katara', 'Sokka', 'Momo', 'Uncle Iroh', 'Toph']
print(all_the_names)

# 把all_the_names的內容 取代 starting_letter.txt。
mail = open("/Users/haodawei/Library/Mobile Documents/com~apple~CloudDocs/PyCharm Projects/Day-24-Mail-Merge/Input/Letters/starting_letter.txt", "r")
mail_content = mail.read()
print(mail_content)

replaced_TEXT = "[name]"

# saved data.
for i in all_the_names:
    revised_content = mail_content.replace(replaced_TEXT, i)
    print(revised_content)
    # Write each data by using mode w to saved it into the new file.
    with open(f"./Output/ReadyToSend/letter_for_{ i }.docx",mode="w") as completed_letter:
        completed_letter.write(revised_content)

