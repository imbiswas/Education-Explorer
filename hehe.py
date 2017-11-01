from flask import Flask, jsonify, request
import urllib.request
import requests
import json
import mysql.connector
from mysql.connector import errors


app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return (
        "Welcome Guest!!!"
    )

######################################################
@app.route('/api', methods=['POST'])
def get_tasks():
    district = request.form['district']
    faculty = request.form['faculty']
    rating = request.form['rating']
    affilation = request.form['affilation']
    fee = request.form['fee']
    # print(district)

    box = []
    st = []
    mov = []
    p = []
    rank1 = []
    rank2 = []
    rank3 = []
    rank4 = []
    rank5 = []
    rankedlist = []
    tasks = []
    listcolz=[]
    cluster0 = [2, 3, 5, 7, 8, 21, 23, 24, 31, 32, 33, 34, 39, 40, 42, 43, 45, 46, 50, 51, 52, 53, 54, 57, 60, 61,
                62, 63, 64, 65, 70, 71, 177, 187, 189, 191, 192, 195, 197, 198, 199, 200, 201, 202, 203, 206]
    cluster1 = [6, 13, 15, 30, 35, 74, 75, 76, 77, 78, 82, 83, 84, 85, 86, 91, 94, 96, 99, 104, 105, 106, 107, 116,
                129, 130, 134, 136, 140, 142, 147, 150, 154]
    cluster2 = [1, 4, 9, 11, 12, 14, 18, 19, 20, 26, 27, 28, 29, 36, 37, 38, 47, 48, 56, 58, 59, 66, 67, 68, 69,
                160, 161, 162, 163, 164, 165, 166, 167, 169, 172, 173, 174, 179, 180, 181, 182, 183, 184, 185, 186,
                188, 193, 194, 196, 204, 205]
    cluster3 = [10, 16, 17, 25, 41, 44, 49, 55, 72, 73, 79, 80, 81, 87, 90, 93, 100, 101, 102, 103, 112, 117, 120,
                121, 122, 123, 124, 125, 126, 127, 131, 132, 137, 138, 139, 146, 148, 153, 155, 156, 157, 158, 170,
                190]
    cluster4 = [22, 88, 89, 92, 95, 97, 98, 108, 109, 110, 111, 113, 114, 115, 118, 119, 128, 133, 135, 141, 143,
                144, 145, 149, 151, 152, 159, 168, 171, 175, 176, 178]
    item=()
    data = {

        "Inputs": {

            "input1":
                {
                    "ColumnNames": ["college_id", "district", "faculty", "Rating", "affilation", "fee"],
                    "Values": [["0", district, faculty, rating, affilation, fee], ]
                }, },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))
    # print(body)
    url = 'https://ussouthcentral.services.azureml.net/workspaces/4706ca7b36cf452695a043b827eec65a/services/5871b8119ab04ed9955ed92e3070123e/execute?api-version=2.0&details=true'
    # Replace this with the API key for the web service
    API_KEY = 'ZuvSeRY48fZExmjaa/e1cZTH/0JdbDzQ//xmctPI4tULQ3cd2P2Et63XIPVzG8ZgNe1UDFY1LjX0gFAncaiF5Q=='
    headers = {'Content-Type': 'application/json',
               'Authorization': ('Bearer ' + API_KEY)}

    # req = urllib.request.Request(url, body, headers)
    req2 = requests.post(url, data=body, headers=headers).json()
    # print(req2)
    # return req2
    clusterNo = req2['Results']['output1']['value']['Values'][0]

    scanresult = clusterNo[0]
    # print(scanresult)


    if scanresult == '0':
        for item in cluster0:
            try:
                cnx = mysql.connector.connect(user="imbiswas@educationxplorer", password='Il0v3u@l0t',
                                              host="educationxplorer.mysql.database.azure.com", port=3306,
                                              database='educationexplorer')

                if cnx.is_connected():
                    # print('Connected to MySQL database')
                    pass
                cursor = cnx.cursor()
                query = (
                    "SELECT college_name,college_address,district_name,faculty_name,affilation_name,college_fee,url,logo FROM educationexplorer.tbl_college as clz join educationexplorer.tbl_district as dist on clz.district_id= dist.district_id inner join educationexplorer.tbl_faculty as fac on fac.faculty_id=clz.faculty_id inner join educationexplorer.tbl_affilation as aff on aff.affilation_id= clz.affilation_id join educationexplorer.tbl_misc as misc on misc.misc_id = clz.miscellaneous_id where college_id='%s'" %
                    (item))

                cursor.execute(query)
                for (
                        college_name, college_address, district_name, faculty_name, affilation_name, college_fee, url,
                        logo) in cursor:
                    individualitem = "{}, {} , {},{}, {}, {},{}, {} ".format(college_name, college_address,
                                                                             district_name,
                                                                             faculty_name, affilation_name, college_fee,
                                                                             url,
                                                                             logo)
                    # print(individualitem)
                    listcolz.append(individualitem)
                # print(self.listcolz)


                cursor.close()



            except ConnectionError as e:
                print(e)

            finally:
                cnx.close()
            # print(self.listcolz)
            # for cluster 1
    elif scanresult == '1':
        for item in cluster1:
            try:
                cnx = mysql.connector.connect(user="imbiswas@educationxplorer", password='Il0v3u@l0t',
                                              host="educationxplorer.mysql.database.azure.com", port=3306,
                                              database='educationexplorer')

                if cnx.is_connected():
                    # print('Connected to MySQL database')
                    pass
                cursor = cnx.cursor()
                query = (
                    "SELECT college_name,college_address,district_name,faculty_name,affilation_name,college_fee,url,logo FROM educationexplorer.tbl_college as clz join educationexplorer.tbl_district as dist on clz.district_id= dist.district_id inner join educationexplorer.tbl_faculty as fac on fac.faculty_id=clz.faculty_id inner join educationexplorer.tbl_affilation as aff on aff.affilation_id= clz.affilation_id join educationexplorer.tbl_misc as misc on misc.misc_id = clz.miscellaneous_id where college_id='%s'" %
                    (item))

                cursor.execute(query)
                for (
                        college_name, college_address, district_name, faculty_name, affilation_name, college_fee, url,
                        logo) in cursor:
                    individualitem = "{}, {} , {},{}, {}, {},{}, {} ".format(college_name, college_address,
                                                                             district_name,
                                                                             faculty_name, affilation_name, college_fee,
                                                                             url,
                                                                             logo)
                    # print(individualitem)
                    listcolz.append(individualitem)
                # print(self.listcolz)


                cursor.close()



            except ConnectionError as e:
                print(e)

            finally:
                cnx.close()
            # print(self.listcolz)
            # for cluster 2
    elif scanresult == '2':
        for item in cluster2:
            try:
                cnx = mysql.connector.connect(user="imbiswas@educationxplorer", password='Il0v3u@l0t',
                                              host="educationxplorer.mysql.database.azure.com", port=3306,
                                              database='educationexplorer')

                if cnx.is_connected():
                    # print('Connected to MySQL database')
                    pass
                cursor = cnx.cursor()
                query = (
                    "SELECT college_name,college_address,district_name,faculty_name,affilation_name,college_fee,url,logo FROM educationexplorer.tbl_college as clz join educationexplorer.tbl_district as dist on clz.district_id= dist.district_id inner join educationexplorer.tbl_faculty as fac on fac.faculty_id=clz.faculty_id inner join educationexplorer.tbl_affilation as aff on aff.affilation_id= clz.affilation_id join educationexplorer.tbl_misc as misc on misc.misc_id = clz.miscellaneous_id where college_id='%s'" %
                    (item))

                cursor.execute(query)
                for (
                        college_name, college_address, district_name, faculty_name, affilation_name, college_fee, url,
                        logo) in cursor:
                    individualitem = "{}, {} , {},{}, {}, {},{}, {} ".format(college_name, college_address,
                                                                             district_name,
                                                                             faculty_name, affilation_name, college_fee,
                                                                             url,
                                                                             logo)
                    # print(individualitem)
                    listcolz.append(individualitem)
                # print(self.listcolz)


                cursor.close()



            except ConnectionError as e:
                print(e)

            finally:
                cnx.close()
            # print(self.listcolz)

            # for cluster 3
    elif scanresult == '3':
        for item in cluster3:
            try:
                cnx = mysql.connector.connect(user="imbiswas@educationxplorer", password='Il0v3u@l0t',
                                              host="educationxplorer.mysql.database.azure.com", port=3306,
                                              database='educationexplorer')

                if cnx.is_connected():
                    # print('Connected to MySQL database')
                    pass
                cursor = cnx.cursor()
                query = (
                    "SELECT college_name,college_address,district_name,faculty_name,affilation_name,college_fee,url,logo FROM educationexplorer.tbl_college as clz join educationexplorer.tbl_district as dist on clz.district_id= dist.district_id inner join educationexplorer.tbl_faculty as fac on fac.faculty_id=clz.faculty_id inner join educationexplorer.tbl_affilation as aff on aff.affilation_id= clz.affilation_id join educationexplorer.tbl_misc as misc on misc.misc_id = clz.miscellaneous_id where college_id='%s'" %
                    (item))

                cursor.execute(query)
                for (
                        college_name, college_address, district_name, faculty_name, affilation_name, college_fee, url,
                        logo) in cursor:
                    individualitem = "{}, {} , {},{}, {}, {},{}, {} ".format(college_name, college_address,
                                                                             district_name,
                                                                             faculty_name, affilation_name, college_fee,
                                                                             url,
                                                                             logo)
                    # print(individualitem)
                    listcolz.append(individualitem)
                # print(self.listcolz)


                cursor.close()



            except ConnectionError as e:
                print(e)

            finally:
                cnx.close()
            # print(self.listcolz)
            # print(self.listcolz)
            # for cluster 4
    elif scanresult == '4':
        for item in cluster4:
            try:
                cnx = mysql.connector.connect(user="imbiswas@educationxplorer", password='Il0v3u@l0t',
                                              host="educationxplorer.mysql.database.azure.com", port=3306,
                                              database='educationexplorer')

                if cnx.is_connected():
                    # print('Connected to MySQL database')
                    pass
                cursor = cnx.cursor()
                query = (
                    "SELECT college_name,college_address,district_name,faculty_name,affilation_name,college_fee,url,logo FROM educationexplorer.tbl_college as clz join educationexplorer.tbl_district as dist on clz.district_id= dist.district_id inner join educationexplorer.tbl_faculty as fac on fac.faculty_id=clz.faculty_id inner join educationexplorer.tbl_affilation as aff on aff.affilation_id= clz.affilation_id join educationexplorer.tbl_misc as misc on misc.misc_id = clz.miscellaneous_id where college_id='%s'" %
                    (item))

                cursor.execute(query)
                for (
                        college_name, college_address, district_name, faculty_name, affilation_name, college_fee, url,
                        logo) in cursor:
                    individualitem = "{}, {} , {},{}, {}, {},{}, {} ".format(college_name, college_address,
                                                                             district_name,
                                                                             faculty_name, affilation_name, college_fee,
                                                                             url,
                                                                             logo)
                    # print(individualitem)
                    listcolz.append(individualitem)
                # print(self.listcolz)


                cursor.close()



            except ConnectionError as e:
                print(e)

            finally:
                cnx.close()









    # print(correct)
    for line in listcolz:
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
    # print(mov)

    for lines in mov:
        if district in lines[1] and faculty in lines[2] and affilation in lines[3]:
            rank = ['1']
            # print(rank)
            lines.extend(rank)
            # print(lines)
            p.append(lines)
        elif (district in lines[1] and faculty in lines[2]):
            rank = ['2']
            # print(rank)
            lines.extend(rank)
            # print(lines)
            p.append(lines)
        elif (district in lines[1] and affilation in lines[3]) or (faculty in lines[2] and affilation in lines[3]):
            rank = ['3']
            lines.extend(rank)
            # print(lines)
            p.append(lines)

        elif district in lines[1] or faculty in lines[2] or affilation in lines[3]:
            rank = ['4']
            # print(rank)
            lines.extend(rank)
            # print(lines)
            p.append(lines)
        else:
            rank = ['5']
            lines.extend(rank)
            # print(lines)
            p.append(lines)
    # print(p)
    for counter in p:
        if counter[-1] is '1':
            rank1.append(counter)
            # print(counter)
            # print(counter[-1])
            # print(rank1)
        elif counter[-1] is '2':
            rank2.append(counter)

        elif counter[-1] is '3':
            rank3.append(counter)
        elif counter[-1] is '3':
            rank4.append(counter)
        else:
            rank5.append(counter)

    rankedlist = rank1 + rank2 + rank3 + rank4 + rank5
    # print(rankedlist)
    # return rankedlist
    # print(a)
    tasks = []
    for i in rankedlist:
        tasks1 = [
            {
                'College Name': i[0],
                'Address': i[1],
                'District': i[2],
                'Faculty': i[3],
                'Affilation': i[4],
                'url': i[6],
                'logo': i[7],

            },

        ]
        tasks.append(tasks1)
    return jsonify({'tasks': tasks})
####################################################################################
@app.route('/search', methods=['POST'])
def get_tasks1():
    values = request.form['values']
    #print(values)

    mov=[]
    box=[]
    st=[]
    databaseobj = []

    #userInput=values
    spellCheck = None
    userParse = [values]

    url = 'https://api.cognitive.microsoft.com/bing/v5.0/spellcheck/?text=' + values

    headers = {
        'Ocp-Apim-Subscription-Key': '7e63d0dc89a24ca7a64c90720c64cabc'
    }
    try:
        response = requests.get(url, headers=headers)
        output = response.json()
        # pprint(output)
        # outputValue = (output['flaggedTokens'])
        # print(outputValue)
        for item in output['flaggedTokens']:
            # print (item['suggestions'])
            for data in item['suggestions']:
                spellCheck = data['suggestion']
                userParse.append(spellCheck)

        response.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


    correct = userParse
    #print(correct)
    for word in correct:
        #search for each keyword in database
        keyword=word
        nameList=[]
        """ Connect to MySQL database """
        try:
            conn = mysql.connector.connect(user="imbiswas@educationxplorer", password='Il0v3u@l0t',
                                          host="educationxplorer.mysql.database.azure.com", port=3306,
                                          database='educationexplorer')
            if conn.is_connected():
                #print('Connected to MySQL database')
                pass
            cursor = conn.cursor()
            query = ("SELECT college_name,college_address,district_name,faculty_name,affilation_name,college_fee,url,logo FROM educationexplorer.tbl_college as clz join educationexplorer.tbl_district as dist on clz.district_id= dist.district_id inner join educationexplorer.tbl_faculty as fac on fac.faculty_id=clz.faculty_id inner join educationexplorer.tbl_affilation as aff on aff.affilation_id= clz.affilation_id join educationexplorer.tbl_misc as misc on misc.misc_id = clz.miscellaneous_id where match(college_name) against('%s' in natural language mode)or match(faculty_name)against('%s' in natural language mode) or match(district_name)against('%s' in natural language mode) or match(affilation_name)against('%s' in natural language mode) or match(college_address)against('%s' in natural language mode)" %(keyword, keyword, keyword, keyword, keyword))

            cursor.execute(query)
            for (college_name,college_address,district_name,faculty_name,affilation_name,college_fee,url,logo) in cursor:
                dblist = "{}, {} , {}, {} , {}, {}, {} , {}".format(
                    college_name, college_address, district_name, faculty_name, affilation_name, college_fee, url, logo)
                nameList.append(dblist)
            databaseobj = nameList
            cursor.close()
            #print(self.nameList)

        except ConnectionError as e:
            print(e)

        finally:

            conn.close()


        #print(tempdatabase)

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



    tasks=[]
    for i in mov:
        tasks1 = [
            {
                'College Name': i[0],
                'Address':i[1],
                'District': i[2],
                'Faculty': i[3],
                'Affilation': i[4],
                'url':i[6],
                'logo':i[7],

            },

        ]
        tasks.append(tasks1)
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug = True)