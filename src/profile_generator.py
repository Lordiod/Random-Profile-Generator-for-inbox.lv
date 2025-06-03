from random import choices, randint
from string import ascii_lowercase, ascii_letters, digits
from datetime import datetime, timedelta
from names import get_first_name, get_last_name
import customtkinter as ctk

def generate_random_string(length, char_set=ascii_lowercase):
    return ''.join(choices(char_set, k=length))

def generate_random_date(start_year=1970, end_year=2005):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    random_date = start_date + timedelta(days=randint(0, (end_date - start_date).days))
    return random_date.strftime("%d %B %Y")

def create_random_profile():
    username = generate_random_string(10)
    email = f"{username}@inbox.lv"
    password = generate_random_string(10, char_set=ascii_letters + digits)
    inbox_answer = generate_random_string(6, char_set=ascii_lowercase + digits)
    date_of_birth = "01 January 2000"
    creation_date = datetime.now().strftime("%d/%m/%Y")
    first_name = get_first_name()
    last_name = get_last_name()
    display_name = username
    region = "Egypt"

    profile = f"""
Login email: {email}
Password email: {password}{randint(100, 999)}
Password epic games: {password}{randint(100, 999)}
First name: {first_name}
Last name: {last_name}
Date of birth: {date_of_birth}
Country: Egypt
Cars unlocked: 11
Question: What is your pet's name?
Answer: {inbox_answer}
payment method: instapay (01064374797)
"""

    return profile

def display_profile_in_window():
    def generate_and_display():
        profile = create_random_profile().strip()
        result_label.configure(state="normal")
        result_label.delete("1.0", "end")
        result_label.insert("1.0", profile)
        result_label.configure(state="disabled")
        
        root.clipboard_clear()
        root.clipboard_append(profile)
        
        status_label.configure(text="Profile copied to clipboard!", text_color="green")
        root.after(2000, lambda: status_label.configure(text="", text_color="green"))

    root = ctk.CTk()
    root.title("Random Profile Generator")
    root.geometry("600x400")
    root.resizable(False, False)

    generate_button = ctk.CTkButton(root, text="Generate Profile", command=generate_and_display)
    generate_button.pack(pady=10)

    result_label = ctk.CTkTextbox(root, width=580, height=300, wrap="word")
    result_label.pack(padx=10, pady=5, fill="both", expand=True)

    status_label = ctk.CTkLabel(root, text="", height=20)
    status_label.pack(pady=5)

    result_label.configure(state="disabled")

    root.mainloop()

if __name__ == "__main__":
    display_profile_in_window()