from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

# Models will go here
class Exercise(db.Model):
  __tablename__ = 'exercises'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False, unique=True)
  category = db.Column(db.String, nullable=False)
  equipment_needed = db.Column(db.Boolean, nullable=False)

  # Relationships will be here
  workout_exercises = db.relationship('WorkoutExercise', backref='exercise', cascade="all, delete-orphan")
  workouts = db.relationship(
    'Workout',
    secondary='workout_exercises',
    back_populates='exercises',
    viewonly=True
  )

  # Validations
  @validates('name')
  def validate_name(self, key, value):
    if not value or not value.strip():
      raise ValueError("Exercise name must not be empty")
    return value

  @validates('category')
  def validate_category(self, key, value):
    if value.lower() not in ['strength', 'cardio', 'mobility']:
      raise ValueError("Category must be strength, cardio, or mobility")
    return value


  def __repr__(self):
    return f"<Exercise {self.name}>"
  
class Workout(db.Model):
  __tablename__ = 'workouts'

  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date, nullable=False)
  duration_minutes = db.Column(db.Integer, nullable=False)
  notes = db.Column(db.Text)

  # Relationships will go here
  workout_exercises = db.relationship('WorkoutExercise', backref='workout', cascade="all, delete-orphan")
  exercises = db.relationship(
    'Exercise',
      secondary='workout_exercises',
      back_populates='workouts',
      viewonly=True
  )

  # Validations
  @validates('duration_minutes')
  def validate_duration(self, key, value):
    if value is None or value < 1:
        raise ValueError("Duration must be at least 1 minute")
    return value
  

  def __repr__(self):
    return f"<Workout {self.id} on {self.date}>"
  
class WorkoutExercise(db.Model):
  __tablename__ = 'workout_exercises'

  id = db.Column(db.Integer, primary_key=True)
  workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
  reps = db.Column(db.Integer)
  sets = db.Column(db.Integer)
  duration_seconds = db.Column(db.Integer)

  # No need for relationships here, handled via relationships above

  def __repr__(self):
    return f"<WorkoutExercise W:{self.workout_id} E:{self.exercise_id}>"
  
