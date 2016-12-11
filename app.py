from flask import Flask, request
from twilio import twiml
import sys
 
 
app = Flask(__name__)
 
 
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    #you can change this
    menu = '1. BIT\n2. Library\n3. Dining Commons\n4. Gym'
    resp = twiml.Response()
    
    #dont touch
    if message_body == 'exit':
        sys.exit()
    
    #resp.message('Hello {}, you said: {}'.format(number, message_body))
    ############################

    #response
    resp.message(menu)
    
    
    return str(resp)
 
if __name__ == '__main__':
    app.run()
