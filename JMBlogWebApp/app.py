from flask import Flask, render_template

app = Flask(__name__)

db = [{"Title":"FirstTitle", "Author":"FirstAuthor", "Content": "xx"},
      {"Title":"SecondTitle", "Author":"SecondAuthor", "Content" : "aa"},
      {"Title":"ThirdTitle", "Author":"ThirdAuthor", "Content" : "bbc"}]

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html", database=db)

@app.route('/item/<int:index>')
def content(index):
    return render_template("Content.html", current=db[index])

if __name__ == '__main__':
    app.run('localhost', 4449)