print("----Simple Calculator----")
num1=float(input("Enter your first number"))
num2=float(input("Enter your second number"))
operator=input("Choose operators (+,-,*,/) :")
if operator == "+":
    print("Result:",num1+num2)
elif operator == "-":
    print("Result:",num1-num2)
elif operator =="*":
    print("Result:",num1*num2)
elif operator =="/":
    if num2 ==0:
        print("zeroError: cannot divisible by zero")
    else:
        print("Result:",num1/num2)
else:
    print("Invalid operator")
