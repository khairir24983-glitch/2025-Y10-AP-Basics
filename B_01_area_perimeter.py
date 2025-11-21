# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "please enter the number that is more than zero\n"
    while True:

       try:
           # ask the user for a number
           response = float(input(question))

           # check thet the number is more than zero
           if response > 0:
              return response
           else:
               print(error)

       except ValueError:
           print(error)

# Main Routine starts here...

keep_going = ""
while keep_going== "":

    # Get width and height
    width = num_check("width: ")
    height = num_check("height: ")

    # Calculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    # Ask user if they want to keep going
    keep_going = input("prees enter to keep going or any key to quit. ")
    print()
print("Thank you for using the area / perimeter calculator")


