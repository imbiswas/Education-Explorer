from CollegeSearch import spellingcheck
from CollegeSearch import database

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

if __name__ == '__main__':
    search()