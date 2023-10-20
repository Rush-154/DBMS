import customtkinter as ctk
import tkinter.messagebox as tkmb

# Selecting GUI theme - dark, light, system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(), app.winfo_screenheight()))  # Open in full screen
app.title("Modern Login UI using Customtkinter")

# Define the name, email, and phone entry fields as global variables
user_entry = None
user_pass = None
name_entry = None
email_entry = None
phone_entry = None

def login_or_signup(action):
    global user_entry, user_pass, name_entry, email_entry, phone_entry  # Define them as global
    if action == "login":
        login_button.place_forget()
        signup_button.place_forget()
        or_label.place_forget()
        
        user_entry = ctk.CTkEntry(master=app, placeholder_text="Username")
        user_entry.place(relx=0.5, rely=0.4, anchor="center")

        user_pass = ctk.CTkEntry(master=app, placeholder_text="Password", show="*")
        user_pass.place(relx=0.5, rely=0.5, anchor="center")
        
        complete_login_button = ctk.CTkButton(master=app, text='Login', command=login)
        complete_login_button.place(relx=0.5, rely=0.6, anchor="center")

    elif action == "signup":
        label.place_forget()
        login_button.place_forget()
        signup_button.place_forget()
        or_label.place_forget()
        
        name_entry = ctk.CTkEntry(master=app, placeholder_text="Name")
        name_entry.place(relx=0.5, rely=0.4, anchor="center")
        
        user_pass = ctk.CTkEntry(master=app, placeholder_text="Password", show="*")
        user_pass.place(relx=0.5, rely=0.5, anchor="center")
        
        email_entry = ctk.CTkEntry(master=app, placeholder_text="Email")
        email_entry.place(relx=0.5, rely=0.6, anchor="center")
        
        phone_entry = ctk.CTkEntry(master=app, placeholder_text="Phone Number")
        phone_entry.place(relx=0.5, rely=0.7, anchor="center")
        
        complete_signup_button = ctk.CTkButton(master=app, text='Complete Signup', command=complete_signup)
        complete_signup_button.place(relx=0.5, rely=0.8, anchor="center")

def complete_signup():
    global name_entry, email_entry, phone_entry, user_pass  # Define them as global
    password = user_pass.get()
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    
    # Display a success message
    tkmb.showinfo(title="Signup Successful", message=f"User {name} with email {email} and phone number {phone} has been registered successfully!")

def login():
    global user_entry, user_pass
    username = "Geeks"
    password = "12345"
    entered_username = user_entry.get()  # Get the user-entered username
    entered_password = user_pass.get()  # Get the user-entered password

    if entered_username == username and entered_password == password:
        tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username or password")

label = ctk.CTkLabel(master=app, text='Welcome')
label.place(relx=0.5, rely=0.4, anchor="center")

login_button = ctk.CTkButton(master=app, text='Login', command=lambda: login_or_signup("login"))
login_button.place(relx=0.5, rely=0.45, anchor="center")

or_label = ctk.CTkLabel(master=app, text='Or')
or_label.place(relx=0.5, rely=0.5, anchor="center")

signup_button = ctk.CTkButton(master=app, text='Signup', command=lambda: login_or_signup("signup"))
signup_button.place(relx=0.5, rely=0.55, anchor="center")

app.mainloop()
