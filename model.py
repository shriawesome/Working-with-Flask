"""
model.py
---------------
Implements the model for our website by simulating a database.

Note:
Although it is a simple example , don't do this in a real world example, having a global
object or application data is asking for trouble rather use a db like SQL etc.
"""

import json

def load_db():
    with open('flashcards_db.json','r') as outfile:
        return json.load(outfile)

db=load_db()
