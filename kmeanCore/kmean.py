# import urllib.request
import requests
import json


class Kmean(object):

    def __init__(self, district, faculty, rating, affilation, fee):
        self.district = district
        self.faculty = faculty
        self.rating = rating
        self.affilation = affilation
        self.fee = fee
        self.clusterNo=None
    def cluster(self):
        data = {

            "Inputs": {

                "input1":
                    {
                        "ColumnNames": ["college_id", "district", "faculty", "Rating", "affilation", "fee"],
                        "Values": [["0", self.district, self.faculty, self.rating, self.affilation, self.fee], ]
                    }, },
            "GlobalParameters": {
            }
        }

        body = str.encode(json.dumps(data))
        #print(body)
        url = 'https://ussouthcentral.services.azureml.net/workspaces/4706ca7b36cf452695a043b827eec65a/services/5871b8119ab04ed9955ed92e3070123e/execute?api-version=2.0&details=true'
        # Replace this with the API key for the web service
        API_KEY = 'ZuvSeRY48fZExmjaa/e1cZTH/0JdbDzQ//xmctPI4tULQ3cd2P2Et63XIPVzG8ZgNe1UDFY1LjX0gFAncaiF5Q=='
        headers = {'Content-Type': 'application/json',
                   'Authorization': ('Bearer ' + API_KEY)}

        # req = urllib.request.Request(url, body, headers)
        req2 = requests.post(url, data=body, headers=headers).json()
        #print(req2)
        #return req2
        self.clusterNo = req2['Results']['output1']['value']['Values'][0]
        return self.clusterNo[0]


if __name__ == '__main__':
    kmean = Kmean(
        district=input("Enter district:"),
        faculty=input("Enter Faculty:"),
        rating=input("Enter Rating:"),
        affilation=input("Enter Affilation:"),
        fee=input("Enter fee:")
    )

    cluster_num = kmean.cluster()
    print("It's in cluster:", cluster_num)
