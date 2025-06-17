import tkinter as tk
import random

def spin_roulette():
    result = random.randint(0, 36)
    result_label.config(text=f"Выпало число: {result}")

root = tk.Tk()
root.title("Рулетка")

spin_button = tk.Button(root, text="Крутить", command=spin_roulette, font=("Arial", 14), width=10)
spin_button.pack(pady=20)

result_label = tk.Label(root, text="Нажмите кнопку, чтобы крутить", font=("Arial", 16))
result_label.pack(pady=20)

root.mainloop()
