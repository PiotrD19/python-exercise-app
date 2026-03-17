class User:
    def __init__(self, name):
        self.name = name
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def remove_workout(self, index):
        if 0 <= index < len(self.workouts):
            del self.workouts[index]

    def manage_workouts(self):
        for i, w in enumerate(self.workouts):
            print(f"[{i}] {w}")

    def filter_by_type(self, workout_type):
        return [w for w in self.workouts if type(w).__name__ == workout_type]

    def total_calories(self):
        return sum(w.calories for w in self.workouts)

