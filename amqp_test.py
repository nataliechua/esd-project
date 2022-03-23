from email import message
from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
# from invokes import invoke_http
# import patient

import amqp_setup
import pika
import json


def send_message():
    message='info: +6598443918'
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="order.message", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

    print("\nMessage published to RabbitMQ Exchange.\n")

# send_message()

