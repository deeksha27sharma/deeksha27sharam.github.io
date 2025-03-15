from Calculator_art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


operation={
    '+':add,
    '-':sub,
    '*':mult,
    '/':div,
}

def calculator():
    should_accumulate = True
    num1=float(input("what is the first number:"))

    while should_accumulate:
        for symbol in operation:
            print(symbol)
        operand=input("pick an operation to perform")
        num2=float(input("what is the next number:"))
        result=operation[operand](num1,num2)
        print(f"{num1}  {operand}  {num2} = {result}")

    # should_continue=True
    # while should_continue==True :
        choice=input(f"Type 'y' to continue working with {result}, or type 'n' to start a new calculation" ).lower()
        if choice=="y":
            num1=result
        else:
            should_accumulate=False
            print("\n"*20)
            calculator()

calculator()


