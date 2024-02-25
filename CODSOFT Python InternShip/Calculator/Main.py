from Simple_Calculator import Calculator, wait_for_keypress, clear_screen


def main():  # Main Method
    calculator = Calculator()
    get_input = True
    num1 = num2 = 0
    while True:
        if get_input:
            print("Welcome to the Calculator")
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
        operation = str(input("Enter operation( + , - , / , * ): "))
        result = 0
        while operation != '+' or operation != '-' or operation != '/' or operation != '*':
            if operation == "+":
                result = calculator.addition(num1, num2)
                break
            elif operation == "-":
                result = calculator.subtraction(num1, num2)
                break
            elif operation == "/":
                result = calculator.division(num1, num2)
                break
            elif operation == "*":
                result = calculator.multiplication(num1, num2)
                break
            else:
                print("Invalid operation")
                operation = str(input("Enter operation( + , - , / , * ): "))
        print(f"{num1} {operation} {num2} = {result}")
        wait_for_keypress()
        clear_screen()

        get_input = True
        while True:
            print("Now what do you want to do: ")
            print("1. Continue with this calculation")
            print("2. Start new calculation")
            print("3. Show calculation history")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                while True:
                    print("Take result as: ")
                    print("1. 1st number")
                    print("2. 2nd number")
                    print("3. None")
                    print("4. Exit")
                    choice_1 = int(input("Enter your choice: "))
                    if choice_1 == 1:
                        num1 = result
                        num2 = float(input("Enter 2nd number: "))
                        get_input = False
                        break
                    elif choice_1 == 2:
                        num2 = result
                        num1 = float(input("Enter 1st number: "))
                        get_input = False
                        break
                    elif choice_1 == 3:
                        break
                    elif choice_1 == 4:
                        print("Exiting...")
                        return
                if not get_input:
                    break
            elif choice == 2:
                calculator.history.append("---------------------")
                break
            elif choice == 3:
                calculator.show_history()
                continue
            elif choice == 4:
                calculator.history.append("---------------------")
                print("Thank you for using Calculator")
                print("Exiting...")
                return


if __name__ == "__main__":
    main()



