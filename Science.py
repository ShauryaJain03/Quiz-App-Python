from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk
import random
from tkinter import messagebox
import questions
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
            question_label.configure(text=selected_questions[question_index][0])
            options.set(-1)

            for i, option in enumerate(option_buttons):
                option.configure(text=selected_questions[question_index][2][i])

            score_label.configure(text="Score: {}".format(score))
            
        else:
            global final_score
            final_score=score
            print(final_score)
            messagebox.showinfo("Quiz", "Quiz completed!\nYour score: {}".format(score))
            window.destroy()

    window = CTkToplevel(sciencespage)
    window.title("Quiz")

    question_label = CTkLabel(window, text=selected_questions[question_index][0])
    question_label.pack(pady=10)

    options = IntVar()
    options.set(-1)

    option_buttons = []
    for i in range(4):
        option_button =CTkRadioButton(window, text="", variable=options, value=i)
        option_button.pack(anchor='w')
        option_buttons.append(option_button)

    check_button = CTkButton(window, text="Check Answer", command=check_answer)
    check_button.pack(pady=10)

    score_label = CTkLabel(window, text="Score: 0")
    score_label.pack()

    next_question()

    window.mainloop()

def science():
    global sciencespage
    sciencespage = CTk()
    sciencespage.title("Science")
    sciencespage.resizable(False,False)
    sciencespage.geometry("680x620")
    sciencespage.attributes("-topmost", True)
    set_appearance_mode("system")
    set_default_color_theme("dark-blue") 
    sciencespage.iconbitmap("C:\\Users\\shaur\\OneDrive\\Desktop\\DS Project\\Images\\iconfilemain\\favicon.ico")
    bg=PhotoImage(file="C:\\Users\\shaur\\OneDrive\\Desktop\\DS Project\\Images\\dark cosmic bac 0.png")
    imglabel=Label(sciencespage,image=bg)
    imglabel.place(x=0,y=0,relwidth=1,relheight=1)
    
    start_btn = CTkButton(sciencespage, text="Start",height=60,width=120,command=lambda:[display_questions(),sciencespage.quit()],font=("helvetica",18)).place(relx=0.40,rely=0.5)
    sciencespage.mainloop()
