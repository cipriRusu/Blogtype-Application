from flask import Flask, render_template, request, redirect
from models.blog_post import BlogPost
from mock_db import MockDatabase

app = Flask(__name__)
mock_database = MockDatabase()

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html", database=mock_database)

@app.route('/item/<uuid:current_index>')
def content(current_index):
    return render_template("Content.html", current=mock_database.GetByIndex(current_index))

@app.route('/addItem', methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        mock_database.AddPost(
            BlogPost(request.form['NameInput'], 
                     request.form['AuthorInput'], 
                     request.form['ContentInput']))
        return redirect('/')
    return render_template("AddItem.html")

@app.route('/removeItem/<uuid:current_index>')
def remove_item(current_index):
    mock_database.Remove(current_index)
    return redirect('/')

@app.route('/updateItem/<uuid:current_index>', methods=["GET", "POST"])
def update_item(current_index):
    if request.method == "GET":
        return render_template("UpdateItem.html", current=mock_database.GetByIndex(current_index))

    if request.method == "POST":
        mock_database.Remove(current_index)

        mock_database.AddPost(BlogPost(
            request.form['NameInput'],
            request.form['AuthorInput'],
            request.form['ContentInput']))

    return redirect('/')

if __name__ == '__main__':
    app.run('localhost', 4449)
