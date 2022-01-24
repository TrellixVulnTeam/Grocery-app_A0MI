from twilio.rest import Client
import time


# Account SID from twilio.com/console
account_sid = "ACe36e256dc29050e96ce9839215e15c97"
# Auth Token from twilio.com/console
auth_token  = "114ae2a1535fb04a2c060092b076c7bc"

# SETUP FOR THE SOFTWARE TO RUN
client = Client(account_sid, auth_token)
localtime = time.localtime()
result = time.strftime("%I:%M:%S %p", localtime)
loop_count = 0

Good_morning_texts = {
    "Hey babe, this is the bot in charge of morning texts, please save this number!",
    "Good morninng loveelyy :))",
    "Good morning Sharmeen, this is Hadi\'s bot",
}
    for Good_morning_text in Good_morning_texts:
        loop_count +=
        message = client.messages.create(
            to="+13479853583",
            from_="+12318190244",
            body="Hello from Python!")
        time.sleep(86400)

print(result)
