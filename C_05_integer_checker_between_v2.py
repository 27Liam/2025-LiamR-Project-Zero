# Functions go here
def num_check(question, low, high):
    """Checks users enter an integer between 2 values"""

    error = f"Oops - please enter an integer between {low} and {high}"

    while True:

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine goes here

# loop for testing purposes...
while True:

    print()

    # ask user for integer
    my_num = int_check("Choose a number:", 1, 10)
    print(f"You chose {my num}")

    my_float = num_check("Please enter a number more than 0: ", "float")
    print(f"Thanks. You chose {my_float}")
    print()
    my_int = num_check("Please enter an integer more than 0: ", "integer", "")

    if my_int == "":
        print("You have chosen infinite mode.")
    else:
        print(f"Thanks. You chose {my_int}")
