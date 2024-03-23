# Add
def add(n1,n2):
    return n1+n2
# Subtraction
def subtract(n1,n2):
    return n1-n2
# Multiplication
def multiply(n1,n2):
    return n1*n2
# Division
def divide(n1,n2):
    return n1/n2

operations ={"+":add,'-':subtract,'*':multiply,"/":divide}

num1=int(input("What is the first number? "))
num2=int(input("What is the second number? "))
for i in operations:
    print(i)
    
symbol=input("Pick an operation symbol ")
answer=operations[symbol](num1,num2)
print(f"{num1} {symbol} {num2} = {answer}")
