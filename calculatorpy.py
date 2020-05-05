#this a simple program to make a calculator 
print("*********************************************calculator by prs***********************************************************")
while True :
    print("select operation :")
    print("***********************************************")
    print("\n"*2)
    print("1.add :")
    print("***********************************************")
    print("\n"*1)
    print("2.subtract:")
    print("***********************************************")
    print("\n"*1)
    print("3.multiply :")
    print("***********************************************")
    print("\n"*1)
    print("4.divide :")
    print("***********************************************")
    print("\n"*1)
    print("5. square :")
    print("***********************************************")
    print("\n"*1)
    print("6. squareroot :")
    print("***********************************************")
    print("\n"*1)
    print("7. cube :")
    print("***********************************************")
    print("\n"*1)
    print("8. cuberoot :")
    print("***********************************************")
    print("\n"*1)
    print("9. to evaluate a simple mathematical expresion ")
    print("***********************************************")
    x = int(input( "enter your choice (1/2/3/4/5/6/7/8/9)"))
    
# function to add 2 numbers
    if x == 1 :
        def add() :
            num1 = int(input("enter the  first number :"))
            num2 = int(input("enter the second number :"))

            num3 = num1 + num2
            print(num1,"+",num2,"=", num3)
        add()

        

# function to subtract 2 numbers 
    elif x == 2 :
        def subtract() :
            num1 = float(input("enter the first number : "))
            num2 = float(input("enter the second number :"))
            num3 = num1 - num2 
            print(num1,"-",num2,"=",num3)
        subtract()

# function to multiply 2 numbers
    elif x == 3 :
        def multiply() :
            num1 = float(input("enter the first number : "))
            num2 = float(input("enter the second number :"))
            num3 = num1 * num2
            print(num1,"*",num2,"=",num3)
        multiply()

# function to divide 2 numbers
    elif x == 4 :
        def divide() :
            num1 = float(input("enter the first number : "))
            num2 = float(input("enter the second number :"))
            num3 = num1 / num2
            print(num1,"/",num2,"=",num3)
        divide()

# function to calculate square of a number
    elif x == 5 :
        def square() :
            num1 = float(input("enter the number : "))
            num2 = num1 ** 2
            print("square of ",num1,"=",(num2))
        square()

#function to calculate  squareroot of  a number
    elif x == 6 :
        def squareroot() :
            num1 = float(input("enter the number : "))
            num2 = num1 ** 0.5
            print("square root of ",num1,"=",(num2))
        squareroot()

# function to calculate cube of a number
    elif x == 7 :
        def cube() :
            num1 = float(input("enter the  number : "))
            num2 = num1 ** 3
            print("cube of ",num1,"=",(num2))
        cube()
# function to calculate cuberoot of a number
    elif x == 8 :
        def cuberoot() : 
            num1 = float(input("enter the number : "))
            num2 = num1 **(1/3)
            print("cuberoot of ",num1,"=",(num2))
        cuberoot()
    elif x == 9 :
        num1 = eval(input("enter the expression"))
        print(num1)
    else :
        print("invalid input \n")
    print("************************************thank you - prs**************************************")
    print("\n"*3)

    


























