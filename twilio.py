
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

import json
import os

import amqp_setup

monitorBindingKey='#'

def receiveOrderLog():
    amqp_setup.check_setup()
        
    queue_name = 'Send_message'
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an order log by " + __file__)
    processOrderLog(json.loads(body))
    print() # print a new line feed

def processOrderLog(order):
    print("Recording an order log:")
    print(order)


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def twilio_send():
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