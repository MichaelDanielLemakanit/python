text="software developer"
#used to convert to uppercase the first letter
text1=text.capitalize()

text1=text.capitalize()
print(text)

#upper convert string to uppercase
text2=text.upper()
print(text2)

#casefold
#lower
text3=text.casefold()
print(text3)
text4=text.lower()

#count the number of apperance of a specific character in a string
print(text.count('e'))

#strip() remove all the space....leading and training spaces

text = "     software developer         "
print(len(text))


text="software Developer"

print(text.find('d'))

# .index() returns the index of the first occurence of a character retuns an eeror if the character is not available

print(text.index('D'))

# .replace

text=text.replace('software', 'python')
print(text)
#split a string uysing a specifi character
email="michaellemakanit@gmail.com"
split_email=email.split('@')
print((split_email))
text = "software Developer"
txt=text.split()
print(txt)

text = "    JunIoR DeVeloper"
cleanned_text = text.strip().capitalize()

print(cleanned_text)