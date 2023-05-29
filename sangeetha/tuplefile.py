# ordered, unchangeable and it allows duplicate values
#
x=("apple","banana","cherry","apple","mango","cherry")
print(x)
print(x[:3])    # to access the values from the particular index
y=list(x)
y[2]="abcd"     # can convert the tuple in to the list,then change the list and convert it back to the tuple
print(y)
x=("apple","banana","cherry","apple","mango")
y=x*2               # to multiply the content of a tuple in a given number of times
print(y)
y=("1","2","3")       # to join two or more tuples by using "+" operator
z=x+y
print(z)
y=list(x)
y.append("abc")        # to add the item in the tuple
x=tuple(y)
print(x)
y=("orange",)          # to add the items in the tuple
x+=y
print(x)
y=list(x)
y.remove("cherry")       # to remove a particular item from the tuple
x=tuple(y)               # converting tuple in to list and remove the item and convert it back to tuple
print(x)
del x
print(x)                  # this will raise an error because the tuple no longer exist
y=x.index("apple")        # to know the particular index value in a tuple
print(y)
print(len(x))            # to know the length of the given tuple
x=("apple",)             # to create a tuple with one item,you can add a comma after a item
print(x)
x=("apple","1","23","banana","true")   # a tuple can contain different data types
print(x)
print(type(x))                         # to find the data type of a given tuple
x=tuple(("apple","21","mango"))        # using tuple() method to make a tuple
print(x)
fruits=("apple","banana","cherry","apple","mango")

(red,yellow,*blue)=fruits   # if the number  of variables is less than the number of values you  can
                            # add "*" to a variable name and that values will be assigned to a variable as a list
print(red)
print(yellow)
print(blue)
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits    # it allowed to extract the values back in to variable
print(green)
print(yellow)
print(red)


#loops
items=("apple","banana","cherry","apple","mango")
for i in items:
    print(i)
for i in range(len(items)):
    print(items[i])
i=0
while i<len(items):
    print(items[i])
    i+=1
y= x.count("cherry")         # it will return the number of times the value appear in the tuple
print(y)
y=x.index("apple")           # it will return the first occurrence of the value and returns it position
print(y)



