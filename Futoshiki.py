import tkinter as tk
import os
import sys
from tkinter import messagebox
from PIL import Image,ImageTk
import pygame
from tkinter import *

root = tk.Tk()
root.title("FUTOSHIKI")
root.geometry("1080x1080")


root.configure(bg='white')
welcome_label = tk.Label(root, text="FUTOSHIKI!", font=("Arial", 3))
bg = tk.PhotoImage(file="futo pic.png")
label1=Label(root,image=bg)
label1.place(x=0,y=0)
welcome_label.pack(pady=200)

def play():
    pygame.mixer.music.load('newfutosong.mp3')
    pygame.mixer.music.play()
    
def stop():
    pygame.mixer.music.stop()


start_button = tk.Button(root, text="Start Game", font=("Arial", 20), bg='Black', fg='white')
start_button.pack()
play_button = Button(root, text="Play Song", font=("Arial", 15),bg='Black', fg='white', command=play)
play_button.pack()

stop_button = Button(root, text="stop Song", font=("Arial", 15),bg='Black', fg='white', command=stop)
stop_button.pack()

pygame.mixer.init()


# Function to start the game
def start_game():  
    root = tk.Tk()
    root.title("Futoshiki Puzzle")
   # root.geometry("500x300")
   # root.config(bg="black")

    # Define the disabled cells
    disabled_cells = [(0,1),(0, 3), (0, 5), (1, 0),(1, 1),(1, 2), (1, 3), (1, 4),(1, 5),(1, 6), (1, 7), (3, 0),(3, 1),(3, 2), (3, 3), (3, 4),(3, 5),(3, 6), (3, 7),(5, 0),(5, 1),(5, 2), (5, 3), (5, 4),(5, 5),(5, 6), (5, 7),(2, 1),(2, 3),(2, 5), (4, 1), (4, 3),(4, 5),(6, 1), (6, 3), (6, 5)]

    # Create the grid cells
    for i in range(7):
        for j in range(7):
            if (i, j) in disabled_cells:
                entry = tk.Entry(root, width=5, state='disabled')
            else:
                entry = tk.Entry(root, width=5)
            entry.grid(row=i, column=j)

    # Add the inequality constraints
    constraints = [((0, 2),(2,2),  "^"), ((0, 6), (2, 6), "v"), ((4, 0), (4, 2), ">"), ((2, 4), (4, 4), "^"),((4, 6), (6, 6), "^")]
    for constraint in constraints:
        row1, col1 = constraint[0]
        row2, col2 = constraint[1]
        symbol = constraint[2]
        label = tk.Label(root, text=symbol)
        label.grid(row=(row1 + row2) // 2, column=(col1 + col2) // 2)

    # Input values for the puzzle
    input_values = { (4, 6): 3}

    # Set the input values in the puzzle
    for (row, col), value in input_values.items():
        entry = root.grid_slaves(row=row, column=col)[0]
        entry.insert(0, str(value))
        entry.config(state="disabled")

    def solve_puzzle():
        # Check that all entries contain a value between 1 and 4
        for i in range(7):
            for j in range(7):
                if (i, j) in disabled_cells:
                    continue
                entry = root.grid_slaves(row=i, column=j)[0]
                value = entry.get()
                if value:
                    if not value.isdigit() or int(value) not in range(1, 5):
                        messagebox.showerror("Error", "Value in cell ({}, {}) must be a number between 1 and 4".format(i, j))
                        return False
                else:
                    messagebox.showerror("error","({},{}) cell cant be empty".format(i,j))

        # Check that each row and column contains unique values
        for i in range(7):
            row_values = set()
            col_values = set()
            for j in range(7):
                if (i, j) in disabled_cells:
                    continue
                # Check row
                row_entry = root.grid_slaves(row=i, column=j)[0]
                row_value = row_entry.get()
                if row_value:
                    if row_value in row_values:
                        messagebox.showerror("Error", "Row {} contains duplicate values".format(i))
                        return False
                    row_values.add(row_value)
                # Check column
                col_entry = root.grid_slaves(row=j, column=i)[0]
                col_value = col_entry.get()
                if col_value:
                    if col_value in col_values:
                        messagebox.showerror("Error", "Column {} contains duplicate values".format(i))
                        return False
                    col_values.add(col_value)
        return True

    def check_constraints():
        # Check that all constraints are satisfied
        for constraint in constraints:
            row1, col1 = constraint[0]
            row2, col2 = constraint[1]
            symbol = constraint[2]
            entry1 = root.grid_slaves(row=row1, column=col1)[0]
            entry2 = root.grid_slaves(row=row2, column=col2)[0]
            value1 = entry1.get()
            value2 = entry2.get()
            if value1 and value2:
                if symbol == "^":
                    if int(value1) > int(value2):
                        messagebox.showerror("Error", "Values in cells ({}, {}) and ({}, {}) do not satisfy the constraint".format(row1, col1, row2, col2))
                        return False
                elif symbol == "v":
                    if int(value1) < int(value2):
                        messagebox.showerror("Error", "Values in cells ({}, {}) and ({}, {}) do not satisfy the constraint".format(row1, col1, row2, col2))
                        return False
                elif symbol == ">":
                    if int(value1) < int(value2):
                        messagebox.showerror("Error", "Values in cells ({}, {}) and ({}, {}) do not satisfy the constraint".format(row1, col1, row2, col2))
                        return False
        else :
              return True



    def on_submit():
        if solve_puzzle() and check_constraints() :
            messagebox.showinfo("Success", "Congratulations, you solved the puzzle!")
        else:
            messagebox.showerror("Error", "There is an error in your solution. Please correct the errors and try again.")

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.grid(row=8, column=3)

    
    def quit_program():
        root.destroy()
    quit_button = tk.Button(root, text="Quit",command=quit_program)
    quit_button.grid(row=8,column=4)
    


    pass

start_button.configure(command=start_game)


root.mainloop()
