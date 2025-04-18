# main.py

import tkinter as tk
from tkinter import ttk, messagebox
from pet import Pet

class PetApp(tk.Tk):
    def __init__(self, pet_name):
        super().__init__()
        self.title(pet_name)
        self.geometry("400x350")
        self.resizable(False, False)

        # Instantiate pet
        self.pet = Pet(pet_name)

        # --- Stat Bars ---
        self.stat_bars = {}
        for i, stat in enumerate(("hunger", "energy", "happiness")):
            lbl = ttk.Label(self, text=stat.capitalize() + ":")
            lbl.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            bar = ttk.Progressbar(self, length=200, maximum=Pet.MAX_STAT, mode="determinate")
            bar.grid(row=i, column=1, padx=5, pady=5)
            self.stat_bars[stat] = bar

        # --- Action Buttons ---
        actions = [
            ("Eat 🍽️", self.eat),
            ("Play 🎾", self.play),
            ("Sleep 🛏️", self.sleep)
        ]
        for idx, (text, cmd) in enumerate(actions):
            btn = ttk.Button(self, text=text, command=cmd)
            btn.grid(row=3, column=idx, padx=10, pady=15)

        # --- Trick Trainer ---
        self.trick_entry = ttk.Entry(self)
        self.trick_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        train_btn = ttk.Button(self, text="Train 🏅", command=self.train)
        train_btn.grid(row=4, column=2, padx=5, pady=5)

        show_btn = ttk.Button(self, text="Show Tricks ✨", command=self.show_tricks)
        show_btn.grid(row=5, column=0, columnspan=3, pady=5)

        # Initial fill
        self.update_bars()

    def update_bars(self):
        """Refresh the progress bars to reflect current pet stats."""
        for stat, bar in self.stat_bars.items():
            bar['value'] = getattr(self.pet, stat)

    def eat(self):
        self.pet.eat()
        self.update_bars()

    def play(self):
        self.pet.play()
        self.update_bars()

    def sleep(self):
        self.pet.sleep()
        self.update_bars()

    def train(self):
        trick = self.trick_entry.get().strip()
        if trick:
            self.pet.train(trick)
            self.trick_entry.delete(0, tk.END)

    def show_tricks(self):
        tricks = self.pet.tricks
        if tricks:
            messagebox.showinfo("ShakaholaKenya's Tricks", "I know: " + ", ".join(tricks))
        else:
            messagebox.showwarning("ShakaholaKenya's Tricks", "No tricks learned yet.")

if __name__ == "__main__":
    app = PetApp("ShakaholaKenya")
    app.mainloop()
