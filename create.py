from application import db
from application.models import Todos
db.drop_all()
db.create_all()

sample_todo= Todos(task = "Sample todo",completed = False)
db.session.add(sample_todo)
db.session.commit()