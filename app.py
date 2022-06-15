from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app) 

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(300))
    completed = db.Column(db.Boolean, default=False)

db.create_all()

sample_todo= Todos(task = "Sample todo",completed = False)
db.session.add(sample_todo)
db.session.commit()

@app.route('/add')
def add():
    return  'Added a new todo'

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')