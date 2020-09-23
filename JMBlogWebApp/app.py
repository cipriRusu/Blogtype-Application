from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",
    message = "Demo text message sent by server side")

@app.route('/test')
def test():
    return "Some other Page"

@app.route('/secondTest')
def secondTest():
    mockNameValue = "MockName"
    mockAgeValue = 30
    return render_template("secondTest.html", name=mockNameValue, age=mockAgeValue)

if __name__ == '__main__':
    app.run('localhost', 4449)