def bmi_calculator():
    length = (input("enter your length: "))
    if length[1] == ".":
        length = float(length)
    else:
        length = (float(length)) * 0.01
    weight = float(input("enter your weight: "))
    BMI = (weight / (length ** 2))
    print(f"Your BMI is: {BMI} kg/m^2")
    if BMI < 18.5:
        print("you're too slim! go eat bro")
    elif 18.5 <= BMI < 25:
        print("normal weight ^-^")
    elif 25 <= BMI < 30:
        print("you're fat '-'")
    elif 30 <= BMI < 35:
        print("you're fat fat bro")
    elif 35 <= BMI < 40:
        print("Stop eating bro ! you're too fat ")
    elif BMI > 40:
        print("fat ass '-'.")