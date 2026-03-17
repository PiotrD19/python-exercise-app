import tkinter as tk
from tkinter import messagebox
from models import RunningWorkout, CyclingWorkout, SwimmingWorkout, GymWorkout, YogaWorkout
from tracker import User
from storage import save_to_csv, load_from_csv
from plot import show_calorie_chart

class WorkoutApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Śledzenie treningów")
        self.root.configure(bg="#f7f7f7")
        self.root.resizable(False, False)

        self.user = User("Janek")
        self.user.workouts = load_from_csv("data.csv")

        self.sort_date_ascending = True
        self.sort_calories_descending = True

        self.type_var = tk.StringVar(value="Bieganie")

        # Główna ramka formularza
        form = tk.Frame(root, bg="#f7f7f7")
        form.pack(pady=20)

        self._add_labeled_entry(form, "Typ treningu:", 0)
        tk.OptionMenu(form, self.type_var, "Bieganie", "Jazda rowerem", "Pływanie", "Siłownia", "Joga").grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        self.date_entry = self._add_labeled_entry(form, "Data (YYYY-MM-DD):", 1)
        self.duration_entry = self._add_labeled_entry(form, "Czas trwania (min):", 2)
        self.calories_entry = self._add_labeled_entry(form, "Kalorie:", 3)
        self.extra_entry = self._add_labeled_entry(form, "Dodatkowe dane(km / grupa mięśni / styl jogi):", 4)
        self.notes_entry = self._add_labeled_entry(form, "Notatki:", 5)

        # Przyciski
        button_frame = tk.Frame(root, bg="#f7f7f7")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Dodaj trening", command=self.add_workout, width=20).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Zarządzaj treningami", command=self.manage_workouts, width=20).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Pokaż wykres", command=self.plot, width=20).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Zapisz dane", command=self.save, width=20).grid(row=0, column=3, padx=5)

    def _add_labeled_entry(self, frame, label_text, row):
        label = tk.Label(frame, text=label_text, font=("Arial", 11), bg="#f7f7f7")
        label.grid(row=row, column=0, sticky="e", padx=10, pady=5)
        entry = tk.Entry(frame, width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    def add_workout(self):
        try:
            wtype = self.type_var.get()
            date = self.date_entry.get()
            duration = int(self.duration_entry.get())
            calories = int(self.calories_entry.get())
            extra = self.extra_entry.get()
            notes = self.notes_entry.get()

            if wtype == "Bieganie":
                w = RunningWorkout(date, duration, calories, float(extra), notes)
            elif wtype == "Jazda rowerem":
                w = CyclingWorkout(date, duration, calories, float(extra), notes)
            elif wtype == "Pływanie":
                w = SwimmingWorkout(date, duration, calories, float(extra), notes)
            elif wtype == "Siłownia":
                w = GymWorkout(date, duration, calories, extra, notes)
            elif wtype == "Joga":
                w = YogaWorkout(date, duration, calories, extra, notes)
            else:
                raise ValueError("Nieznany typ treningu")

            self.user.add_workout(w)
            messagebox.showinfo("Sukces", "Dodano trening!")

        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    def manage_workouts(self):
        def update_display(workouts):
            text.config(state=tk.NORMAL)
            text.delete(1.0, tk.END)
            for i, w in enumerate(workouts):
                text.insert(tk.END, f"[{i}] {w}\n")
            text.config(state=tk.DISABLED)

        def delete_selected():
            try:
                index = int(entry.get())
                self.user.remove_workout(index)
                update_display(self.user.workouts)
                entry.delete(0, tk.END)
                messagebox.showinfo("Sukces", "Usunięto trening!")
            except Exception as e:
                messagebox.showerror("Błąd", str(e))

        def sort_by_date():
            self.sort_date_ascending = not self.sort_date_ascending
            self.user.workouts.sort(key=lambda w: w.date, reverse=not self.sort_date_ascending)
            update_display(self.user.workouts)

        def sort_by_calories():
            self.sort_calories_descending = not self.sort_calories_descending
            self.user.workouts.sort(key=lambda w: w.calories, reverse=self.sort_calories_descending)
            update_display(self.user.workouts)

        top = tk.Toplevel(self.root)
        top.title("Zarządzanie treningami")


        text_frame = tk.Frame(top)
        text_frame.pack(pady=10)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text = tk.Text(text_frame, height=15, width=100, font=("Courier", 10), yscrollcommand=scrollbar.set)
        text.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar.config(command=text.yview)

        sort_frame = tk.Frame(top)
        sort_frame.pack()

        tk.Button(sort_frame, text="Sortuj po dacie ↑↓", command=sort_by_date).pack(side=tk.LEFT, padx=5)
        tk.Button(sort_frame, text="Sortuj po kaloriach ↑↓", command=sort_by_calories).pack(side=tk.LEFT, padx=5)

        update_display(self.user.workouts)

        tk.Label(top, text="Podaj numer treningu do usunięcia:").pack()
        entry = tk.Entry(top)
        top.resizable(False, False)
        entry.pack()
        tk.Button(top, text="Usuń trening", command=delete_selected).pack(pady=10)

    def plot(self):
        show_calorie_chart(self.user.workouts)

    def save(self):
        save_to_csv("data.csv", self.user.workouts)
        messagebox.showinfo("Zapisano", "Dane zapisane do pliku.")
