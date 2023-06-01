from tkinter import *
import time
from customtkinter import *
from PIL import Image,ImageTk
import random
from CTkMessagebox import CTkMessagebox
import sc_questions
import requests
import threading
import MySQLfunctions
from io import BytesIO
quiz_ended=False
hint_taken=False
hint_count=0
#function which displays the hint on show hint button being clicked
def show_hint():
    global hint_count
    global hint_taken
    hint_taken=True
    hint_clicked=CTkMessagebox(title="HINT",message=hint_hard,width=400,height=280,button_color="#0191C8",font=("helvetica",18))
    if hint_taken==True:
        hint_count+=1
    
#function which terminates the quiz
def end_quiz():
        click_ans=CTkMessagebox(title="Quiz",  option_1="Close", option_2="See Analysis",message="Quiz completed!\nYour score: {}/30".format(final_score),fade_in_duration=0.5,width=400,height=280,button_color="#0191C8",font=("helvetica",18))
        if click_ans.get()=="End":
            sciencespage.destroy()
        else:
            sciencespage.destroy()

#loading images for the image based questions
def preload_images(*questions):
    for question in questions:
        if question[3] == "image":  # index 3 contains the difficulty level
            img_url = question[4]  # index 4 contains the image URL
            preload_image(img_url)

def preload_image(img_url):
    response = requests.get(img_url)

#function to display questions
def display_questions(window):
    global user_responses
    start_time = 0
    total_time = 0
    user_responses=[]      #to store user responses as a tuple
    easy_questions = []    #List to store easy level questions
    medium_questions = []  #List to store medium level questions
    hard_questions = []    #List to store hard level questions
    image_questions=[]     #List to store image questions

    global clock_label
    clock_label = Label(window, text="Time: 0", font=("helvetica", 22))  #Timer label
    clock_label.pack(anchor="ne", padx=10)
    start_time = time.time()  #store the start time


    #sort the questions based on their difficulty level into the pre defined list structure
    for question in sc_questions.all_questions:
        difficulty = question[3]  #the difficulty level is stored at index 3 of each question tuple
        if difficulty == "easy":
            easy_questions.append(question)
        elif difficulty == "medium":
            medium_questions.append(question)
        elif difficulty == "hard":
            hard_questions.append(question)
        elif difficulty=="image":
            image_questions.append(question)
    
    #selecting random questions from each difficulty level list
    selected_questions = []
    selected_questions.extend(random.sample(easy_questions,4))  #for easy it is taking n+1 as argument to display n questions   
    selected_questions.extend(random.sample(medium_questions,4))
    selected_questions.extend(random.sample(hard_questions,3))
    selected_questions.extend(random.sample(image_questions, 2))
    
    question_index = 0
    score = 0

    preload_thread = threading.Thread(target=preload_images, args=(selected_questions))
    preload_thread.start()

    #clock updation function
    def update_clock():
            if quiz_ended==False:
                current_time = time.time() - start_time  #calculate the time elapsed
                clock_label.configure(text="Time: {:.2f} seconds".format(current_time))
                window.after(100, update_clock)          #update the clock every 0.1 seconds
    update_clock() 

    #function to check answer
    def check_answer():
        global final_score
        nonlocal score
        nonlocal start_time
        nonlocal total_time
        global answer
        selected_option = options.get()
        correct_option = selected_questions[question_index][1]   #correct option stored at index 1
        difficulty = selected_questions[question_index][3]       #difficulty stored at index 3
        code=selected_questions[question_index][5]               #question code stored at index 5
        hint_avail=selected_questions[question_index][4]         #hint stored at index 4

        if selected_option == correct_option:   #check if the selected option is the same as the correct answer
            answer="correct"
            if difficulty == "easy":
                score += 1
            elif difficulty == "medium":
                score += 2
            elif difficulty == "hard":
                score += 3
            elif difficulty=="image":
                score+=5
        elif selected_option==-1:
            answer="notAnswered"
        else:
            answer="wrong"         

        end_time = time.time()              #get the current time
        time_taken = end_time - start_time  #calculate the time taken
        total_time += time_taken            #updates total_time after each question

        #the tuple for storing question , user response and time taken per question and other data to be written to the tables in the database
        if (difficulty=="hard" and hint_taken==True):
            user_responses.append([selected_questions[question_index][0], difficulty,selected_option,answer,time_taken,"yes",code,score])
        elif(difficulty=="hard" and hint_taken==False):
            user_responses.append([selected_questions[question_index][0],  difficulty,selected_option,answer,time_taken,"no",code,score])
        else:
            user_responses.append([selected_questions[question_index][0], difficulty, selected_option,answer,time_taken,hint_avail,code,score])



        clock_label.configure(text="Time: {:.2f} seconds".format(time_taken))  #updating the clock label
        print("Time: {:.3f} seconds".format(time_taken)+" , {} level ".format(difficulty))  #printing time data to terminal

        next_question()

    def next_question():
        global hint_taken
        hint_taken=False
        nonlocal question_index
        nonlocal start_time
        nonlocal total_time  #this inherits the value from check_answer function
        if question_index < len(selected_questions) - 1:
            question_index += 1
            question_label.configure(text="Q{}. ".format(question_index) + selected_questions[question_index][0])
            options.set(-1)

            #if question is hard then display 
            if (selected_questions[question_index][3]=="hard"):
                hint_btn.configure(state=ACTIVE,command=show_hint)
                global hint_hard
                hint_hard=selected_questions[question_index][4]            

            for i, option in enumerate(option_buttons):
                option.configure(text=selected_questions[question_index][2][i])

            start_time = time.time()  # Starts timer from 0 after each question
            if question_index==10:    #toggles the button text at the last question
                check_button.configure(text="End")

            if selected_questions[question_index][3] == "image":
                hint_btn.configure(state=DISABLED,command=show_hint)
                img_path = selected_questions[question_index][4]
                display_image(img_path)
            else:
                hide_image()
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


    def display_image(img_url):
        response = requests.get(img_url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image = image.resize((550, 450), resample=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo
        image_label.place(x=1000, y=180)

    def hide_image():
        image_label.pack_forget()

    
    window = CTkToplevel(sciencespage,fg_color="#25292e")
    window.title("The Main Event")
    window.attributes("-topmost", True)
    window.geometry("1050x600")
    window.resizable(False,False)
    window.iconbitmap("C:\\Users\\shaur\\OneDrive\\Desktop\\DS Project\\Images\\iconfilemain\\favicon.ico")
    question_label = CTkLabel(window, text=selected_questions[question_index][0],font=("helvetica",24),wraplength=1000,text_color="#f2a66a",padx=10,pady=15)
    question_label.pack(pady=20,anchor="w",padx=10)
    clock_label = CTkLabel(window, text="Time: 0", font=("helvetica", 22))  #timer label
    clock_label.pack(anchor="e",padx=10) 
    image_label = Label(window)
    
    options = IntVar()
    options.set(-1)

    option_buttons = []
    for i in range(4):
        option_button =CTkRadioButton(window, text="", variable=options, value=i,hover_color="#57a3e8",border_color="#ef727d",fg_color="#575bc1",radiobutton_height=20,radiobutton_width=20,height=40,font=("helvetica",20),text_color="white",border_width_checked=2,border_width_unchecked=2)
        option_button.pack(anchor='w',padx=10,pady=15)
        option_buttons.append(option_button)

    global check_button
    check_button = CTkButton(window, text="Next", command=check_answer,font=("helvetica",18),width=110,height=70,fg_color="#575bc1",text_color="#fff",hover_color="#2a357a")
    check_button.place(x=550,y=500)
    global hint_btn
    hint_btn=CTkButton(window,text="Show Hint",state=DISABLED,font=("helvetica",20),width=110,height=70)
    hint_btn.place(x=400,y=500)

    next_question()
    window.mainloop()

def science():

    global sciencespage
    sciencespage = CTk()
    sciencespage.title("Science")
    sciencespage.resizable(False,False)
    sciencespage.geometry("720x680")
    sciencespage.attributes("-topmost", True)
    set_appearance_mode("system")
    #bg=PhotoImage(file="C:\\Users\\shaur\\OneDrive\\Desktop\\DS Project\\Images\\sciencebkg.png")
    #imglabel=Label(sciencespage,image=bg)
    #imglabel.place(x=0,y=0,relwidth=1,relheight=1)
    set_default_color_theme("dark-blue") 
    sciencespage.iconbitmap("C:\\Users\\shaur\\OneDrive\\Desktop\\DS Project\\Images\\iconfilemain\\favicon.ico")
    info_label=CTkLabel(sciencespage,text="\t\t               Welcome to the Quiz\n\nRules:\n\n1 .The quiz consists of 12 multiple-choice questions and total weightage of 30 marks.\n\n2. Each question has four options, among which only one is correct.\n\n3. The questions are of 4 categories - Easy , Medium , Hard and Image based\n\n4. Each category has a different marking scheme and no marks will be \n    deducted for incorrect responses : \n\n \ta) Easy - 1 marks for correct answer\n\tb) Medium - 2 marks for correct answer\n\tc) Hard - 3 marks for correct answer\n\td) Image - 5 marks for correct answer",font=("helvetica",18),justify="left").place(x=20,y=20)

    info_label1=CTkLabel(sciencespage,text="\n5. Select the option you think is correct and click Next to move to the next \n    question.\n\n6. You can use the Show Hint button to get a hint for hard questions, but it\n    will reduce your final score.\n\n",font=("helvetica",18),justify="left").place(x=20,y=360)

    info_label2=CTkLabel(sciencespage,text="\n\n        All the best! Put your knowledge to the test and enjoy the quiz!",font=("helvetica",20),justify="left").place(x=20,y=500)

    start_btn = CTkButton(sciencespage, text="Start",height=60,width=120,command=lambda:display_questions(sciencespage),font=("helvetica",20)).place(x=280,y=600)
    sciencespage.mainloop()

    for i in user_responses:
        if i[1]=="image":
            i[7]=final_score
    for i in user_responses:
        print(i)

    MySQLfunctions.insert_response("iec2022010",user_responses)

science()
