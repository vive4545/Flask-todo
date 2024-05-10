from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# for database creating models
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Todo %r>' % self.id

# Create tables inside the application context
with app.app_context():
    db.create_all()


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#crud (create)
@app.route('/', methods =['GET','POST'])

def products():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        todo = Todo(name = name, email=email,phone = phone,address = address)
        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()
    return render_template('clientdetails.html',allTodo=allTodo)
#crud(read)
@app.route('/show')
def show():
    allTodo = Todo.query.all()
    print(allTodo)
    return render_template('clientdetails.html',allTodo=allTodo)

#crud(update)
@app.route('/update/<int:id>')
def update(id):
    allTodo = Todo.query.filter_by(id=id).first()
    print(allTodo)
    return render_template('update.html',allTodo=allTodo)


# crud(delete)
@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


if __name__== "__main__":
    app.run(debug=True)
