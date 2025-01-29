import random
import string
from datetime import datetime, timedelta
import names
import customtkinter as ctk

def generate_random_string(length, char_set=string.ascii_lowercase):
    return ''.join(random.choices(char_set, k=length))

def generate_random_date(start_year=1970, end_year=2005):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime("%d %B %Y")

def create_random_profile():
    username = generate_random_string(10)
    email = f"{username}@inbox.lv"
    password = generate_random_string(10, char_set=string.ascii_letters + string.digits)
    inbox_answer = generate_random_string(6, char_set=string.ascii_lowercase + string.digits)
    date_of_birth = generate_random_date() 
    creation_date = datetime.now().strftime("%d/%m/%Y")
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    display_name = username
    region = "Egypt"

    profile = f"""
Email: {email}
Passwords(Email - Epic Games): {password}
InBox question : What is your pet's name?
InBox Answer the question : {inbox_answer}
Date of birth: {date_of_birth}
Creation date: {creation_date}
Name(First - Last): {first_name} {last_name}
Displayname: {display_name}
Region: {region}
Unlocked cars:

payment method: Vodafone cash - insta pay
"""

    return profile

def display_profile_in_window():
    def generate_and_display():
        profile = create_random_profile()
        result_label.configure(state="normal")
        result_label.delete("1.0", "end")
        result_label.insert("1.0", profile)
        result_label.configure(state="disabled")

    # Initialize the customtkinter window
    root = ctk.CTk()
    root.title("Random Profile Generator")
    root.geometry("600x400")

    # Create a button to generate the profile
    generate_button = ctk.CTkButton(root, text="Generate Profile", command=generate_and_display)
    generate_button.pack(pady=10)

    # Create a text widget to display the profile result
    result_label = ctk.CTkTextbox(root, width=580, height=300, wrap="word")
    result_label.pack(padx=10, pady=10, fill="both", expand=True)

    # Make the text widget initially empty and read-only
    result_label.configure(state="disabled")

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    display_profile_in_window()
