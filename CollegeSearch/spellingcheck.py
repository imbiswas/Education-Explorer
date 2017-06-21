import requests
import json

class keywordInput(object):
    def __init__(self,userInput):
        self.userInput=userInput

        #userInput=input()
        spellCheck = None
        self.userParse = [userInput]

        url = 'https://api.cognitive.microsoft.com/bing/v5.0/spellcheck/?text=' + userInput

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
                    # spellCheck=str(spellCheck)
                    # spellCheck = input("Enter:")
                    self.userParse.append(spellCheck)
                    #print("You have Entered:", userInput)
                    #print("Corrected spelling:", spellCheck)
                    # self.userParse.insert(0,spellCheck)
            response.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

        #print("Final List : ", self.userParse)

    def result(self): # String result() { return userParse)
        return self.userParse