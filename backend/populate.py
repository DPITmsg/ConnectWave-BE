from config import app, db
import openai

# This code is unusable but we don't use it so it's okay

openai.api_key = "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"
scale = 1

def generate_activity():
    activity = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Think of an activity one can do with \
            friends or strangers. Pass the properties: name, startdate, enddate,\
            time, author, tags, category, description, address,\
            number_of_participants in the following form: [name, startdate, enddate,\
            time, author, tags, category, description, address,\
            number_of_participants]. Please give them in such a manner that they are\
            passable as python strings in a list."},
        ]
    )
    return activity

def generate_user():
    pass
 
def generate_location():
    pass

def populate_database():
    for i in range(scale):
        print(generate_activity())
        generate_user()
        generate_location()

populate_database()
