from tkinter import *
from tkinter import messagebox
import customtkinter

main = Tk()
main.title("Login")
main.iconbitmap(".\icon.ico")
main.configure(bg="#F6F1F1")

#function start

def submit_handler():
    username = entry_username.get()
    password = entry_password.get()
    if username == "chenmh":
        if password == "gfi83795":
            messagebox.showinfo("WELCOME!", "WELCOME")
        else:
            messagebox.showinfo("WRONG PASSWORD!", "WRONG PASSWORD!")
    else:
        messagebox.showinfo("WRONG USERNAME!", "WRONG USERNAME!")






#function end

#geometry start

width = 900
height = 500
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
screen_width = int((screen_width - 900) / 2)
screen_height = int((screen_height - 520) / 2)
main.geometry(f"{width}x{height}+{screen_width}+{screen_height}")
main.resizable(False, False)

#geometry end


section_login = customtkinter.CTkFrame(
    master=main,
    fg_color="#AFD3E2",
    width=400,
    height=400,

)
section_login.place(x=250, y=50)


login_label = customtkinter.CTkLabel(
    master=main,
    text_color="BLACK",
    text="WELCOME",
    font=("Time news romen", 26, "bold"),
    bg_color="#AFD3E2"
)
login_label.place(x=385, y=120)

username_label = customtkinter.CTkLabel(
    master=main,
    text_color="BLACK",
    text="Username",
    font=("Sylfaen", 14),
    bg_color="#AFD3E2"
)
username_label.place(x=340, y=180)

password_label = customtkinter.CTkLabel(
    master=main,
    text_color="BLACK",
    text="Password",
    font=("Sylfaen", 14),
    bg_color="#AFD3E2"
)
password_label.place(x=340, y=250)

entry_username = customtkinter.CTkEntry(
    master=main,
    width=100,
    placeholder_text="your username",
    fg_color="#AFD3E2",
    border_color="#AFD3E2",
    corner_radius=0,
    text_color="Black"
)
entry_username.place(x=333, y=210)

entry_password = customtkinter.CTkEntry(
    master=main,
    width=100,
    placeholder_text="your password",
    fg_color="#AFD3E2",
    border_color="#AFD3E2",
    corner_radius=0,
    text_color="Black"
)
entry_password.place(x=333, y=280)

submit_btn = customtkinter.CTkButton(
    master=main,
    text="SUBMIT",
    text_color="BLACK",
    fg_color="#19A7CE",
    corner_radius=0,
    border_color="#19A7CE",
    width=230,
    height=30,
    command=submit_handler
)
submit_btn.place(x=336, y=330)




main.mainloop()