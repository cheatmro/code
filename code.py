import tkinter as tk
from tkinter import messagebox

def on_click():
    balik_btn.pack()  # Показать кнопку Балик

def on_balik():
    messagebox.showinfo("Сообщение", "Нажата кнопка Балик!")

root = tk.Tk()
root.title("Кнопки Клик и Балик")

click_btn = tk.Button(root, text="Клик", command=on_click)
click_btn.pack(pady=10)

balik_btn = tk.Button(root, text="Балик", command=on_balik)
# Скрываем кнопку Балик изначально (не упаковываем)
# balik_btn.pack() не вызываем

root.mainloop()
