def main():

    number1 = int(input("First Number: "))
    number2 = int(input("Second Number: "))
    
    for operation in operations:
        print(operation)
    operator = input("Choose an operation above: ")
    result = operations[operator](number1, number2)
    print(f"{number1} {operator} {number2} = {result}")

    keep_going = True
    while keep_going: 
        cont_op = input("Continue Operation?: [y/n]")
        if cont_op.lower() == 'y' or cont_op.lower() == 'yes':
            new_result = result
            for operation in operations:
                print(operation)
            new_operator = input("Choose next operation: + - * /: ")
            new_number = int(input("Choose next number: "))
            new_result = operations[operator](result, new_number)
            print(f"{result} {new_operator} {new_number} = {new_result}")
        elif cont_op.lower() == 'n' or cont_op.lower() == 'no':
            new_problem = input("New Problem?: [y/n]")
            if new_problem == 'y' or new_problem == 'yes':
                main()
            else:
                exit()
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2 

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

if __name__ == "__main__":
    main()