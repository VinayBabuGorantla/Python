from flask import Flask
'''
It creates and instance of the Flast class,
Which is nothing but WSGI(Web Server Gateway Interface) application
'''

# WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask Course"

@app.route("/index")
def index():
    return "Welcome to the Index Page"

if __name__=="__main__":
    app.run(debug=True)