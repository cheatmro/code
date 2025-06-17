import tkinter as tk

class DinoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра Динозаврик")
        self.width = 600
        self.height = 200
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        # Динозаврик - прямоугольник
        self.dino_x = 50
        self.dino_y = 150
        self.dino_width = 40
        self.dino_height = 40
        self.dino = self.canvas.create_rectangle(self.dino_x, self.dino_y - self.dino_height, self.dino_x + self.dino_width, self.dino_y, fill="green")

        # Параметры прыжка
        self.is_jumping = False
        self.jump_speed = 15
        self.gravity = 3
        self.jump_velocity = 0

        # Препятствие
        self.obs_width = 20
        self.obs_height = 40
        self.obs_x = self.width
        self.obs_y = 150
        self.obstacle = self.canvas.create_rectangle(self.obs_x, self.obs_y - self.obs_height, self.obs_x + self.obs_width, self.obs_y, fill="red")

        # Управление
        self.root.bind("<space>", self.jump)

        # Запускаем игру
        self.game_over = False
        self.update_game()

    def jump(self, event):
        if not self.is_jumping and not self.game_over:
            self.is_jumping = True
            self.jump_velocity = -self.jump_speed

    def update_game(self):
        if self.game_over:
            self.canvas.create_text(self.width/2, self.height/2, text="Игра окончена!", font=("Arial", 24), fill="red")
            return

        # Прыжок динозаврика
        if self.is_jumping:
            self.canvas.move(self.dino, 0, self.jump_velocity)
            self.jump_velocity += self.gravity

            # Проверка, достиг ли динозаврик земли
            coords = self.canvas.coords(self.dino)
            if coords[3] >= self.dino_y:
                # Вернуть на землю
                self.canvas.move(self.dino, 0, self.dino_y - coords[3])
                self.is_jumping = False

        # Движение препятствия
        self.obs_x -= 10
        if self.obs_x < -self.obs_width:
            self.obs_x = self.width
        self.canvas.coords(self.obstacle, self.obs_x, self.obs_y - self.obs_height, self.obs_x + self.obs_width, self.obs_y)

        # Проверка столкновения
        dino_coords = self.canvas.coords(self.dino)
        obs_coords = self.canvas.coords(self.obstacle)

        if self.check_collision(dino_coords, obs_coords):
            self.game_over = True

        self.root.after(50, self.update_game)

    def check_collision(self, rect1, rect2):
        # rect = [x1, y1, x2, y2]
        return not (rect1[2] < rect2[0] or rect1[0] > rect2[2] or rect1[3] < rect2[1] or rect1[1] > rect2[3])

if __name__ == "__main__":
    root = tk.Tk()
    game = DinoGame(root)
    root.mainloop()
