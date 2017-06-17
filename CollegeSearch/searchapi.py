from flask import Flask, jsonify, request
from CollegeSearch import educationSearch

app = Flask(__name__)
#a=[['Nepal Law Camus', 'Kathmandu', 'Other', 'Tribhuwan University', '142864.0', '2'], ['Central Department Of BioTechnology', 'Kathmandu', 'Other', 'Tribhuwan University', '122628.0', '2'], ['Central Department Of Linguistic', 'Kathmandu', 'Other', 'Tribhuwan University', '182417.0', '2'], ['TU School Of Mathmatical Science', 'Kathmandu', 'Other', 'Tribhuwan University', '169099.0', '2'], ['Tcondaryhe Chandbagh Higher Secondary School', 'Kathmandu', 'Other', 'Tribhuwan University', '156308.0', '2'], ['Islington College', 'Kathmandu', 'IT', 'Others', '119507.0', '2'], ['Uniglobe College', 'Kathmandu', 'Business', 'Pokhara University', '177790.0', '3'], ['Gateway College of Professional Studies', 'Kathmandu', 'Business', 'Purbanchal University', '157648.0', '3'], ['Globle College International', 'Kathmandu', 'Business', 'Others', '115415.0', '3'], ['CG Institute of management', 'Kathmandu', 'Business', 'Others', '107522.0', '3'], ['Andrew J Weild College', 'Kathmandu', 'Other', 'CTEVT', '142648.0', '3'], ['Chelsea International College', 'Kathmandu', 'Other', 'CTEVT', '119864.0', '3'], ['Malpi International College', 'Kathmandu', 'Business', 'Others', '162489.0', '3'], ['National College Of Accountancy', 'Kathmandu', 'Business', 'Others', '158359.0', '3'], ['New Jyoti Hogher Secondary School and College', 'Kathmandu', 'Other', 'Others', '107901.0', '3'], ['Liberty College', 'Kathmandu', 'Business', 'Pokhara University', '104459.0', '3'], ['Samriddhi School', 'Kathmandu', 'Business', 'Others', '173281.0', '3'], ['Camad College', 'Kathmandu', 'Business', 'Pokhara University', '160165.0', '3'], ['Excel Business College', 'Kathmandu', 'Business', 'Pokhara University', '176072.0', '3'], ['SAIM College', 'Kathmandu', 'Business', 'Pokhara University', '174806.0', '3'], ['Sunway International Business School', 'Kathmandu', 'Business', 'Others', '172495.0', '3'], ['Phoenix College Of Management', 'Kathmandu', 'Business', 'CTEVT', '153483.0', '3'], ['Atharva Business College', 'Kathmandu', 'Business', 'Pokhara University', '137063.0', '3'], ["People's Campus", 'Kathmandu', 'Business', 'Others', '106582.0', '3'], ['Baneshwor Campus', 'Kathmandu', 'Business', 'Others', '163340.0', '3'], ['Jagat Mandir Higher Secondary School', 'Kathmandu', 'Other', 'Others', '142765.0', '3'], ['Kantipur Campus', 'Kathmandu', 'Business', 'Others', '174848.0', '3'], ['Shivapuri Higher Secondary School and College', 'Kathmandu', 'Business', 'Others', '192955.0', '3'], ['Ratna Jyoti Multipl Campus', 'Kathmandu', 'Business', 'Others', '159152.0', '3'], ['Kathmandu Campus', 'Kathmandu', 'Business', 'Others', '178644.0', '3'], ['Santwona Memorial Campus', 'Kathmandu', 'Business', 'Others', '120610.0', '3'], ['Namgyal Higher Secondary School', 'Kathmandu', 'Medical', 'Others', '188343.0', '3'], ['National College of Accountancy (NCA)', 'Kathmandu', 'Business', 'Others', '130686.0', '3'], ['Kathmandu University Centre for Buddhist Studies', 'Kathmandu', 'Other', 'Kathmandu University', '128799.0', '3'], ['College of Applied Food and Dairy Technology', 'Kathmandu', 'Other', 'Purbanchal University', '189704.0', '3'], ['Himalayan College of Agriculture Science and Technology', 'Kathmandu', 'Engineering', 'Purbanchal University', '197628.0', '3'], ['International Institute of Fashion Design', 'Kathmandu', 'Other', 'Others', '119412.0', '3'], ['Ace Institute Of Mangagement', 'Kathmandu', 'Business', 'Pokhara University', '104573.0', '3'], ['Bridgewater International College', 'Kathmandu', 'Business', 'Others', '108077.0', '3'], ['Rupys International School', 'Kathmandu', 'Business', 'Others', '108432.0', '3'], ['Kaasthamandap Vidhyalaya', 'Kathmandu', 'Business', 'Others', '114932.0', '3'], ['Naaya Aayam Multi-Disciplinary Institute', 'Kathmandu', 'Other', 'Others', '101083.0', '3'], ['British Model College', 'Kathmandu', 'Business', 'Others', '165388.0', '3'], ['Maya Animation Academy', 'Kathmandu', 'Other', 'Others', '198349.0', '3'], ['Namuna College of Fashion Technology', 'Kathmandu', 'Other', 'Purbanchal University', '156778.0', '3'], ['Kathmandu School of Law', 'Bhaktapur', 'Other', 'Purbanchal University', '149420.0', '4']]



@app.route('/search', methods=['POST'])
def get_tasks():
    values = request.form['values']
    #print(values)
    r = educationSearch.EducationSearch(values)
    a = r.search()
    #print(a)
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
    app.run(debug = True, port=5002 )