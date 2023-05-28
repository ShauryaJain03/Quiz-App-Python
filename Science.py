from tkinter import *
import time
from customtkinter import *
from PIL import Image,ImageTk
import random
from CTkMessagebox import CTkMessagebox
import sc_questions

quiz_ended=False
hint_taken=False
hint_count=0

def show_hint():
    global hint_count
    hint_taken=True
    hint_clicked=CTkMessagebox(title="HINT",message=hint_hard,width=400,height=280,button_color="#0191C8",font=("helvetica",18))
    if hint_taken==True:
        hint_count+=1
    

def end_quiz():
        
        click_ans=CTkMessagebox(title="Quiz",  option_1="Close", option_2="See Analysis",message="Quiz completed!\nYour score: {}".format(final_score),fade_in_duration=0.5,width=400,height=280,button_color="#0191C8",font=("helvetica",18))
        if click_ans.get()=="End":
            sciencespage.destroy()
        else:
            sciencespage.destroy()

def display_questions(window):
    user_responses=[]   #to store user responses as a tuple
    start_time = 0
    total_time = 0
    easy_questions = []  # List to store easy level questions
    medium_questions = []  # List to store medium level questions
    hard_questions = []  # List to store hard level questions

    global clock_label
    clock_label = Label(window, text="Time: 0", font=("helvetica", 22))  # Timer label
    clock_label.pack(anchor="ne", padx=15)
    start_time = time.time()  # Store the start time


    # assign questions based on their difficulty level
    for question in sc_questions.all_questions:
        difficulty = question[3]  #the difficulty level is stored at index 3 of each question tuple
        if difficulty == "easy":
            easy_questions.append(question)
        elif difficulty == "medium":
            medium_questions.append(question)
        elif difficulty == "hard":
            hard_questions.append(question)
    
    # Selecting random questions from each difficulty level
    selected_questions = []
    selected_questions.extend(random.sample(easy_questions,3))  #for easy it is taking n+1 as argument to display n questions
    selected_questions.extend(random.sample(medium_questions,2))
    selected_questions.extend(random.sample(hard_questions,2))
    
    question_index = 0
    score = 0

    def update_clock():
            if quiz_ended==False:
                current_time = time.time() - start_time  # Calculate the time elapsed
                clock_label.configure(text="Time: {:.2f} seconds".format(current_time))
                window.after(100, update_clock)  # Update the clock every 100 milliseconds (0.1 seconds)
    update_clock() 


    def check_answer():
        nonlocal score
        nonlocal start_time
        nonlocal total_time
        global answer
        selected_option = options.get()
        correct_option = selected_questions[question_index][1]
        difficulty = selected_questions[question_index][3]
        

        if selected_option == correct_option:
            answer="correct"
            if difficulty == "easy":
                score += 1
            elif difficulty == "medium":
                score += 2
            elif difficulty == "hard":
                score += 3
        elif selected_option==-1:
            answer="notAnswered"
        else:
            answer="wrong"

        end_time = time.time()  # Get the current time
        time_taken = end_time - start_time  # Calculate the time taken
        total_time += time_taken  # Updates total_time after each question

        #the tuple for storing question , user response and time taken per question
        if (difficulty=="hard" and hint_count>=1):
            user_responses.append((selected_questions[question_index][0], selected_option,answer,time_taken,"yes"))
        elif(difficulty=="hard" and hint_count==0):
            user_responses.append((selected_questions[question_index][0], selected_option,answer,time_taken,"no"))
        else:
            user_responses.append((selected_questions[question_index][0], selected_option,answer,time_taken))


        clock_label.configure(text="Time: {:.2f} seconds".format(time_taken))  #updating the clock label
        print("Time: {:.3f} seconds".format(time_taken)+" , {} level ".format(difficulty))  #printing time data to terminal

        next_question()

    def next_question():
        nonlocal question_index
        nonlocal start_time
        nonlocal total_time  # This inherits the value from check_answer function
        if question_index < len(selected_questions) - 1:
            question_index += 1
            question_label.configure(text="Q{}. ".format(question_index) + selected_questions[question_index][0])
            options.set(-1)

            if selected_questions[question_index][3]=="hard":
                hint_btn.configure(state=ACTIVE,command=show_hint)
                global hint_hard
                hint_hard=selected_questions[question_index][4]            

            for i, option in enumerate(option_buttons):
                option.configure(text=selected_questions[question_index][2][i])

            start_time = time.time()  # Starts timer from 0 after each question
            if question_index==6:    #toggles the button text at the last question
                check_button.configure(text="End")

        else:
            global quiz_ended
            quiz_ended=True
            global final_score
            final_score = score-hint_count
            print("Final score is : ",final_score)   #print final score
            print("Total Time: {:.3f} seconds".format(total_time))   #print total time
            print("Average time taken: {:.3f} seconds".format(total_time / 6))  #print average time

            #print(user_responses)  
            #print user responses as individual tuples 
            for i in user_responses:
                print(i,end="\n")
            end_quiz()
            # window.destroy()


    # Rest of the code remains the same...
    window = CTkToplevel(sciencespage,fg_color="#25292e")
    window.title("The Main Event")
    window.attributes("-topmost", True)
    window.geometry("1050x600")
    window.resizable(False,False)
    window.iconbitmap("C:\\Users\\shaur\\OneDrive\\Desktop\\DS Project\\Images\\iconfilemain\\favicon.ico")
    question_label = CTkLabel(window, text=selected_questions[question_index][0],font=("helvetica",24),wraplength=1000,text_color="#f2a66a",padx=10,pady=15)
    question_label.pack(pady=20,anchor="w",padx=10)
    clock_label = CTkLabel(window, text="Time: 0", font=("helvetica", 22))  #timer label
    clock_label.pack(anchor="ne",padx=15) 

    options = IntVar()
    options.set(-1)

    option_buttons = []
    for i in range(4):
        option_button =CTkRadioButton(window, text="", variable=options, value=i,hover_color="#57a3e8",border_color="#ef727d",fg_color="#575bc1",radiobutton_height=20,radiobutton_width=20,height=40,font=("helvetica",18),text_color="white",border_width_checked=2,border_width_unchecked=2)
        option_button.pack(anchor='w',padx=10,pady=15)
        option_buttons.append(option_button)

    global check_button
    check_button = CTkButton(window, text="Next", command=check_answer,font=("helvetica",18),width=110,height=70,fg_color="#575bc1",text_color="#fff",hover_color="#2a357a")
    check_button.place(x=550,y=450)
    global hint_btn
    hint_btn=CTkButton(window,text="Show Hint",state=DISABLED,font=("helvetica",20),width=110,height=70)
    hint_btn.place(x=400,y=450)
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
    start_btn = CTkButton(sciencespage, text="Start",height=60,width=120,command=lambda:display_questions(sciencespage),font=("helvetica",20)).place(relx=0.40,rely=0.5)
    sciencespage.mainloop()  
