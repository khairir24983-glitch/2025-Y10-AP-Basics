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

# Main Routine
keep_going=""
while keep_going=="":

    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height:")

    # ask for cost

    cost_per_metre = num_check("cost: ")


    # calculator the area
    perimeter = 2 * (width + height)

    # calculate the cost
    cost= cost_per_metre * perimeter

# output the  perimeter cost
    print()
    print(f"perimeter: {perimeter} units")
    print(f"cost: ${cost: .2f} square units")


    # Ask users if they want to keep going
    keep_going = input("press enter to keep going or any key to quit")
    print()

print("thank you for using the fence calculator")