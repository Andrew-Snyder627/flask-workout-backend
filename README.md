# Flask Workout Application Backend

## Project Description

This repository contains the backend API for a workout tracking application designed for personal trainers and fitness enthusiasts. Built with Flask, SQLAlchemy, and Marshmallow, the API enables creation and management of workouts, exercises, and workout sessions. The backend enforces robust data validation and constraints to ensure data integrity. All endpoints have been thoroughly tested using Postman.

---

## Features

- Workouts: Create, view, and delete workouts with custom notes and durations.
- Exercises: Manage reusable exercises with categories and equipment tracking.
- Workout Logging: Assign any exercise to any workout, with detailed set/rep/duration info.
- Validations: Multiple layers of validation using SQLAlchemy, Marshmallow, and database constraints.
- Clean Architecture: Modular, maintainable codebase following industry best practices.

---

## Installation Instructions

1. Clone the Repository

```
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME/server
```

2. Install Dependencies with Pipenv

```
   pipenv install
```

3. Initialize the Database

```
   pipenv shell
   export FLASK_APP=app.py
   flask db upgrade
```

4. Seed the Database with Sample Data

```
   python seed.py
```

5. Run the Application

```
   flask run
```

The server will run on http://localhost:5555

---

## API Endpoints

```
| Method | Endpoint                                                                | Description                                                           |
|--------|-------------------------------------------------------------------------|-----------------------------------------------------------------------|
| GET    | /workouts                                                              | List all workouts                                                     |
| GET    | /workouts/<id>                                                         | Retrieve a single workout and its associated exercises                |
| POST   | /workouts                                                              | Create a new workout (date, duration_minutes, notes)                  |
| DELETE | /workouts/<id>                                                         | Delete a workout and its associated WorkoutExercises                  |
| GET    | /exercises                                                             | List all exercises                                                    |
| GET    | /exercises/<id>                                                        | Retrieve a single exercise                                            |
| POST   | /exercises                                                             | Create a new exercise (name, category, equipment_needed)              |
| DELETE | /exercises/<id>                                                        | Delete an exercise and its associated WorkoutExercises                |
| POST   | /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises       | Add an exercise to a workout, including reps/sets/duration            |

```

All POST/DELETE requests require JSON bodies where applicable.

---

## Example Usage

Create an Exercise

POST /exercises
Content-Type: application/json

```
{
"name": "Deadlift",
"category": "strength",
"equipment_needed": true
}
```

Create a Workout
POST /workouts
Content-Type: application/json

```
{
"date": "2025-08-01",
"duration_minutes": 60,
"notes": "Full body strength session"
}
```

Add an Exercise to a Workout

POST /workouts/1/exercises/1/workout_exercises
Content-Type: application/json

```
{
"reps": 10,
"sets": 4,
"duration_seconds": 0
}
```

---

## Validations & Constraints

- Table Constraints: Unique exercise names; required fields cannot be null.
- Model Validations: Exercise category must be 'strength', 'cardio', or 'mobility'. Workout duration must be at least 1 minute. Exercise name must not be empty.
- Schema Validations: Additional Marshmallow checks for required fields and valid categories.

---

## Testing

All endpoints have been tested using Postman.
You can import the endpoints and JSON payloads into Postman for your own testing, or use curl commands. Error handling and validation have been verified for all input types.

---

## Project Structure

```
server/
├── app.py
├── models.py
├── schemas.py
├── seed.py
├── migrations/
├── app.db
├── Pipfile
├── Pipfile.lock
```

---

## Author

Andrew Snyder

---

## License

This project is for educational purposes as part of the Flatiron School of Software Engineering.
