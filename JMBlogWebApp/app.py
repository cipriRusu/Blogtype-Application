from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

db = [{"Title":"FirstTitle", "Author":"FirstAuthor", "Content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."},
      {"Title":"SecondTitle", "Author":"SecondAuthor", "Content" : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."},
      {"Title":"ThirdTitle", "Author":"ThirdAuthor", "Content" : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."}]

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html", database=db)

@app.route('/item/<int:index>')
def content(index):
    return render_template("Content.html", current=db[index])

@app.route('/addItem', methods=["GET", "POST"])
def addItem():
    if request.method == "POST":
        current = {
            'Title': request.form['NameInput'], 
            'Author': request.form['AuthorInput'], 
            'Content': request.form['ContentInput']}
        db.append(current)
        return redirect('/')
    else:
        return render_template("AddItem.html");

if __name__ == '__main__':
    app.run('localhost', 4449)