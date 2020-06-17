from flask import (Flask,render_template,abort,jsonify, request,
                    redirect,url_for)

#import datetime as dt
from model import db,save_db

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

# Add Card via users
# By default views only accept the GET request and not the POST requested, hence to do that
# we need to use the 'methods' parameter.
@app.route('/add_card/',methods=['GET','POST'])
def add_card():
    if request.method == 'POST':
        # Process the data and add it to the database.
        card={'question':request.form['question'],
                'answer':request.form['answer']}
        db.append(card)
        save_db()
        return redirect(url_for('card_view',index=len(db)-1))

    else:
        return render_template('add_card.html')

# Remove a flashcard.
@app.route('/remove_card/<int:index>',methods=['GET','POST'])
def remove_card(index):
    try:
        if request.method=='POST':
            # Delete the entry from the db
            db.pop(index)
            save_db()
            return redirect(url_for('welcome'))
    except IndexError:
        abort(404)


    else:
        return render_template('remove_card.html',card=db[index])
