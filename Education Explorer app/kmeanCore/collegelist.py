import mysql.connector
from mysql.connector import errors

class Collegelist(object):
    def __init__(self,clusterno):
        self.clusterno=clusterno
        self.item = ()
        self.listcolz = []
        self.cluster0 = [2, 3, 5, 7, 8, 21, 23, 24, 31, 32, 33, 34, 39, 40, 42, 43, 45, 46, 50, 51, 52, 53, 54, 57, 60, 61,
                    62, 63, 64, 65, 70, 71, 177, 187, 189, 191, 192, 195, 197, 198, 199, 200, 201, 202, 203, 206]
        self.cluster1 = [6, 13, 15, 30, 35, 74, 75, 76, 77, 78, 82, 83, 84, 85, 86, 91, 94, 96, 99, 104, 105, 106, 107, 116,
                    129, 130, 134, 136, 140, 142, 147, 150, 154]
        self.cluster2 = [1, 4, 9, 11, 12, 14, 18, 19, 20, 26, 27, 28, 29, 36, 37, 38, 47, 48, 56, 58, 59, 66, 67, 68, 69,
                    160, 161, 162, 163, 164, 165, 166, 167, 169, 172, 173, 174, 179, 180, 181, 182, 183, 184, 185, 186,
                    188, 193, 194, 196, 204, 205]
        self.cluster3 = [10, 16, 17, 25, 41, 44, 49, 55, 72, 73, 79, 80, 81, 87, 90, 93, 100, 101, 102, 103, 112, 117, 120,
                    121, 122, 123, 124, 125, 126, 127, 131, 132, 137, 138, 139, 146, 148, 153, 155, 156, 157, 158, 170,
                    190]
        self.cluster4 = [22, 88, 89, 92, 95, 97, 98, 108, 109, 110, 111, 113, 114, 115, 118, 119, 128, 133, 135, 141, 143,
                    144, 145, 149, 151, 152, 159, 168, 171, 175, 176, 178]


    def connect(self):

        try:
            cnx = mysql.connector.connect(user="imbiswas@educationxplorer", password='apple1234**',
                                          host="educationxplorer.mysql.database.azure.com", port=3306,
                                          database='educationexplorer')

            if cnx.is_connected():
                #print('Connected to MySQL database')
                pass
            cursor = cnx.cursor()
            query = ("SELECT college_name,college_address,district_name,faculty_name,affilation_name,college_fee,url,logo FROM educationexplorer.tbl_college as clz join educationexplorer.tbl_district as dist on clz.district_id= dist.district_id inner join educationexplorer.tbl_faculty as fac on fac.faculty_id=clz.faculty_id inner join educationexplorer.tbl_affilation as aff on aff.affilation_id= clz.affilation_id join educationexplorer.tbl_misc as misc on misc.misc_id = clz.miscellaneous_id where college_id='%s'" % (self.item))

            cursor.execute(query)
            for (college_name,college_address,district_name,faculty_name,affilation_name,college_fee,url,logo) in cursor:
                individualitem = "{}, {} , {},{}, {}, {},{}, {} ".format(college_name,college_address,district_name,faculty_name,affilation_name,college_fee,url,logo)
                #print(individualitem)
                self.listcolz.append(individualitem)
            #print(self.listcolz)


            cursor.close()



        except ConnectionError as e:
            print(e)

        finally:
            cnx.close()


    def cases(self):
        if self.clusterno == '0':
            for self.item in self.cluster0:
                self.connect()
            #print(self.listcolz)
        # for cluster 1
        elif self.clusterno == '1':
            for self.item in self.cluster1:
                self.connect()
            #print(self.listcolz)
        # for cluster 2
        elif self.clusterno == '2':
            for self.item in self.cluster2:
                self.connect()
            #print(self.listcolz)

        # for cluster 3
        elif self.clusterno == '3':
            for self.item in self.cluster3:
                self.connect()
            #print(self.listcolz)
        # for cluster 4
        elif self.clusterno == '4':
            for self.item in self.cluster4:
                self.connect()
            #print(self.listcolz)
        return self.listcolz
