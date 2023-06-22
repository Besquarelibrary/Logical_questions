# which is ordered,changeable and it does not allow duplicates

num={"1":"name","2":"abc","3":"def","4":"mango"}
num.update({"3":"apple"})
print(num)
x=num.get("1")                 # to get the value for a particular key
print(x)
num[4]="apple"                 # to update the key value for a particular key
print(num)

# to remove items(pop,popitem,del,clear)
num.popitem()                  # to remove the last item from the dictionary
print(num)
num.pop("3")                   # to remove the particular item from the dictionary
print(num)
del num["2"]                   # to delete a particular item from the dict
print(num)
num.clear()                    # this method empties the dict
print(num)

# to copy the items (copy,dict)
# num2=num.copy()                # to make copy of dictionary
# print(num2)
# num2=dict(num)                 # another inbuilt method to copy a dictionary
# print(num2)
# x=('key1','key2','key3')
# y=0
# num=dict.fromkeys(x,y)         #fromkeys method returns a dict with specified keys and specified values
# print(num)
# num=dict.fromkeys(x)           #the default values is none
# print
num={"1":"name","2":"abc","3":"def","4":"mango"}
x=num.get("2")                 # to get a particular key value from the dict
print(x)
                                 #which returns a list containing a tuples for each key value pair
x=num.items()                  #the key-value pairs of a dictionary as tuples in a list
print(x)
x=num.keys()                   #to return the keys
print(x)
x= num.setdefault("2","5")     #returns the value of a specified key
print(x)
x=num.setdefault("8","apple")  #if the value does not exist this value become the key value
print(x)
print(num)
x=num.values()                 # returns the list of all values in the dictionary
print(x)
child1={"name":"abc","age":"2"}  # nested dictionary
child2={"name":"def","age":"5"}  # a dictionary can contain dictionaries
child3={"name":"ghi","age":"8"}
child4={"name":"jkl","age":"10"}
new={"child1":child1,"child2":child2,"child3":child3}
print(new)
for i in num:
    print(i,end=" ")
for i in num:
    print(num[i])
for i in num.values():              # to returns the values of dictionary
    print(i)
for i in num.keys():                  # to returns the keys of dictionary
    print(i)






