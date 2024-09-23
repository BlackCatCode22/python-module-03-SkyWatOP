# int. empty list to store numbers
numbers = []

while True:
    # Prompt the user to enter a number or done
    user_input = input('Enter a number or "done" to finish: ')

    # check if user inputs done to break
    if user_input == 'done':
        break
    try:
        # Try to convert the input to a float and add it to list
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input, pls enter a numberic value or use 'done' to exit: ")

if numbers:
    print("Max: ", max(numbers))
    print("Min: ", min(numbers))
else:
    print("No numbers inputted :( ")