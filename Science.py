from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk
def science():
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
    start_btn = CTkButton(sciencespage, text="Start",height=40,width=100,command=sciencespage.destroy).place(relx=0.4,rely=0.5)
    sciencespage.mainloop()

science()
