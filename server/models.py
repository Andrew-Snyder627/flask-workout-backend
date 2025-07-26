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