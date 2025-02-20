from flask import Flask, request
from twilio import twiml
import sys
 
 
app = Flask(__name__)
 
 
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    #you can change this
    menu = 'Welcome to CSUMB Text Bot Menu\n1. BIT\n2. Library\n3. Dining Commons\n4. Student Center\n5. Gym\n6. Dr. Tao\n7. Champan Science Center\n8. North Quad\n *Reply with 1-8 for more info or Csumb for school phone number*'
    resp = twiml.Response()
    option = message_body
    #dont touch
    if message_body == 'exit':
        sys.exit()
    
    #resp.message('Hello {}, you said: {}'.format(number, message_body))
    ############################
    if option=='1':
        #msg.media("")
        sent="Name: Joel & Dena Gambord Business & Information Technology Building \nAddress: 3052 Divarty St, Marina CA 93933 \nHours: 8 AM to 10 PM \nFact: Did you know the official naming took place on February 25, 2016.\n*Reply 'menu' to go to the main menu*"
    elif option=='2':
        sent="Name: Tanimura & Antle Family Memorial Library \nAddress: 3054 Divarty St, Seaside, CA 93955 \nHours: 8 AM to 12 AM \nFact: Library closes at 4 in the morning during finals. \n*Reply 'menu' to go to the main menu*"
    elif option=='3':
        sent="Name: Dining Commons \nAddress: 3112 Inter-Garrison Rd, Seaside, CA 93955 \nHours: 7 AM to 2 PM, 5 PM to 8 PM \nFact: From 11 AM-12 PM lunch is $4. \n*Reply 'menu' to go to the main menu*"
    elif option=='4':
        sent="Name: Student Center \nAddress: Alumni & Visitors Center, 5108 Fourth Ave, Marina, CA 93933 \nHours: 8 AM to 5 PM \nFact: You can rent out equipment with a drivers license. \n*Reply 'menu' to go to the main menu*"
    elif option=='5':
        sent="Name: Otter Sports Center \nAddress: 2050 Inter-Garrison Rd, Marina, CA 93933 \nHours: 6 AM to 12 Midnight \nFact: The gym has recieved several different upgrades. \n*Reply 'menu' to go to the main menu*"
    elif option=='6':
        sent="Dr. Tao \nEducation: Ph.D. in Computer Engineering, University of California at Irvine.\nThe best professor in Computer Architecture\n*Reply 'menu' to go to the main menu*"
    elif option=='otter' or option=='Otter':
        sent="Nothing hotter than an otter!"
    elif option=='7':
        sent="Name: Chapman Science Academic Center\nAddress: 6133 Fifth Avenue Seaside, CA 93955 \nHours: 7 AM to 10 PM \nFact: Inspired by the Monterey Bay Aquarium, the architect installed a system that sprays salt water in the air to make the building smell like the ocean. \n*Reply 'menu' to go to the main menu*"
    elif option=='8':
        sent="Name: North Quad Dorms \nAddress: 3116 Inter-Garrison Rd Seaside, CA 93955 \nHours: 24 Hours a day \nFact: Students in their second year at CSUMB are eligible for the suites \n*Reply 'menu' to go to the main menu*"
    elif option=='whats my number' or option=='number' or option=='my number':
        sent='Your phone number is: {}'.format(number)
    elif option=='CSUMB' or option=='Csumb' or option=='csumb':
        sent="CSUMB Campus Number: 831582300"
    else:
        sent=menu
    #response
    
    resp.message(sent)

    
    
    return str(resp)
 
if __name__ == '__main__':
    app.run()
