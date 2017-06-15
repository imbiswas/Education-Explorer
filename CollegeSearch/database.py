import mysql.connector
from mysql.connector import Error

class KeywordSearch(object):
    def __init__(self,keyword):
        self.keyword=keyword
        self.nameList=[]
        """ Connect to MySQL database """
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='educationexplorer',
                                           user='root',
                                           password='1234')
            if conn.is_connected():
                # print('Connected to MySQL database')
                pass
            cursor = conn.cursor()
            query = (
                "SELECT college_name,college_address,district_name,faculty_name,affilation_name FROM educationexplorer.tbl_college as clz join educationexplorer.tbl_district as dist  on clz.district_id= dist.district_id inner join educationexplorer.tbl_faculty as fac on fac.faculty_id=clz.faculty_id inner join educationexplorer.tbl_affilation as aff on aff.affilation_id= clz.affilation_id where match(college_name) against('%s' in natural language mode) or match(faculty_name)against('%s' in natural language mode) or match(district_name)against('%s' in natural language mode) or match(affilation_name)against('%s' in natural language mode) or match(college_address)against('%s' in natural language mode)" % (
                    keyword, keyword, keyword, keyword, keyword))
            cursor.execute(query)
            for (college_name, college_address, district_name, faculty_name, affilation_name) in cursor:
                dblist = "{}, {} , {}, {} , {}".format(
                    college_name, college_address, district_name, faculty_name, affilation_name)
                self.nameList.append(dblist)

            cursor.close()
            #print(self.nameList)

        except ConnectionError as e:
            print(e)

        finally:

            conn.close()

    def result(self):  # String result() { return userParse)
            return self.nameList