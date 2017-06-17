from CollegeSearch import spellingcheck
from CollegeSearch import database

class EducationSearch(object):
    def __init__(self,values):
        self.values=values

    def search(self):
        mov=[]
        box=[]
        st=[]
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
        for line in a:
            line = line.split(",")
            # print(line)
            for member in line:
                member = member.strip()
                # print(member)
                box.append(member)
            st = box
            box = []
            mov.append(st)
            # print(st)
        #print(mov)
        return mov


