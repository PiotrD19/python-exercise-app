import csv
from models import RunningWorkout,CyclingWorkout, SwimmingWorkout, GymWorkout, YogaWorkout

def save_to_csv(filename, workouts):
    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f)
        for w in workouts:
            writer.writerow([type(w).__name__, w.date.strftime("%Y-%m-%d"), w.duration, w.calories, getattr(w, 'distance', '') or getattr(w, 'muscle_group', '') or getattr(w, 'style', ''), w.notes])

def load_from_csv(filename):
    workouts = []
    try:
        with open(filename, mode="r") as f:
            reader = csv.reader(f)
            for row in reader:
                w_type, date, duration, calories, extra, notes = row
                if w_type == "RunningWorkout":
                    workouts.append(RunningWorkout(date, int(duration), int(calories), float(extra), notes))
                elif w_type == "CyclingWorkout":
                    workouts.append(CyclingWorkout(date, int(duration), int(calories), float(extra), notes))
                elif w_type == "SwimmingWorkout":
                    workouts.append(SwimmingWorkout(date, int(duration), int(calories), float(extra), notes))
                elif w_type == "GymWorkout":
                    workouts.append(GymWorkout(date, int(duration), int(calories), extra, notes))
                elif w_type == "YogaWorkout":
                    workouts.append(YogaWorkout(date, int(duration), int(calories), extra, notes))
    except FileNotFoundError:
        print("Plik nie istnieje – zostanie utworzony przy zapisie.")
    return workouts
