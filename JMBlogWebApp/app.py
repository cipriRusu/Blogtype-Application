from flask import Flask, render_template, request, redirect
from models.BlogPost import BlogPost

app = Flask(__name__)

db = [BlogPost("FirstTitle", "FirstAuthor", "Lorem Ipsum is simply dummy , \
       'text of the printing and typesetting industry. Lorem Ipsum has been the industry's , \
       standard dummy text ever since the 1500s, when an unknown printer took a galley of , \
       type and scrambled it to make a type specimen book. It has survived not only five centuries, , \
       but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised, in the, \
       1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop , \
       publishing software like Aldus PageMaker including versions of Lorem Ipsum."),

      BlogPost("SecondTitle", "SecondAuthor", "Lorem Ipsum is simply dummy text of the, \
        printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since, \
        the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen , \
        book. It has survived not only five centuries, but also the leap into electronic typesetting, , \
        remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets , \
        containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker , \
        including versions of Lorem Ipsum."),

      BlogPost("ThirdTitle", "ThirdAuthor", "Lorem Ipsum is simply dummy text of the printing , \
      and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, , \
      when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived , \
      not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was, \
      popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently , \
      with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")]

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html", database=db)

@app.route('/item/<int:current_index>')
def content(current_index):
    return render_template("Content.html", current=db[current_index])

@app.route('/addItem', methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        db.append(BlogPost(
            request.form['NameInput'], 
            request.form['AuthorInput'], 
            request.form['ContentInput']))
        return redirect('/')

    return render_template("AddItem.html")

@app.route('/removeItem/<uuid:current_index>')
def remove_item(current_index):
    for element in db:
        if element.id == current_index:
            db.remove(element)
            return redirect('/')

    return redirect('/')

@app.route('/updateItem/<uuid:current_index>', methods=["GET", "POST"])
def update_item(current_index):
    if request.method == "GET":
        for element in db:
            if element.id == current_index:
                return render_template("UpdateItem.html", current=element)

    if request.method == "POST":
        for element in db:
            if element.id == current_index:
                db.remove(element)

        current = BlogPost(
            request.form['NameInput'], 
            request.form['AuthorInput'], 
            request.form['ContentInput'])
        db.append(current)
    return redirect('/')

if __name__ == '__main__':
    app.run('localhost', 4449)
