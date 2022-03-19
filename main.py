#importing libraries and modules
from hp import get_char
from space import people_space
from weather import get_weather
import os
from twilio.rest import Client
import random, json
from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/sms')
def send_sms():
    #setting up environment variables
  sid = os.environ['sid']
  auth = os.environ['auth']

  #creating mail list
  recipients = {
    "sharon":{"name":"sharon","number":"+17056886756","lucky":random.randint(1,10),"location":"sudbury"}
  }

  # and set the environment variables. See http://twil.io/secure
  client = Client(sid, auth)

  #creating message
  for key, value in recipients.items():

    msg = f"Hello {value['name'].title()},\n\nSpace: {people_space()}. \n\nWeather: The temperature in {value['location'].title()} is currently {get_weather(value['location'])}°c \n\nHarry Potter: {get_char()}"

    print(msg)

    message = client.messages \
                    .create(
                        body=msg,
                        from_='+17058065787', #this is your virtual twillio number
                        to = value["number"] #who youre sending the sms to
                    )

    print(message.sid)
    
    #logging sent messages to json locally
    with open('log.json', 'a') as f:
      json.dump(msg, f, indent = 4)
    

  return render_template("success.html")

app.run(host='0.0.0.0', port=8080, debug=True)
