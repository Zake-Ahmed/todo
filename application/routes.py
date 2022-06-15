from application import app, db
from application.models import Todos


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