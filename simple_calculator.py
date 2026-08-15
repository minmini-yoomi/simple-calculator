print("Press X to exit")
def check_x(inp : str):
    if inp.upper()=='X':
        print("Exit")
        return None
    else:
        return inp
def to_float(num):
    try:
        return float(num)
    except ValueError:
        print("ERROR: You must enter a number.")
        return None
exit_flag = False
while True :
    num1 = None
    num2 = None
    res = None
    while num1==None:
        num1 = input("number 1: ")
        if not check_x(num1):
            exit_flag = True
            break
        num1 = to_float(num1)
    if exit_flag : break
    operate = input("the operation (+ , - , * , /): ")
    if not check_x(operate): break
    while num2 == None:
        num2 = input("number 2: ")
        if not check_x(num2):
            exit_flag= True
            break
        num2 = to_float(num2)
    if exit_flag : break

    if operate == "+":
        res = num1 + num2
    elif operate == "-":
        res = num1 - num2
    elif operate == "*":
        res = num1 * num2
    elif operate == "/":
        if num2 != 0:
            res = num1 / num2
        else:
            print("ERROR: Division by zero is not allowed")
    else:
        print("INVALID INPUT")
    print("the result is: ", res)
