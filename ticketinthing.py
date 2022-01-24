ticket_price = 10
tickets_remaining = 100

while tickets_remaining != "0":
    # Output how many tickets are remaining in a variable
    print("There are {} tickets remaining".format(tickets_remaining))

    # Gather the user's name and assign it to a new variable
    input_name = input("What is your name?")

    # prompt the user by name and ask how many tickets they would like
    input_ticket_qty = input("Hello {}, how many tickets would you like".format(input_name))

    # Calculate the price (number of tickets multiplied by the price) and assign it to a variable
    cart_price = int(input_ticket_qty) * int(ticket_price)

    # Output the price to the screen
    print(cart_price)
    
    # Define left over tickets
    adjusted_tickets = int(tickets_remaining) - int(input_ticket_qty)

    #ask them if they would like to purchase
    checkout_query = input("Would you like to buy the these tickets? - Answer with Y/N")
    if checkout_query == "Y":
         if int(adjusted_tickets) != "0":
             print("cleared this part of the code 1")
         else:
             "we're fresh out!"

else:
    print("we're fresh out, sorry!")

