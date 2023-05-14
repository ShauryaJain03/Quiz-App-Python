from tkinter import *
import time
from customtkinter import *
from PIL import Image,ImageTk
import random
from CTkMessagebox import CTkMessagebox
import sc_questions
def end_quiz():
        click_ans=CTkMessagebox(title="Quiz",  option_1="Close", option_2="See Analysis",message="Quiz completed!\nYour score: {}".format(final_score),fade_in_duration=0.5,width=400,height=300,button_color="#0191C8",font=("helvetica",18))
        if click_ans.get()=="End":
            sciencespage.destroy()
        else:
            sciencespage.destroy()
def display_questions():
    start_time = 0
    total_time = 0
    easy_questions = []  # List to store easy level questions
    medium_questions = []  # List to store medium level questions
    hard_questions = []  # List to store hard level questions

    # Separate the questions based on their difficulty level
    for question in sc_questions.all_questions:
        difficulty = question[3]  # Assuming the difficulty level is stored at index 3 of each question tuple
        if difficulty == "easy":
            easy_questions.append(question)
        elif difficulty == "medium":
            medium_questions.append(question)
        elif difficulty == "hard":
            hard_questions.append(question)

    # Select random questions from each difficulty level
    selected_questions = []
    selected_questions.extend(random.sample(easy_questions,3))  #for easy it is taking n+1 as argument to display n questions
    selected_questions.extend(random.sample(medium_questions,2))
    selected_questions.extend(random.sample(hard_questions,2))

    question_index = 0
    score = 0

    def check_answer():
        nonlocal score
        nonlocal start_time
        nonlocal total_time
        selected_option = options.get()
        correct_option = selected_questions[question_index][1]
        difficulty = selected_questions[question_index][3]

        if selected_option == correct_option:
            if difficulty == "easy":
                score += 1
            elif difficulty == "medium":
                score += 2
            elif difficulty == "hard":
                score += 3

        end_time = time.time()  # Get the current time
        time_taken = end_time - start_time  # Calculate the time taken
        total_time += time_taken  # Updates total_time after each question
        clock_label.configure(text="Time: {:.2f} seconds".format(time_taken))
        print("Time: {:.3f} seconds".format(time_taken)+" with difficulty : {}".format(difficulty))
        next_question()

    def next_question():
        nonlocal question_index
        nonlocal start_time
        nonlocal total_time  # This inherits the value from check_answer function
        if question_index < len(selected_questions) - 1:
            question_index += 1
            question_label.configure(text=selected_questions[question_index][0])
            options.set(-1)

            for i, option in enumerate(option_buttons):
                option.configure(text=selected_questions[question_index][2][i])

            start_time = time.time()  # Starts timer from 0 after each question

        else:
            global final_score
            final_score = score
            print(final_score)
            print("Total Time: {:.3f} seconds".format(total_time))
            print("Average time taken: {:.3f} seconds".format(total_time / 6))
            end_quiz()
            # window.destroy()

    # Rest of the code remains the same...
    window = CTkToplevel(sciencespage)
    window.title("Quiz")
    window.attributes("-topmost", True)
    window.geometry("1100x600")
    question_label = CTkLabel(window, text=selected_questions[question_index][0],font=("helvetica",22),wraplength=1000,text_color="red",bg_color="white",padx=10,pady=15)
    question_label.pack(pady=20,anchor="w",padx=10)
    clock_label = CTkLabel(window, text="Time: 0", font=("helvetica", 20))  #timer label
    clock_label.pack(anchor="ne",padx=15) 

    options = IntVar()
    options.set(-1)

    option_buttons = []
    for i in range(4):
        option_button =CTkRadioButton(window, text="", variable=options, value=i,hover_color="white",border_color="red",fg_color="aqua",radiobutton_height=20,radiobutton_width=20,height=40,font=("helvetica",18))
        option_button.pack(anchor='w',padx=10,pady=15)
        option_buttons.append(option_button)

    check_button = CTkButton(window, text="Next", command=check_answer,font=("helvetica",18),width=100,height=60)
    check_button.pack(pady=50)

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
    #bg=PhotoImage(file="C:\\Users\\shaur\\OneDrive\\Desktop\\DS Project\\Images\\sciencebkg.png")
    #imglabel=Label(sciencespage,image=bg)
    #imglabel.place(x=0,y=0,relwidth=1,relheight=1)
    start_btn = CTkButton(sciencespage, text="Start",height=60,width=120,command=lambda:display_questions(),font=("helvetica",18)).place(relx=0.40,rely=0.5)
    sciencespage.mainloop()
science()
