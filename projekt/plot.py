import matplotlib.pyplot as plt

def show_calorie_chart(workouts):
    if not workouts:
        print("Brak danych.")
        return

    workouts_sorted = sorted(workouts, key=lambda x: x.date)
    dates = [w.date.strftime("%Y-%m-%d") for w in workouts_sorted]
    calories = [w.calories for w in workouts_sorted]

    plt.figure(num="Wykres", figsize=(10, 5), facecolor="#f7f7f7")
    plt.plot(dates, calories, marker='o')
    plt.xticks(rotation=45)
    plt.title(f"Kalorie spalane w czasie (łącznie: {sum(calories)} kcal)")
    plt.grid(axis = 'y')
    plt.xlabel("Data")
    plt.ylabel("Kalorie")
    plt.tight_layout()
    plt.show()
