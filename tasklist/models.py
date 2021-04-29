from tasklist import db

class TaskItem(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String(length=50), nullable = False, unique=True)
    status = db.Column(db.String(length=10), nullable = False)

    def __repr__(self):
        #return f'Task: {self.description}'
        return f'{self.description}'