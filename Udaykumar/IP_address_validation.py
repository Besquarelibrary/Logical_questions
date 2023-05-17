# To validate IP address between 0.0.0.0 to 255.255.255.255

# Input String
My_str = input("Enter IP:")

# Using try & exception to valid code crash for errors
try:
    # Dividing given string into list using split method
    values = My_str.split('.')
    # Comparing each list element value with min & max range if length of list equal to 4
    valid = all(0 <= int(ele) < 256 for ele in values) if len(values) == 4 else False
    # printing the output
    print(f"{My_str} -- Is a Valid IP" if valid else f"{My_str} -- Is a Invalid IP")

# except block will be executed when try block fail
except:
    print("Data Type Error Arrived!")

# Finally block will be executed for without any restrictions to indicate end of the process..
finally:
    pass

