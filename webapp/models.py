```python
from flask_sqlalchemy import SQLAlchemy
from webapp import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Patent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Patent %r>' % self.title

class CostEstimate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patent_id = db.Column(db.Integer, db.ForeignKey('patent.id'), nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<CostEstimate %r>' % self.cost
```