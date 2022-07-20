
def main():
    number1 = int(input("First Number: "))
    operator = input("+\n-\n*\n/\n")
    number2 = int(input("Second Number: "))
    print(calc(number1, operator, number2))

def calc(num1, operator, num2):
    if operator == '+':
        return num1 + num2

    elif operator == '-':
        return num1 - num2

    elif operator == '*':
        return num1 * num2

    elif operator == '/':
        return num1 / num2
    
if __name__ == "__main__":
    main()