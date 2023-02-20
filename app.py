from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

# FOR NEWS API
current_date= datetime.now()
today = current_date.strftime("%Y-%m-%d")

urlfornews = (f'https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from={today}&'
       'sortBy=popularity&'
       'apiKey=#####################') # YOUR API KEY HERE IN PLACE OF #
response = requests.get(urlfornews)
news_data = response.json()
# NEWS API END

# FOR QUIZ API
# SET [ amount = 20 to larger number ,
#       category = 9/18/22/21 all these code to other codes from taking from api json,
#       difficulty = hard to easy/medium,
#       ]

# AS PER YOUR REQUIREMENT OR SEND IT  VIA USER INPUT, i.e.Dynamically

urlforgk = ('https://opentdb.com/api.php?amount=20&category=9&difficulty=hard&type=multiple')
urlforcs = ('https://opentdb.com/api.php?amount=20&category=18&difficulty=hard&type=multiple')
urlforgeo = ('https://opentdb.com/api.php?amount=20&category=22&difficulty=hard&type=multiple')
urlforsports = ('https://opentdb.com/api.php?amount=20&category=21&difficulty=hard&type=multiple')

response1 = requests.get(urlforgk)
response2 = requests.get(urlforcs)
response3 = requests.get(urlforgeo)
response4 = requests.get(urlforsports)

data_for_gk = response1.json()
data_for_cs = response2.json()
data_for_go = response3.json()
data_for_sp = response4.json()

# QUIZ API END

# NEWS PAGES STARTS ---
@app.route('/')
def news():
    return render_template('index.html', news_data=news_data)

@app.route('/allnews')
def allnews():
    return render_template('allnews.html', news_data=news_data)\

@app.route('/allnews_2')
def allnews_2():
    return render_template('allnews_2.html', news_data=news_data)\

# QUESTION ANSWER PAGES STARTS ---

@app.route('/data_for_gk')
def gkmethod():
    return render_template('GK.html', data_for_gk = data_for_gk)

@app.route('/data_for_cs')
def csmethod():
    return render_template('CS.html', data_for_cs = data_for_cs)

@app.route('/data_for_go')
def gomethod():
    return render_template('GO.html', data_for_go = data_for_go)

@app.route('/data_for_sp')
def spmethod():
    return render_template('SP.html', data_for_sp = data_for_sp)

if __name__ == '__main__':
    app.run(debug=True)
