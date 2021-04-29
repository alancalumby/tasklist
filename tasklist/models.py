from tasklist import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable = False, unique=True)
    email = db.Column(db.String(length=80), nullable = False, unique=True)
    name = db.Column(db.String(length=50), nullable = False)
    password_hash = db.Column(db.String(length=60), nullable = False)
    task_items = db.relationship('TaskItem', backref='owned_user', lazy=True)

    def __repr__(self):
        return f'{self.name}'

class TaskItem(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String(length=50), nullable = False, unique=True)
    status = db.Column(db.String(length=10), nullable = False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        #return f'Task: {self.description}'
        return f'{self.description}'