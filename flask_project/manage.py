from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
   return 'Welcome to my Flask app!'

@app.route('/greetings/')
def greetings():
   return 'Please choose a season: For Christmas season: greetings/christmas ; For New Year season: greetings/newyear'

@app.route('/greetings/<greeting>')
def greeting_redirect(greeting):
   if greeting == 'christmas':
       return redirect(url_for('christmas'))
   elif greeting == 'newyear':
       return redirect(url_for('newyear'))
   else: 
       return 'Invalid greeting. Please enter a valid greeting endpoint, such as /greetings/christmas or /greetings/newyear/'

@app.route('/christmas')
def christmas():
   return 'Merry Christmas!'

@app.route('/newyear')
def newyear():
   return 'Happy New Year!'

if __name__ == "__main__":
   app.run(debug=True)

