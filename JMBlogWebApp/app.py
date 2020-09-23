from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    #render basic index page with received server variable
    return render_template("index.html",
    message = "Demo text message sent by server side")

@app.route('/test')
def test():
    #return string value from server
    return "Some other Page"

@app.route('/secondTest')
def secondTest():
    #render basic page with multiple received server variables
    mockNameValue = "MockName"
    mockAgeValue = 30
    return render_template("secondTest.html", name=mockNameValue, age=mockAgeValue)

@app.route('/thirdTest')
def thirdTest():
    #render basic page with values loaded from json file
    data = json.load(open("mock.json"))
    return render_template("thirdTest.html", jsonData=data)

if __name__ == '__main__':
    app.run('localhost', 4449)