import customtkinter as ctk
import tkinter.messagebox as tkmb

# Selecting GUI theme - dark, light, system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
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
        login_button.pack_forget()
        signup_button.pack_forget()
        
        user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
        user_entry.pack(pady=12, padx=10)
        user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
        user_pass.pack(pady=12, padx=10)
        
        complete_login_button = ctk.CTkButton(master=frame, text='Login', command=login)
        complete_login_button.pack(pady=12, padx=10)

        

    elif action == "signup":
        # Hide login and signup buttons
        login_button.pack_forget()
        signup_button.pack_forget()
        
        # Create and display additional input fields
        name_entry = ctk.CTkEntry(master=frame, placeholder_text="Name")
        name_entry.pack(pady=12, padx=10)
        
        user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
        user_pass.pack(pady=12, padx=10)
        
        email_entry = ctk.CTkEntry(master=frame, placeholder_text="Email")
        email_entry.pack(pady=12, padx=10)
        
        phone_entry = ctk.CTkEntry(master=frame, placeholder_text="Phone Number")
        phone_entry.pack(pady=12, padx=10)
        
        complete_signup_button = ctk.CTkButton(master=frame, text='Complete Signup', command=complete_signup)
        complete_signup_button.pack(pady=12, padx=10)

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

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Welcome')
label.pack(pady=12, padx=10)

login_button = ctk.CTkButton(master=frame, text='Login', command=lambda: login_or_signup("login"))
login_button.pack(pady=12, padx=10)

signup_button = ctk.CTkButton(master=frame, text='Signup', command=lambda: login_or_signup("signup"))
signup_button.pack(pady=12, padx=10)

app.mainloop()