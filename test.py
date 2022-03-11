
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']='ACb439cfbd32321ec9c5155a497b3a0518'
auth_token = os.environ['TWILIO_AUTH_TOKEN']='8794277a116a7098ad00f1f4f8b097fb'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello this is twilio test.",
                     from_='+17087251094',
                     to='+6598443918'
                 )

print(message.sid)