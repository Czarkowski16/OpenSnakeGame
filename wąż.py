import tkinter as tk
import random
import time

class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = [(0, 0)]
        self.food = self.generate_food()
        self.direction = (1, 0)
        self.score = 0

        # Set up the Tkinter window
        self.root = tk.Tk()
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(self.root, width=self.width * 30, height=self.height * 30, bg="black")
        self.canvas.pack()

    def draw_board(self):
        self.canvas.delete("all")

        for coord in self.snake:
            x, y = coord
            self.canvas.create_rectangle(x * 30, y * 30, (x + 1) * 30, (y + 1) * 30, fill="green")

        x, y = self.food
        self.canvas.create_rectangle(x * 30, y * 30, (x + 1) * 30, (y + 1) * 30, fill="red")

        self.canvas.create_text(50, 10, text=f"Score: {self.score}", anchor=tk.NW, fill="white")

    def generate_food(self):
        food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        while food in self.snake:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        return food

    def get_user_input(self, event):
        key = event.keysym
        if key == 'w' and self.direction != (0, 1):
            self.direction = (0, -1)  # Up
        elif key == 'a' and self.direction != (1, 0):
            self.direction = (-1, 0)  # Left
        elif key == 's' and self.direction != (0, -1):
            self.direction = (0, 1)   # Down
        elif key == 'd' and self.direction != (-1, 0):
            self.direction = (1, 0)   # Right

    def update_snake(self):
        head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        self.snake = [head] + self.snake[:-1]

    def check_collision(self):
        if self.snake[0] == self.food:
            self.snake.append(self.food)
            self.food = self.generate_food()
            self.score += 1
        elif (
            not (0 <= self.snake[0][0] < self.width) or
            not (0 <= self.snake[0][1] < self.height) or
            self.snake[0] in self.snake[1:]
        ):
            print("Game Over! Your score: {}".format(self.score))
            self.root.destroy()
            return True
        return False

    def run_game(self):
        self.root.bind("<Key>", self.get_user_input)

        while True:
            self.draw_board()
            self.root.update_idletasks()
            self.root.update()

            self.update_snake()

            if self.check_collision():
                break

            time.sleep(0.2)  # Adjust the speed of the game

# Initialize and run the game
snake_game = SnakeGame(width=20, height=15)
snake_game.run_game()
