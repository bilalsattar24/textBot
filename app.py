from flask import Flask, request
from twilio import twiml
import sys
 
 
app = Flask(__name__)
 
 
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    #you can change this
    menu = '1. BIT\n2. Library\n3. Dining Commons\n4. Student Center\n5. Gym'
    resp = twiml.Response()
    option = message_body
    #dont touch
    if message_body == 'exit':
        sys.exit()
    
    #resp.message('Hello {}, you said: {}'.format(number, message_body))
    ############################
    if option=='1':
        sent="Bit builiding is open from 8AM to 8PM\n"
    elif option=='2':
        sent="Library is open from 8AM to 10PM"
    elif option=='3':
        sent=""
    elif option=='4':
        sent=""
    elif option=='5':
        sent=""
    else:
        sent=menu
    #response
    resp.message(menu)

    
    
    return str(resp)
 
if __name__ == '__main__':
    app.run()
