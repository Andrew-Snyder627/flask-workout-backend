from app import app
from models import db, Exercise, Workout, WorkoutExercise
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create Exercises
    pushup = Exercise(name="Push-Up", category="strength", equipment_needed=False)
    squat = Exercise(name="Squat", category="strength", equipment_needed=False)
    plank = Exercise(name="Plank", category="mobility", equipment_needed=False)

    db.session.add_all([pushup, squat, plank])
    db.session.commit()

    # Create Workout
    workout1 = Workout(date=date(2025, 7, 26), duration_minutes=45, notes="Morning strength session")
    db.session.add(workout1)
    db.session.commit()

    # Add WorkoutExercises
    we1 = WorkoutExercise(workout_id=workout1.id, exercise_id=pushup.id, reps=12, sets=3)
    we2 = WorkoutExercise(workout_id=workout1.id, exercise_id=squat.id, reps=15, sets=3)
    db.session.add_all([we1, we2])
    db.session.commit()

    print("Seeded database!")
