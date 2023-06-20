# Take a string for checking given string pangram or not
string="The quick brown fox jumps over the lazy dog"
# Taking an empty string to store only alphabets from given string
string_new=''
# iterate the string to find alphabets and add into new empty string
for i in string:
# comparing i character is alphabet or not
    if i.isalpha():
        string_new +=i
# taking all alphabets into lower case
string_lower=string_new.lower()
# Taking the set for each character unique
unique_characters=set(string_lower)
# Comparing length unique_characters with  alphabets constant length 26
if len(unique_characters)==26:
    print("Given string is Pangram")
else:
    print("Given string is non Pangram")