from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk
import random
from tkinter import messagebox
from CTkMessagebox import CTkMessagebox
import sc_questions
def end_quiz():
        msg=CTkMessagebox(title="Quiz",  option_1="End", option_2="See analysis",message="Quiz completed!\nYour score: {}".format(final_score))
        if msg.get()=="End":
            print(1)
        else:
            print(2)


def display_questions():
    selected_questions = random.sample(sc_questions.all_questions, 6)
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

            #score_label.configure(text="Score: {}".format(score))
            
        else:
            global final_score
            final_score=score
            print(final_score)
            end_quiz()
            window.destroy()

    window = CTkToplevel(sciencespage)
    window.title("Quiz")
    window.attributes("-topmost", True)
    window.geometry("1000x650")
    question_label = CTkLabel(window, text=selected_questions[question_index][0],font=("helvetica",22),wraplength=1000,text_color="red",bg_color="white",padx=10,pady=15)
    question_label.pack(pady=20,anchor="w",padx=10)

    options = IntVar()
    options.set(-1)

    option_buttons = []
    for i in range(4):
        option_button =CTkRadioButton(window, text="", variable=options, value=i,hover_color="white",border_color="red",fg_color="aqua",radiobutton_height=20,radiobutton_width=20,height=40,font=("helvetica",18))
        option_button.pack(anchor='w',padx=10,pady=15)
        option_buttons.append(option_button)

    check_button = CTkButton(window, text="Next", command=check_answer,font=("helvetica",16),width=100,height=40)
    check_button.pack(pady=30)

    #score_label = CTkLabel(window, text="Score: 0")
    #score_label.pack()

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
    bg=PhotoImage(file="C:\\Users\\shaur\\OneDrive\\Desktop\\DS Project\\Images\\sciencebkg.png")
    imglabel=Label(sciencespage,image=bg)
    imglabel.place(x=0,y=0,relwidth=1,relheight=1)
    start_btn = CTkButton(sciencespage, text="Start",height=60,width=120,command=lambda:display_questions(),font=("helvetica",18)).place(relx=0.40,rely=0.5)
    sciencespage.mainloop()
