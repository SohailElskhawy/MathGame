from tkinter import *
import random

question_label = None
user_points = 0

def open_gamemode(string):
    global operation
    operation = string
    if operation == "A":
        print(f"Hello From {operation}")
        
        addition()
        show_entry()
        enter_but = Button(root, text="Enter", command=check_answer, font=20, borderwidth=10, bg="powder blue")
        enter_but.grid(row=9, column=1)
        
    elif operation == "S":
        print(f"Hello From {operation}")
        
        subtraction()
        show_entry()
        enter_but = Button(root, text="Enter", command=check_answer, font=20, borderwidth=10, bg="powder blue")
        enter_but.grid(row=9, column=1)
        
    elif operation == "M":
        print(f"Hello From {operation}")
        
        multiplication()
        show_entry()
        enter_but = Button(root, text="Enter", command=check_answer, font=20, borderwidth=10, bg="powder blue")
        enter_but.grid(row=9, column=1)
        

def addition():
    global x
    global y
    x = random.randint(1, 20)
    y = random.randint(1, 20)
    if question_label and question_label.winfo_ismapped():
        question_label.destroy()
    show_question()
        

def subtraction():
    global k
    global l
    k = random.randint(10,20)
    l = random.randint(1,k-1)
    if question_label and question_label.winfo_ismapped():
        question_label.destroy()
    show_question()

def multiplication():
    global a
    global b
    a = random.randint(1, 10)
    b = random.randint(0, 10)
    if question_label and question_label.winfo_ismapped():
        question_label.destroy()
    show_question()

def show_question():
    global question_label
    if operation == "A":
        question = f"{x} + {y}"
    elif operation == "S":
        question = f"{k} - {l}"
    elif operation == "M":
        question = f"{a} x {b}"
    
    question_label = Label(root, text=question, font=(50), bg="powder blue")
    question_label.grid(row=4, column=1)

def show_entry():
    global question_entry
    question_entry = Entry(root, width=30, borderwidth=5)
    question_entry.grid(row=7, column=1)

def update_points():
    points_label.config(text=f"Points: {user_points}")

def check_answer():
    global result
    global user_points
    result = int(question_entry.get())
    if operation == "A":
        if result == (x + y):
            print(f"Correct, You Have {user_points} Points")
            user_points += 1
            update_points()
            correct_label.grid(row=10,column=1)
            root.after(1000, hide_label)
            addition()
            question_label.destroy()
            show_question()
            question_entry.delete(0, END)
        else:
            print("Wrong")
            wrong_label.grid(row=10,column=1)
            root.after(1000, hide_label)    
    if operation == "S":
        if result == (k - l):
            user_points += 1
            update_points()
            correct_label.grid(row=10,column=1)
            root.after(1000, hide_label)
            print(f"Correct, You Have {user_points} Points")
            subtraction()
            question_label.destroy()
            show_question()
            question_entry.delete(0, END)
        else:
            print("Wrong")
            wrong_label.grid(row=10,column=1)
            root.after(1000, hide_label)
    if operation == "M":
        if result == (a * b):
            user_points += 1
            update_points()
            correct_label.grid(row=10,column=1)
            root.after(1000, hide_label)
            print(f"Correct, You Have {user_points} Points")
            multiplication()
            question_label.destroy()
            show_question()
            question_entry.delete(0, END)
        else:
            print("Wrong")
            wrong_label.grid(row=10,column=1)
            root.after(1000, hide_label)

def hide_label():
    correct_label.grid_forget()
    wrong_label.grid_forget()




root = Tk()
root['background'] = "powder blue"
root.title("Math Quiz Game")
root.geometry("500x500")

game_label = Label(root, text="Select Game Mode: ", font=('arial',15,'bold'), fg="green", bg="powder blue")
game_label.grid(row=0, column=0)
button_addition = Button(root, text="Addition", command=lambda: open_gamemode("A"), font=(14), bg="red", borderwidth=10)
button_subtract = Button(root, text="Subtraction", command=lambda: open_gamemode("S"), font=(14), bg="green", borderwidth=10)
button_multiply = Button(root, text="Multiplication", command=lambda: open_gamemode("M"), font=(14), bg="blue", borderwidth=10)
points_label = Label(root, text=f"Points: {user_points}", fg="green", bg="powder blue", font=('arial',15,'bold'))
points_label.grid(row=0, column=14)
button_addition.grid(row=1, column=1)
button_subtract.grid(row=2, column=1)
button_multiply.grid(row=3, column=1)
correct_label = Label(root,text="Correct",font=(40),fg="green",bg="powder blue")
wrong_label = Label(root,text="Wrong",font=(40),fg="red",bg="powder blue")

root.mainloop()

