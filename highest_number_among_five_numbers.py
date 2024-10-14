def highest_number():

    # Ask the user to input 5 numbers
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    num_3 = float(input("Enter the third number: "))
    num_4 = float(input("Enter the fourth number: "))
    num_5 = float(input("Enter the fifth number: "))

    # Assume the first number as the highest number
    highest = num_1

    # Compare the second number to the highest number
    if num_2 > highest:
        highest = num_2
    
    # Compare the third number to the highest number
    if num_3 > highest:
        highest = num_3
    
    # Compare the fourth number to the highest number
    if num_4 > highest:
        highest = num_4

