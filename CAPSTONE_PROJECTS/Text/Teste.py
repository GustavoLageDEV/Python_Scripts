
mystring = "A man, a plan, a canal – Panama"
clean_string = []
for char in mystring:
    if char.isalpha():
        clean_string.append(char)

clean_string = "".join(clean_string)

mystring = clean_string.lower()

print(mystring)

print(mystring[::-1])

