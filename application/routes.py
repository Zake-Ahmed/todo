from application import app, db
from application.models import Todos


@app.route('/add')
def add():
    return  'Added a new todo'