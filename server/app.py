from flask import Flask, request, jsonify, abort
from flask_migrate import Migrate
from models import db, Exercise, Workout, WorkoutExercise
from schemas import ExerciseSchema, WorkoutSchema, WorkoutExerciseSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Schema Instatiation
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)

# Workout Routes
@app.route('/workouts', methods=['GET'])
def get_workouts():
  workouts = Workout.query.all()
  return workouts_schema.dump(workouts), 200

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
  workout = Workout.query.get_or_404(id)
  return workout_schema.dump(workout), 200

@app.route('/workouts', methods=['POST'])
def create_workout():
  data = request.get_json()
  try:
    validated = workout_schema.load(data)
    workout = Workout(**validated)
    db.session.add(workout)
    db.session.commit()
    return workout_schema.dump(workout), 201
  except Exception as e:
    db.session.rollback()
    return {"error": str(e)}, 400

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
  workout = Workout.query.get_or_404(id)
  try:
    db.session.delete(workout)
    db.session.commit()
    return {}, 204
  except Exception as e:
    db.session.rollback()
    return {"error": str(e)}, 400


# Exercise Routes
@app.route('/exercises', methods=['GET'])
def get_exercises():
  exercises = Exercise.query.all()
  return exercises_schema.dump(exercises), 200

@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
  exercise = Exercise.query.get_or_404(id)
  return exercise_schema.dump(exercise), 200

@app.route('/exercises', methods=['POST'])
def create_exercise():
  data = request.get_json()
  try:
    validated = exercise_schema.load(data)
    exercise = Exercise(**validated)
    db.session.add(exercise)
    db.session.commit()
    return exercise_schema.dump(exercise), 201
  except Exception as e:
    db.session.rollback()
    return {"error": str(e)}, 400

@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
  exercise = Exercise.query.get_or_404(id)
  try:
    db.session.delete(exercise)
    db.session.commit()
    return {}, 204
  except Exception as e:
    db.session.rollback()
    return {"error": str(e)}, 400

# Add Exercise to Workout (Join Route)
@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
  data = request.get_json() or {}
  try:
    # Ensure workout and exercise exist
    Workout.query.get_or_404(workout_id)
    Exercise.query.get_or_404(exercise_id)
    # Get join table details
    reps = data.get('reps')
    sets = data.get('sets')
    duration_seconds = data.get('duration_seconds')
    # Create join table record
    we = WorkoutExercise(
      workout_id=workout_id,
      exercise_id=exercise_id,
      reps=reps,
      sets=sets,
      duration_seconds=duration_seconds
    )
    db.session.add(we)
    db.session.commit()
    return workout_exercise_schema.dump(we), 201
  except Exception as e:
    db.session.rollback()
    return {"error": str(e)}, 400
  
# Error Handling
@app.errorhandler(404)
def not_found(e):
  return {"error": "Resource not found"}, 404

if __name__ == '__main__':
  app.run(port=5555, debug=True)