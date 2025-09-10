#VARIABEL GLOBAL
x = "Awesome"

def myFunc():
    print("Python is " + x)

myFunc()

#  KATA KUNCI GLOBAL
x = "Awesome"

def myfunc1():
    x = "fantastic"
    print("python is " + x)
    
myfunc1()
print("python is " + x)

