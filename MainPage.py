from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk
from MySQLfunctions import *
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
    write(username,email)
    menu=CTkToplevel()
    menu.title("Menu")
    menu.geometry("680x620")
    root.withdraw()
def close(window):
    pass

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

root.protocol("WM_DELETE_WINDOW",login)
root.mainloop()