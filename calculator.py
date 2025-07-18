def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y


def main():
    print("===Amazing Calculator is here===")


    # we must create some selections so the user to select what type of calcilation he/she wants
while True:
    print("\nSelect operation:")
    print("1. ADD")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. I am leaving this project")

    answer = input("Select an operation ")
    if answer == '5':
        print("GoodBye Sir")
        break

    if answer in ('1', '2', '3', '4'):
        try:
            first_number = float(input("Enter a number: "))
            second_number = float(input("Enter a number: "))
        except ValueError:
            print("Invalid Input.Please try to input numbers")
            continue
        if answer == '1':
            print(
                f"Result: {first_number} + {second_number} = {add(first_number, second_number)}")
        elif answer == '2':
            print(
                f"Result: {first_number} - {second_number} = {sub(first_number, second_number)}")
        elif answer == '3':
            print(
                f"Result: {first_number} * {second_number} = {multiply(first_number, second_number)}")
        elif answer == '4':
            result = divide(first_number, second_number)
            print(f"Result: {first_number} / {second_number} = {result}")


# this is must have , without this the terminal will not show you a message
if __name__ == "__main__":
    main()
