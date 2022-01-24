## attendees = ["ken", "mary", "rookwood"]
## for attendee in attendees:
   ## print(attendee)
## attendee will now hold the last item in the list
## print("the last person in the above list is saved to attendee now and that person's name is {}".format(attendee))

#------------ PRACTICING LISTS -----------------#

##continents = [
    ## 'Asia',
    ## 'South America',
    ## 'North America',
    ## 'Africa',
    ## 'Europe',
    ## 'Antarctica',
    ## 'Australia',
##]
## Your code here
## for continent in continents:
    ## if continent[0] == "A":
       ## print("* "+"{}".format(continent))

#------------ PRACTICING TIME SPECIFIC FUNCTIONS -----------------#

## import time

## words = ['The', 'big', 'girl', 'went', 'to', 'school']

## for word in words:
    ## print(word)
    ## time.sleep(1)

#------------ PRACTICING TIME SPECIFIC FUNCTIONS -----------------#
##travel_expenses = [
  ##  [5.00, 2.75, 22.00, 0.00, 0.00],
  ##  [24.75, 5.50, 15.00, 22.00, 8.00],
  ##  [2.75, 5.50, 0.00, 29.00, 5.00]
## ]
##print("travel_expenses:")
## week_number = 1

## for day in travel_expenses:
    ## print("* Week #{}, has ${} in expenses".format(week_number, sum(day)))

#------------ STORING LISTS FROM INPUT -----------------#
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

account_sid = "ACe36e256dc29050e96ce9839215e15c97"
auth_token  = "114ae2a1535fb04a2c060092b076c7bc"

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply(user_message):
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


def display_cart():
    for cart_items in shopping_list:
        print(cart_items)

def catch_items(potato):
    if new_item != 'LIST':
        shopping_list.append(potato)
        print("{} has been added to the list, you now have {} item(s) in your cart now".format(shopping_list[-1], len(shopping_list)))

def show_help():
    message = client.messages.create(
        to="+13479853583",
        from_="+12318190244",
        body="""Enter 'DONE' to stop adding items
Enter 'HELP' for this help
ENTER 'LIST' to see everything in the cart so far"""
)

    print("What do you need to buy")
    print("""
Enter 'DONE' to stop adding items
Enter 'HELP' for this help
ENTER 'LIST' to see everything in the cart so far
""")
show_help()
while True:
    new_item = input("> ")
    if new_item == 'DONE':
        break
    elif new_item == 'LIST':
        display_cart()
    elif new_item == 'HELP':
        show_help()
        continue


    catch_items(new_item)








