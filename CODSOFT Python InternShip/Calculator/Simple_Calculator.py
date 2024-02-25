def wait_for_keypress():
    print("Press Enter to resume...", end='', flush=True)
    input()  # Wait for Enter keypress


def clear_screen():  # Works excepts on pycharm IDE
    print('\033[H\033[J')  # ANSI escape code to clear screen


class Calculator:  # Calculator class

    def __init__(self):
        self.first_number = 0
        self.second_number = 0
        self.operator = ''
        self.history = []

    def addition(self, first_number, second_number):  # Method for addition
        self.first_number = first_number
        self.second_number = second_number
        self.operator = '+'
        result = self.first_number+self.second_number
        self.history.append(f"{self.first_number} {self.operator} {self.second_number} = {result} ")
        return result

    def subtraction(self, first_number, second_number):  # Method for subtraction
        self.first_number = first_number
        self.second_number = second_number
        self.operator = '-'
        result = self.first_number - self.second_number
        self.history.append(f"{self.first_number} {self.operator} {self.second_number} = {result} ")
        return result

    def division(self, first_number, second_number):  # Method for division
        self.first_number = first_number
        self.second_number = second_number
        self.operator = '/'
        if second_number == 0:
            result = "Error : Division by zero"
            self.history.append(f"{self.first_number} {self.operator} {self.second_number} = {result} ")
            return result
        else:
            result = self.first_number / self.second_number
            self.history.append(f"{self.first_number} {self.operator} {self.second_number} = {result} ")
            return result

    def multiplication(self, first_number, second_number):  # Method for multiplication
        self.first_number = first_number
        self.second_number = second_number
        self.operator = '*'
        result = self.first_number * self.second_number
        self.history.append(f"{self.first_number} {self.operator} {self.second_number} = {result} ")
        return result

    def show_history(self):  # Method for showing calculation history
        if len(self.history) > 0:
            print("Calculator History:")
            for operation in self.history:
                print(operation)
        else:
            print("History is empty")
            wait_for_keypress()


