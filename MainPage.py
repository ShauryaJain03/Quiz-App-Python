from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk
from MySQLfunctions import *
from MainMenu import *
from trivia import *
global bg
global photo1
global photo2
# Create the main window and run the app
root = CTk()
root.title("Quizzify")
root.geometry("680x620")  #width vs height
root.resizable(False,False)
root.iconbitmap("C:\\Users\\shaur\\OneDrive\\Desktop\\Project\\Images\\iconfilemain\\favicon.ico")
set_appearance_mode("system")
set_default_color_theme("dark-blue") 

bg=PhotoImage(file="C:\\Users\\shaur\\OneDrive\\Desktop\\Project\\Images\\background2.png")

# Get the entered username and password using get function
def login():
    username = username_entry.get()
    email = email_entry.get()
    #write(username,email)
    root.withdraw()
    mainmenu()




def mainmenu():
    menu=CTkToplevel(root)
    menu.title("Main Menu")
    menu.geometry("680x620")
    menu.resizable(False,False)    
    menu.iconbitmap('C:\\Users\\shaur\\OneDrive\\Desktop\\Project\\Images\\iconfilemain\\favicon.ico')
    image1=Image.open('C:\\Users\\shaur\\OneDrive\\Desktop\\Project\\Images\\background.png')
    photo1=ImageTk.PhotoImage(image1)
    label1=Label(menu,image=photo1)
    label1.image=photo1
    label1.pack()
    playbtn=CTkButton(menu,text="Play",fg_color="#97e2e8",border_width=1,text_color="#000",border_color="#feaf88",height=40,width=115, font=("helvetica",18)).place(relx=0.4,rely=0.3)
    leadbtn=CTkButton(menu,text="Leaderboard",fg_color="#97e2e8",border_width=1,text_color="#000",border_color="#feaf88",height=40,width=115, font=("helvetica",18)).place(relx=0.4,rely=0.4)
    trivbtn=CTkButton(menu,text="Trivia",command=trivia,fg_color="#97e2e8",border_width=1,border_color="#feaf88",text_color="#000",height=40,width=115, font=("helvetica",18)).place(relx=0.4,rely=0.5)
    exitbtn=CTkButton(menu,text="Exit",command=lambda:[menu.destroy(),root.quit()],fg_color="#97e2e8",border_width=1,text_color="#000",border_color="#feaf88",height=40,width=115, font=("helvetica",18)).place(relx=0.4,rely=0.6)

def display_random_fact():
    random_fact = random.choice(facts)
    fact_var.set(random_fact)    


def trivia():
    global trivia_page
    trivia_page=Toplevel(root)
    trivia_page.title("DID YOU KNOW?")
    trivia_page.geometry("680x471") 
    trivia_page.resizable(False,False)
    trivia_page.iconbitmap('C:\\Users\\shaur\\OneDrive\\Desktop\\Project\\Images\\iconfilemain\\favicon.ico')
    image2=Image.open("C:\\Users\\shaur\\OneDrive\\Desktop\\Project\\Images\\mainpage.jpg")
    photo2=ImageTk.PhotoImage(image2)
    label2=Label(trivia_page,image=photo2)
    label2.image=photo2
    label2.pack()
    global fact_label
    global fact_var
    fact_var = StringVar()
    fact_label=CTkLabel(trivia_page,textvariable=fact_var,text_color="black",fg_color="aqua").place(relx=0.5,rely=0.5)
    triv_close=CTkButton(trivia_page,text="Close",command=trivia_page.destroy,height=30,width=100,text_color="#fff", font=("helvetica",18))
    triv_close.place(relx=0.4,rely=0.9)
    generate_button=CTkButton(trivia_page,text="generate",command=display_random_fact).place(relx=0.7,rely=0.9)

#create label
mylabel=Label(root,image=bg)
mylabel.place(x=0,y=0,relwidth=1,relheight=1)

# Create username label and entry field
CTkLabel(root, text="Username",anchor=CENTER,fg_color="#feaf88",width=100,height=30,font=("helvetica",16),corner_radius=20,text_color="#0b2954",).place(relx=0.3,rely=0.35)
        
username_entry = CTkEntry(root,width=150,height=30,bg_color="#0b2954",text_color="#feaf88",font=("helvetica",16))
username_entry.place(relx=0.47,rely=0.35)

# Create email label and entry field
CTkLabel(root, text="Email",anchor=CENTER,fg_color="#feaf88",width=100,height=30,font=("helvetica",16),corner_radius=20,text_color="#0b2954").place(relx=0.3,rely=0.45)
email_entry = CTkEntry(root,width=150,height=30,bg_color="#0b2954",text_color="#feaf88", font=("helvetica",16),)
email_entry.place(relx=0.47,rely=0.45)

# Create login button
login_button = CTkButton(root, text="Login", command=login,fg_color="#7b27a1",border_width=1,border_color="#feaf88",height=35,width=105, font=("helvetica",17))
login_button.place(relx=0.40,rely=0.54)

root.mainloop()
