# 1 Variable Declaration and Types

a=15
b=12
print(type(a))
print(type(b))

# 2 Basic Arthmetic Operations

print ("Sum=", a+b)
print ("Difference=", a-b)
print ("Product=", a*b)
print ("Dividend=", a/b)

# 3 Using Variables and Type Casting

c=a//b #double // changes integers to float
print ("Value of c=", c)
print("type of c", type(c))

c_float = float(c) #Changing Integer c to Float c
print("New value=", c_float)
print("Type of new value=", type(c_float))

# 4 Working with strings

message="The result of a divided by b is:"
message_with_c = message +  " " + str(c) #Concatenating the message with the value of c
print(message_with_c)

# 5 Using Comparison operators

if a > b:
    print("True")
else:
    print("False")
if a==b:
    print("True")
else:
    print("False")

