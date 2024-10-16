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
mail_content = mail.readline()
print(mail_content)

replaced_TEXT = "[name]"
#
# for new_sample in all_the_names:



