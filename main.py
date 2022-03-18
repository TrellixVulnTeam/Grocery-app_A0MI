## attendees = ["ken", "mary", "rookwood"]
## for attendee in attendees:
## print(attendee)
## attendee will now hold the last item in the list
## print("the last person in the above list is saved to attendee now and that person's name is {}".format(attendee))

# ------------ PRACTICING LISTS -----------------#

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

# ------------ PRACTICING TIME SPECIFIC FUNCTIONS -----------------#

## import time

## words = ['The', 'big', 'girl', 'went', 'to', 'school']

## for word in words:
## print(word)
## time.sleep(1)

# ------------ PRACTICING TIME SPECIFIC FUNCTIONS -----------------#
##travel_expenses = [
##  [5.00, 2.75, 22.00, 0.00, 0.00],
##  [24.75, 5.50, 15.00, 22.00, 8.00],
##  [2.75, 5.50, 0.00, 29.00, 5.00]
## ]
##print("travel_expenses:")
## week_number = 1

## for day in travel_expenses:
## print("* Week #{}, has ${} in expenses".format(week_number, sum(day)))

# ------------ PACKING FUNCTIONS -----------------#
# def packer (*args):
#     for val in args:
#         print(val)
# packer('hi', 'i', 'love', 'python')
#
# def unpacker ():
#     return(1, 2, 3)
# var1, var2, var3 = unpacker()
#
# print(var1)
# print(var2)
# print(var3)
#
# def unpacker ():
#     return('hey')
# var1, var2, var3 = unpacker()
#         #the above function when written out like that with var1, var2, var3.. will split up the text in "hey" into individual letters and assign it to each of the "vars"
# print(var1)
# print(var2)
# print(var3)

# ------------ ENUMERATE FUNCTIONS-----------------#
# words = ['The', 'big', 'girl', 'went', 'to', 'school']
#
# for index,one_word in enumerate(words, 2):
#     print(index,one_word)
#     print(f'{index}. {one_word}')

# ------------ STEP FUNCTIONS-----------------#
## variable( start : stop : step)
# rainbow = ['red', 'yellow', 'pink', 'blue', 'purple']
# print(rainbow[1:3]) ## prints from range 1 to 3
# print(rainbow[3:]) ## prints from the range 3 onwards
# print(rainbow[::3]) ## prints every a value every 3 steps. The empty start argument in the step function by default is 0
# pritn(rainbow[::-1] ## prints the list in reverse
# ------------ SPLITTING INPUTS -----------------#

# first, last = input('Please provide your first and last name: \n').split(' ')
# print(first)
# print(last)

# ------------ CHECKING INPUTS -----------------#

# request = input("What would you like?  ")
# while "please" not in request:
#     request = input("You seem to be missing a magic word.  What would you like?  ")
# print("Here you go!")

# ------------ JOINING LISTS -----------------#

# musical_groups = [
#     ["Ad Rock", "MCA", "Mike D."],
#     ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
#     ["Salt", "Peppa", "Spinderella"],
#     ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
#     ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
#     ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
#     ["Run", "DMC", "Jam Master Jay"],
# ]
# for group in musical_groups:
#     print(", ".join(group))
#     break
# for tri in musical_groups:
#     if len(tri) == 3:
#         print(", ".join(tri))

# ------------ SEARCHING THROUGH LISTS -----------------#
# some_list = ['ALena', 'Ashley', 'Nicole', 'Treasure']
# teachers.index('Nicole') # will return the number 2 because the number that matches 'Nicole is third in the list
#
# #if you add Niccole one more time in the listf
# some_list = ['ALena', 'Ashley', 'Nicole', 'Treasure', 'Nicole']
# teachers.index('Nicole') # will STILL return the number 2 because it stops running as soon as it finds a match

# ------------ DICTIONARIES and ITERATION-----------------#
course = {'teacher':'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginnier'}
print(course['teacher'])
print(course.keys()) # prints the keys of each value
sorted(course.values())

course['teacher'] = 'Dean' # Changes the value assigned to the key 'teacher'

for item in course:
        print(course[items]) # Prints all the values assigned

for key, value in course.items(): # .items will sort through all keys and values
    print(key,value)

for key in course.keys(): # .keys will sort through all the keys in the dictionary
    print(key)

For value in course.values(): #.values will sort through all the values in the dictionary instead


def print_teach (**kwargs): # Example of a function that uses packing. Any amount of arguments can be passed through the function now - KWARGS = key word arguments
    for key, value in kwargs.items

# ------------ OBJECT ORIENTED PYTHON -----------------#

#Is a way to structure your code into objects and behaviors
# E.g a Car has two doors which is an object, and behaviors are opening/closing

class Car: # this is called instantiation
    pass
my_car = Car () # this is the instance

print(my_car) #prints the instance
print(type(my_car)) #checking to see the type of the instance in the class
print(isinstance(my_car, Car)) #to check if something is an instance of a given class

# ------------ STORING TEXT MESSAGES AS LISTS FROM INPUT -----------------#
# from docutils.parsers.rst.directives import body
# from flask import Flask, request, redirect
# from twilio.twiml.messaging_response import MessagingResponse
#
# account_sid = "ACe36e256dc29050e96ce9839215e15c97"
# auth_token = "dce9b989e87c4ded5a4bd8cc6e23814b"
#
# app = Flask(__name__)
#
# @app.route("/sms", methods=['GET', 'POST'])
# def incoming_sms():
#     """Send a dynamic reply to an incoming text message"""
#     # Get the message the user sent our Twilio number
#     body = request.values.get('Body', None)
#     return str(body)
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
# shopping_list = []
# new_message = incoming_sms()
# resp = MessagingResponse()
# print(new_message)
#
# # def catch_items(potato):
# #     if new_message != 'LIST':
# #         shopping_list.append(potato)
# #         resp.message("{} has been added to the list, you now have {} item(s) in your cart now".format(shopping_list[-1],len(shopping_list)))
# #
# #
#
# while True:
#     if new_message == 'DONE':
#         break
#     # elif new_message == 'LIST':
#     #     for cart_items in shopping_list:
#     #         resp.message(cart_items)
#     elif new_message == 'HELP':
#         resp.message("this is working")
#         # resp.message("""Enter 'DONE' to stop adding items
#         # Enter 'HELP' for this help
#         # ENTER 'LIST' to see everything in the cart so far""")
#     continue
# # catch_items(new_message)
