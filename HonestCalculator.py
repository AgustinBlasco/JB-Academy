def is_one_digit(value):
    try:
        if value.is_integer():
            if -10 < value < 10:
                return True
    except AttributeError:
        if -10 < value < 10:
            return True
        else:
            return False
    else:
        return False


class HonestCalculator:

    def __init__(self):

        # Messages
        self.msg_index = 0
        self.msg_list = ["Enter an equation",
                         "Do you even know what numbers are? Stay focused!",
                         "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
                         "Yeah... division by zero. Smart move...",
                         "Do you want to store the result? (y / n):",
                         "Do you want to continue calculations? (y / n):",
                         " ... lazy",
                         " ... very lazy",
                         " ... very, very lazy",
                         "You are",
                         "Are you sure? It is only one digit! (y / n)",
                         "Don't be silly! It's just one number! Add to the memory? (y / n)",
                         "Last chance! Do you really want to embarrass yourself? (y / n)"]

        # Variables
        self.running = True
        self.operators = ["+", "-", "*", "/"]
        self.memory = 0.0
        self.operation_ran = 0.0

    def validate_number(self, input_number):
        try:
            if input_number == "M":
                return float(self.memory)
            return float(input_number)
        except ValueError:
            print(self.msg_list[1])

    def validate_operator(self, input_operator):
        if input_operator in self.operators:
            return input_operator
        else:
            print(self.msg_list[2])

    def run_operation(self, x_input, y_input, operation):
        if operation == "/":
            if y_input != 0:
                return x_input / y_input
            else:
                print(self.msg_list[3])
        elif operation == "*":
            return x_input * y_input
        elif operation == "-":
            return x_input - y_input
        else:
            return x_input + y_input

    def set_memory(self, action, number_to_save):
        if action.lower() == "y":
            self.memory = number_to_save

    def close_program(self, action):
        if action.lower() == "n":
            self.running = False

    def check(self, first_value, second_value, operator):
        msg = ""
        if is_one_digit(first_value) and is_one_digit(second_value):
            msg += self.msg_list[6]
        if first_value == 1 or second_value == 1:
            msg += self.msg_list[7]
        if (first_value == 0 or second_value == 0) and (operator == "*" or operator == "+" or operator == "-"):
            msg += self.msg_list[8]
        if msg != "":
            msg = self.msg_list[9] + msg

        print(msg)

    def main(self):

        while self.running:
            print(self.msg_list[0])
            calc = input().split(" ")
            try:
                operator = self.validate_operator(calc[1])
                x_number = self.validate_number(calc[0])
                y_number = self.validate_number(calc[2])
            except ValueError:
                print(self.msg_list[1])
            else:
                self.check(
                    first_value=x_number,
                    second_value=y_number,
                    operator=operator
                )
                self.operation_ran = self.run_operation(
                    x_input=x_number,
                    y_input=y_number,
                    operation=operator
                )
                if self.operation_ran is None:
                    continue
                else:
                    print(self.operation_ran)
                print(self.msg_list[4])
                if input().lower() == 'n':
                    pass
                else:
                    if is_one_digit(self.operation_ran):
                        self.msg_index = 10
                        print(self.msg_list[self.msg_index])
                        if input().lower() == 'n':
                            pass
                        else:
                            while self.msg_index < 12:
                                self.msg_index += 1
                                print(self.msg_list[self.msg_index])
                                if input().lower() == 'n':
                                    break
                                else:
                                    self.memory = self.operation_ran
                    else:
                        self.memory = self.operation_ran
                print(self.msg_list[5])
                if input().lower() == 'n':
                    break


if __name__ == '__main__':
    app = HonestCalculator()
    app.main()
