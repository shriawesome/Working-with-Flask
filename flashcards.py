from flask import Flask,render_template,abort,jsonify

#import datetime as dt
from model import db

# Flask constructor that creates a global Flask application object\
# __name__ contains the name of the present module
app=Flask(__name__)

# @app.route() is a decorator and route is a method of the app object that,
# changes the below f'n from a simple f'n to a "View F'n". By doing this we are assigning the
# URL to our application in this case the '/' is the root URL for our application.
@app.route('/')
def welcome():
    # Normally a web page is a complex page with not just a single string value
    # return 'Welcome to my Flash Card Application'

    # render_template will look for the named template in the templates/
    # cards=db passes the entire db values which should not be done in production env
    return render_template('welcome.html',
                            name="Shri ",
                            age=24,
                            cards=db)

'''
# Just for understanding basic flask
@app.route('/date')
def date():
    return 'The page was Served at ' + str(dt.datetime.now())

counter=0
@app.route('/count_views')
def count_views():
    global counter
    counter+=1
    return "This page is viewed {} times".format(counter)
'''
# <int:index> : Special argument that only route will understand.
# Error 404 to handle and exception when the user enters the index not in range.
@app.route('/cards/<int:index>')
def card_view(index):
    try :
        return render_template('card.html',
                           card=db[index],
                           index=index,
                           max_index=len(db)-1)
    except IndexError:
        abort(404)

# Working with REST APIs

@app.route('/api/cards/')
def api_card_details():
    # return db won't work as flask doesn't allow the whole list to be passed in one go
    return jsonify(db)

@app.route('/api/cards/<int:index>')
def api_card_view(index):
    try:
        return db[index]
    except IndexError:
        abort(404)
