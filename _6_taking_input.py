# val = input("Enter your name: ")

# print("Entered name: "+ val)

#getting input and get type

# input1 = input("Enter your your input :")

# print(type(input1))

#taking input and making sum type casting
# num1 = int(input("Enter number1 : "))
# num2 = int(input("Enter number2 : "))

# print(num1 + num2)

#taking input and type casting to float

# float1 = float(input("Enter number1 : "))
# float2 = float(input("Enter number2 : "))

# print(float1 + float2)

#string is default input

#taking multiple inputs at a time 
# x,y= input("Enter two values : ").split()
# print(x,y)

#taking three input at a time
# x,y,z= input("Enter three values : ").split()
# print(x,y,z)
#printing with format
# print("x is : {} , y is : {} , z is : {}".format(x,y,z))

# taking multiple input at a time
# and type casting them using list
# x = list(map(int,input("Enter number with spaces : ").split()))
# print(x)

# Fusing list comprehension
x = [int(x) for x in input("Enter number with spaces : ").split()]
print(x)

