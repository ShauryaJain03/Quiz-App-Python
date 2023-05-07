import tkinter as tk
import random
import questions
from tkinter import messagebox

def display_questions():
    selected_questions = random.sample(questions.all_questions, 5)
    question_index = 0
    score = 0

    def check_answer():
        nonlocal score

        selected_option = options.get()
        correct_option = selected_questions[question_index][1]

        if selected_option == correct_option:
            score += 1

        next_question()

    def next_question():
        nonlocal question_index

        if question_index < len(selected_questions) - 1:
            question_index += 1
            question_label.config(text=selected_questions[question_index][0])
            options.set(-1)

            for i, option in enumerate(option_buttons):
                option.configure(text=selected_questions[question_index][2][i])

            score_label.config(text="Score: {}".format(score))
        else:
            messagebox.showinfo("Quiz", "Quiz completed!\nYour score: {}".format(score))
            window.destroy()

    window = tk.Tk()
    window.title("Quiz")

    question_label = tk.Label(window, text=selected_questions[question_index][0])
    question_label.pack(pady=10)

    options = tk.IntVar()
    options.set(-1)

    option_buttons = []
    for i in range(4):
        option_button = tk.Radiobutton(window, text="", variable=options, value=i)
        option_button.pack(anchor='w')
        option_buttons.append(option_button)

    check_button = tk.Button(window, text="Check Answer", command=check_answer)
    check_button.pack(pady=10)

    score_label = tk.Label(window, text="Score: 0")
    score_label.pack()

    next_question()

    window.mainloop()

display_questions()
