from CollegeSearch import spellingcheck
from CollegeSearch import database

class educationSearch(object):
    def __init__(self,values):
        self.values=values

    def search(self):

        databaseobj = []
        #get value from bing
        parser = spellingcheck.keywordInput(self.values)
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

