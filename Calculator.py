import Calculate

num1 = input("Enter First Num: ")
num2 = input("Enter Second Num: ")
num1 = int(num1)
num2 = int(num2)
print("1. Sum")
print("2. substraction")
print("3. multiple")
print("4. divide")
switch = input("calculate: ")
switch = int(switch)
match switch:
    case 1:
        Calculate.function_sum(num1, num2)
    case 2:
        Calculate.function_substraction(num1, num2)
    case 3:
        Calculate.function_multiple(num1, num2)
    case 4:
        Calculate.function_divide(num1, num2)
