from application import app, db
from application.models import Todos
from flask import render_template,redirect,url_for



@app.route('/add')
def add():

    
    return  'Added a new todo'

@app.route('/add/taskname/<task>')
def taskname(task):
    todo = Todos(task =task)
    db.session.add(todo)
    db.session.commit()
    return task

@app.route('/complete/<task>')
def complete(task):
    todo = Todos.query.filter_by(task=task).first()
    todo.completed=True
    db.session.commit()
    return str(todo.completed)

@app.route('/delete/<task>')
def delete(task):
    todo = Todos.query.filter_by(task=task).first()
    db.session.delete(todo)
    db.session.commit()
    return f'Deleted {task}'


@app.route('/update/<oldtask>/<newtask>')
def update(oldtask,newtask):
    todo = Todos.query.filter_by(task=oldtask).first()
    todo.task= newtask
    db.session.commit()
    return newtask

@app.route('/list')
def listB():
    list1=["ben", "harry", "bob", "jay", "matt", "bill","zake","ryan","ahmed"]
    list2=[]
    for user in list1:
        a=user[0].upper()
        user=a+user[1:]
        list2.append(user)
    return render_template('list.html',  listB=list2, letter="B")

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/task')
def readall():
    all_Users = Todos.query.all()
    return render_template('task.html', all_Users=all_Users)

@app.route('/home')
def home():
    return render_template('home.html')

     