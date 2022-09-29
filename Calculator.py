import Calculate

num1 = input("Enter First Num: ")
num2 = input("Enter Second Num: ")
num1 = int(num1)
num2 = int(num2)
print("1. Sum")
print("2. Substraction")
print("3.Multiple")
print("4. Divide")
switch = input("calculate: ")
switch = int(switch)
match switch:
    case 1:
        print(f"Sum Result: ")
        Calculate.function_sum(num1, num2)
    case 2:
        print(f"Substraction Result: ")
        Calculate.function_substraction(num1, num2)
    case 3:
        print(f"Multiple Result: ")
        Calculate.function_multiple(num1, num2)
    case 4:
        print(f"Divide Result: ")
        Calculate.function_divide(num1, num2)
