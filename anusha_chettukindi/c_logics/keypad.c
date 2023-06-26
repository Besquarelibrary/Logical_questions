QUESTION:
WRITE THE PROGRAM FOR KEYPAD WHICH WHEN USER WANTS TO SEND A MESSAGE WHAT DIGITS NEED TO BE SELECTED ON THE KEYPAD

PROGRAM IN C:

keypad = {
    "abc": "222",
    "def": "333",
    "ghi": "444",
    "jkl": "555",
    "mno": "666",
    "pqrs": "7777",
    "tuv": "888",
    "wxyz": "9999"
}
#read the input string from user
string=input("enter string")
#empty string to store the numeric value of every character
new_str=""
#iterate string
for chr in string:
    #read key and value from dict items
    for key,value in keypad.items():
        #iterate every key in dict
        for ele in range(len(key)):
            #check char exist in the key
            if chr==key[ele]:
                #add the digit value which belongs to character in string 
                new_str=new_str+value[0:ele+1:1]
#print the resultant string with digits
print(new_str)

OUTPUT:
enter string anusha
anusha
266887777442