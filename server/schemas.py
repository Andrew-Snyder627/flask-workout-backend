from marshmallow import Schema, fields, validates, ValidationError

class ExerciseSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  category = fields.Str(required=True)
  equipment_needed = fields.Bool(required=True)

  @validates('category')
  def validate_category(self, value):
    if value.lower() not in ['strength', 'cardio', 'mobility']:
      raise ValidationError('Invalid category. Choose strength, cardio, or mobility.')
    
class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()
    workout_exercises = fields.Nested(WorkoutExerciseSchema, many=True)