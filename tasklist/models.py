from tasklist import db,login_mgr
from tasklist import bcrypt
from flask_login import UserMixin

@login_mgr.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable = False, unique=True)
    email = db.Column(db.String(length=80), nullable = False, unique=True)
    name = db.Column(db.String(length=50))
    password_hash = db.Column(db.String(length=60), nullable = False)
    task_items = db.relationship('TaskItem', backref='owned_user', lazy=True)

    def __repr__(self):
        return f'{self.name}'

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def validate_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

class TaskItem(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String(length=50), nullable = False, unique=True)
    status = db.Column(db.String(length=10), nullable = False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        #return f'Task: {self.description}'
        return f'{self.description}'