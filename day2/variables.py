# prints the value of message to the console
message = "Hello, World!"
print(message)

## output
# Hello, World!


# long and descriptive variable names
secret_message = "Hey, here is my secret"
print(secret_message)

## output
# Hey, here is my secret


# Declare multiple variables in a single line
# doing it the conventional way
name = "Prince"
age = 12
hobby = "Swimming"
print("Name:", name, " Age:", age, " Hobby: ", hobby)

# doing it the Python way
my_name, my_age, my_hobby = "Prince", 12, "Swimming"
print("Name:", my_name, " Age:", my_age, " Hobby: ", my_hobby)

## output
# Name: Prince  Age: 12  Hobby:  Swimming
# Name: Prince  Age: 12  Hobby:  Swimming



# Reassigning variables
my_age = 20
print(my_age)

# reassign the value of my_age
my_age = 21
print(my_age)

## output
#20
#21


# Operations on variables
PI = 3.142857143
radius = 44
perimeter = 2 * PI * radius
print(perimeter)

## output
# 276.571428584


# String operations
msg1 = "Hello"
msg2 = "World"
full_msg = msg1 + msg2
print(full_msg)

## output
# HelloWorld

# String operations
fav_language = "Python"
output = fav_language * 5
print(output)

## output
# PythonPythonPythonPythonPython


# Variable scope
# local variable
def some_function():
    my_real_age = 19
    print(my_real_age) # my_real_age is locally available inside some_function

some_function()
print(my_real_age) # my_real_age is not available outside the function 

## output
# 19
# NameError: name 'my_real_age' is not defined

# global variable
def some_function():
    global my_real_age
    my_real_age = 19 # globally available throughout this program
    print(my_real_age) 

some_function()
print(my_real_age) # my_real_age is now available outside the some_function 

## output
# 19
# 19

























