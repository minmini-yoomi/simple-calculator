def logical_calculator():
    number1 = int(input("enter the first number: "))
    number2 = int(input("enter the second number: "))  # logical operations takes ONLY int value
    Logical_Op = input("enter the operation you want to perform(AND & - OR | - XOR ^): ")
    result = None
    if Logical_Op.upper() == "OR" or Logical_Op == "|":
        result = number1 | number2
    elif Logical_Op.upper() == "XOR" or Logical_Op == "^":
        result = number1 ^ number2
    elif Logical_Op.upper() == "AND" or Logical_Op == "&":
        result = number1 & number2
    else:
        print("INVALID INPUT!")
    print(f"The result is: {result}")