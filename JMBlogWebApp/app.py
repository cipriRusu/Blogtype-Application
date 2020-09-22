from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",
    message = "Demo text message sent by server side")

@app.route('/test')
def test():
    return "Some other Page"

if __name__ == '__main__':
    app.run('localhost', 4449)