x = 10
y = 20

print(x)
print(x*2)

if x > y :
    print(x, "is greater than ", y)
else:
    print("y is greater than", x)
    #print(" y is greater than x")

message="Hello World!"

print(message)

print(type (x))
print(type (message))

def myfun() :
    global var
    var = 60
    print (var)

myfun()
print(var)