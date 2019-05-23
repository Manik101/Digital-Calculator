print("Hello User! This program perform many Mathematical Calculation.\n\n ")

def addition():
    a = input("Enter first number : ")
    b = input("Enter second number : ")
    sum = str(float(a) + float(b))
    print("The sum of given two number is " + sum + ".")

def subtraction():
    a = input("Enter first number : ")
    b = input("Enter second number : ")
    difference = str(float(a) - float (b))
    print("The difference of given two number is " + difference + ".")

def multiplication():
    a = input("Enter first number : ")
    b = input("Enter second number : ")
    product = str(float(a) * float(b))
    print("The product of given two number is " + product + ".")

def division():
    a = input("Enter dividend : ")
    b = input("Enter divisor : ")
    divide = str(float(a)/float(b))
    print("The answer is" + divide + ".")

def square():
    a = input("Enter the number : ")
    b = str(float(a) * float(a))
    print("The square of the given number is " + b  + ".")

def cube():
    a = input("Enter the number : ")
    b = str(float(a) * float(a) * float(a))
    print("The cube of the given number is " + b + ".")

def sqroot():
    a = input("Enter the number : ")
    b = str(sqroot(a))
    print("The square root of given number is " + b + ".")

def curoot():
    a = input("Enter the number : ")
    b = str(curoot(a))
    print("The cube root of the given number is " + b + ".")


print("Insert:"
      "\n A or + for Addition                       B or - for Subtraction"
      "\n C or * for Multiplication                 D or / for Division"
      "\n S to square the number                    Cu to cube the number"
      "\n E to put the number in square root        F to put the number in cube root\n")
X = input("")
if X.upper() == "A" or X == "+":
    addition()

elif X.upper() == "B" or X == "-":
    subtraction()

elif X.upper() == "C" or X == "*":
    multiplication()

elif X.upper() == "S":
    square()

elif X.upper() == "CU":
    cube()

elif X.upper() == "E":
    sqroot()

elif X.upper() == "F":
    curoot()

else:
    print("Invalid Data Entered.")




