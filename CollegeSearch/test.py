from CollegeSearch import spellingcheck
from CollegeSearch import database
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

# Create a engine for connecting to SQLite3.
# Assuming salaries.db is in your app root folder

e = None;

app = Flask(__name__)
api = Api(app)
a=None;

def search():

    databaseobj = []
    inputstring = input("Enter:")
    #get value from bing
    parser = spellingcheck.keywordInput(inputstring)
    correct = parser.result()
    #print(correct)
    for word in correct:
        #search for each keyword in database
        searcher = database.KeywordSearch(word)
        tempdatabase = searcher.result()
        #print(tempdatabase)
        databaseobj = databaseobj + tempdatabase
    #prints unique data only
    a = list(set(databaseobj))
    print(a)
    # print(len(a))
    # print(len(database))
    #for i in a:
        #print(i)
#e = create_engine(a)
class Departments_Meta(Resource):
    def get(self):

        try:
            return {'Name': a[0],'Address':a[0],'District':a[0],'Faculty':a[0],'Affilation':[0],}
        except TypeError as e:
            pass





api.add_resource(Departments_Meta, '/departments')

if __name__ == '__main__':
    search()
    app.run(port=5002)