from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Role(db.Model):
    id = db.column(db.Integer, primary_key=True, unique=True)
    roleType=db.column(db.String,unique=True)

    def __repr__(self) -> str:
        return f'<Role: {self.id}, {self.roleType} '

class  User(db.Model):
    id = db.column(db.Integer, primary_key=True, unique=True)
    email = db.column(db.String(120), unique=True)
    phoneNumber = db.column(db.String)
    firstName= db.column(db.String(12))
    lastName= db.column(db.String(12))
    role= db.column(db.Integer, default=0)
    
    def __repr__(self) -> str:
        return f'<User: {self.email}, {self.firstName}, {self.lastName}, {self.phoneNumber}>'
        

    
