from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Welcome to my website"

@app.route('/contact')
def contact():
    return "My contact no is 1234567788"

@app.route('/package')
def xyz():
    return "My package is xyz"


app.run(port=5005)
