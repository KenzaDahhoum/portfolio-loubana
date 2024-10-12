from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(100), nullable=False)
    degree = db.Column(db.String(100), nullable=False)
    field_of_study = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(50))
    end_date = db.Column(db.String(50))

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(50))
    end_date = db.Column(db.String(50))
    location = db.Column(db.String(100))
    description = db.Column(db.Text)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(100))
    link = db.Column(db.String(200))

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # Add category to the Skill model
