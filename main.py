from tkinter import *
import tkinter as tk

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.button_1 = tk.Button(self.root, width=5, justify="center", font=('Calibri 20'), bg="white", command=lambda: [self.on_button_click(1), self.how_many_clicks(), self.get_button_text()])
        self.button_2 = tk.Button(self.root, width=5, justify="center", font=('Calibri 20'), bg="white", command=lambda: [self.on_button_click(2), self.how_many_clicks(), self.get_button_text()])
        self.button_3 = tk.Button(self.root, width=5, justify="center", font=('Calibri 20'), bg="white", command=lambda: [self.on_button_click(3), self.how_many_clicks(), self.get_button_text()])
        self.button_4 = tk.Button(self.root, width=5, justify="center", font=('Calibri 20'), bg="white", command=lambda: [self.on_button_click(4), self.how_many_clicks(), self.get_button_text()])
        self.button_5 = tk.Button(self.root, width=5, justify="center", font=('Calibri 20'), bg="white", command=lambda: [self.on_button_click(5), self.how_many_clicks(), self.get_button_text()])
        self.button_6 = tk.Button(self.root, width=5, justify="center", font=('Calibri 20'), bg="white", command=lambda: [self.on_button_click(6), self.how_many_clicks(), self.get_button_text()])
        self.button_7 = tk.Button(self.root, width=5, justify="center", font=('Calibri 20'), bg="white", command=lambda: [self.on_button_click(7), self.how_many_clicks(), self.get_button_text()])
        self.button_8 = tk.Button(self.root, width=5, justify="center", font=('Calibri 20'), bg="white", command=lambda: [self.on_button_click(8), self.how_many_clicks(), self.get_button_text()])
        self.button_9 = tk.Button(self.root, width=5, justify="center", font=('Calibri 20'), bg="white", command=lambda: [self.on_button_click(9), self.how_many_clicks(), self.get_button_text()])
        self.reset_button = tk.Button(self.root, text="Reset", width=25, justify="center", font=('Calibri 14'), command=self.reset_game)

        self.button_1.grid(column=0, row=0)
        self.button_2.grid(column=1, row=0)
        self.button_3.grid(column=2, row=0)
        self.button_4.grid(column=0, row=1)
        self.button_5.grid(column=1, row=1)
        self.button_6.grid(column=2, row=1)
        self.button_7.grid(column=0, row=2)
        self.button_8.grid(column=1, row=2)
        self.button_9.grid(column=2, row=2)
        self.reset_button.grid(row=3, columnspan=3)

        self.choices = ["X", "0", "X", "0", "X", "0", "X", "0", "X"]

        self.count = 0
        self.root.mainloop()

    def how_many_clicks(self):
        self.count = self.count + 1

    def disable_all_buttons(self):
        self.button_1.config(state="disabled")
        self.button_2.config(state="disabled")
        self.button_3.config(state="disabled")
        self.button_4.config(state="disabled")
        self.button_5.config(state="disabled")
        self.button_6.config(state="disabled")
        self.button_7.config(state="disabled")
        self.button_8.config(state="disabled")
        self.button_9.config(state="disabled")

    def get_button_text(self):
        text_button_1 = self.button_1.cget("text")
        text_button_2 = self.button_2.cget("text")
        text_button_3 = self.button_3.cget("text")
        text_button_4 = self.button_4.cget("text")
        text_button_5 = self.button_5.cget("text")
        text_button_6 = self.button_6.cget("text")
        text_button_7 = self.button_7.cget("text")
        text_button_8 = self.button_8.cget("text")
        text_button_9 = self.button_9.cget("text")

        if text_button_1 == text_button_2 == text_button_3 == "X" or text_button_1 == text_button_2 == text_button_3 == "0":
            self.button_1.config(bg="green")
            self.button_2.config(bg="green")
            self.button_3.config(bg="green")
            self.disable_all_buttons()
        elif text_button_4 == text_button_5 == text_button_6 == "X" or text_button_4 == text_button_5 == text_button_6 == "0":
            self.button_4.config(bg="green")
            self.button_5.config(bg="green")
            self.button_6.config(bg="green")
            self.disable_all_buttons()
        elif text_button_7 == text_button_8 == text_button_9 == "X" or text_button_7 == text_button_8 == text_button_9 == "0":
            self.button_7.config(bg="green")
            self.button_8.config(bg="green")
            self.button_9.config(bg="green")
            self.disable_all_buttons()
        elif text_button_1 == text_button_4 == text_button_7 == "X" or text_button_1 == text_button_4 == text_button_7 == "0":
            self.button_1.config(bg="green")
            self.button_4.config(bg="green")
            self.button_7.config(bg="green")
            self.disable_all_buttons()
        elif text_button_2 == text_button_5 == text_button_8 == "X" or text_button_2 == text_button_5 == text_button_8 == "0":
            self.button_2.config(bg="green")
            self.button_5.config(bg="green")
            self.button_8.config(bg="green")
            self.disable_all_buttons()
        elif text_button_3 == text_button_6 == text_button_9 == "X" or text_button_3 == text_button_6 == text_button_9 == "0":
            self.button_3.config(bg="green")
            self.button_6.config(bg="green")
            self.button_9.config(bg="green")
            self.disable_all_buttons()
        elif text_button_1 == text_button_5 == text_button_9 == "X" or text_button_1 == text_button_5 == text_button_9 == "0":
            self.button_1.config(bg="green")
            self.button_5.config(bg="green")
            self.button_9.config(bg="green")
            self.disable_all_buttons()
        elif text_button_3 == text_button_5 == text_button_7 == "X" or text_button_3 == text_button_5 == text_button_7 == "0":
            self.button_3.config(bg="green")
            self.button_5.config(bg="green")
            self.button_7.config(bg="green")
            self.disable_all_buttons()

    def on_button_click(self, button_id):
        if button_id == 1:
            self.button_1.config(text=self.choices[self.count], state="disabled")
        elif button_id == 2:
            self.button_2.config(text=self.choices[self.count], state="disabled")
        elif button_id == 3:
            self.button_3.config(text=self.choices[self.count], state="disabled")
        elif button_id == 4:
            self.button_4.config(text=self.choices[self.count], state="disabled")
        elif button_id == 5:
            self.button_5.config(text=self.choices[self.count], state="disabled")
        elif button_id == 6:
            self.button_6.config(text=self.choices[self.count], state="disabled")
        elif button_id == 7:
            self.button_7.config(text=self.choices[self.count], state="disabled")
        elif button_id == 8:
            self.button_8.config(text=self.choices[self.count], state="disabled")
        elif button_id == 9:
            self.button_9.config(text=self.choices[self.count], state="disabled")

    def reset_game(self):
        self.count = 0
        self.button_1.config(text="", state="normal", bg="white")
        self.button_2.config(text="", state="normal", bg="white")
        self.button_3.config(text="", state="normal", bg="white")
        self.button_4.config(text="", state="normal", bg="white")
        self.button_5.config(text="", state="normal", bg="white")
        self.button_6.config(text="", state="normal", bg="white")
        self.button_7.config(text="", state="normal", bg="white")
        self.button_8.config(text="", state="normal", bg="white")
        self.button_9.config(text="", state="normal", bg="white")

game = Game()
