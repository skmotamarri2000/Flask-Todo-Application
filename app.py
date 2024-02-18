from flask import Flask, render_template,request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STATIC_FOLDER'] = 'static' 

db = SQLAlchemy(app)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(1000))
    complete = db.Column(db.Boolean)

@app.route('/')
def home_page():

    # Displays all the todo items
    todo_list = Todo.query.all()
    return render_template('home.html', todo_list = todo_list)


# Route for adding the list of to ado items
@app.route("/add", methods = ["POST"])
def add():
    # adding New item
    title = request.form.get("title")
    new_todo = Todo(title = title, complete = False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home_page"))

# Route for updating the todo item as complted or not
@app.route("/update/<int:todo_id>")
def update(todo_id):
    #Updating the item
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home_page"))


# Route for deleting the todo items.
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    # Deleting the item
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home_page"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
