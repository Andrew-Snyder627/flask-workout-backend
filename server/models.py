from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Models will go here
class Exercise(db.Model):
  __tablename__ = 'exercises'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False, unique=True)
  category = db.Column(db.String, nullable=False)
  equipment_needed = db.Column(db.Boolean, nullable=False)

  # Relationships will be here

  def __repr__(self):
    return f"<Exercise {self.name}>"
  
class Workout(db.Model):
  __tablename__ = 'workouts'

  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date, nullable=False)
  duration_minutes = db.Column(db.Integer, nullable=False)
  notes = db.Column(db.Text)

  # Relationships will go here

  def __repr__(self):
    return f"<Workout {self.id} on {self.date}>"
  
