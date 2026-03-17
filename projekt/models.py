from datetime import datetime

class Workout:
    def __init__(self, date, duration, calories, notes=""):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.duration = duration  # w minutach
        self.calories = calories
        self.notes = notes

    def __str__(self):
        return f"{self.__class__.__name__} | {self.date.date()} | {self.duration} min | {self.calories} kcal | {self.notes}"

    def __eq__(self, other):
        return self.date == other.date and self.duration == other.duration

    def __lt__(self, other):
        return self.date < other.date

class RunningWorkout(Workout):
    def __init__(self, date, duration, calories, distance, notes=""):
        super().__init__(date, duration, calories, notes)
        self.distance = distance  # w kilometrach

    def __str__(self):
        base = super().__str__()
        return f"{base} | {self.distance} km"

class CyclingWorkout(Workout):
    def __init__(self, date, duration, calories, distance, notes=""):
        super().__init__(date, duration, calories, notes)
        self.distance = distance  # w kilometrach

    def __str__(self):
        base = super().__str__()
        return f"{base} | {self.distance} km"

class SwimmingWorkout(Workout):
    def __init__(self, date, duration, calories, distance, notes=""):
        super().__init__(date, duration, calories, notes)
        self.distance = distance  # w kilometrach

    def __str__(self):
        base = super().__str__()
        return f"{base} | {self.distance} km"

class GymWorkout(Workout):
    def __init__(self, date, duration, calories, muscle_group, notes=""):
        super().__init__(date, duration, calories, notes)
        self.muscle_group = muscle_group

    def __str__(self):
        base = super().__str__()
        return f"{base} | {self.muscle_group}"


class YogaWorkout(Workout):
    def __init__(self, date, duration, calories, style, notes=""):
        super().__init__(date, duration, calories, notes)
        self.style = style

    def __str__(self):
        base = super().__str__()
        return f"{base} | {self.style}"
