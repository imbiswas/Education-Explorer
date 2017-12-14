#FOR TESTING CODE IN APP

from flask import Flask, jsonify, request
from CollegeSearch import educationSearch

app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return (
        "Welcome Guest!!!"
    )
@app.route('/search', methods=['POST'])
def get_tasks1():
    values = request.form['values']
    print(values)
    r = educationSearch.EducationSearch(values)
    a = r.search()
    print(a)
    tasks = []
    for i in a:
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
    app.run(debug = True, port=5001)