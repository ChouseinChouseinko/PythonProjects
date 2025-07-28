def Division(num1, num2):

    if num2 > num1:
        num1, num2 = num2, num1
    while num2 != 0:
        varocg = num1 % num2
        num1 = num2
        num2 = varocg

    # code goes here
    return num1


# keep this function call here
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(Division(num1, num2))
