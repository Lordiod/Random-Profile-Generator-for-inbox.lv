import random  # Import the random module for generating random values
import string  # Import string module for character sets
from datetime import datetime, timedelta  # Import datetime for handling dates
import names  # Import names module for generating random names
import customtkinter as ctk  # Import customtkinter for GUI

# Function to generate a random string of specified length
def generate_random_string(length, char_set=string.ascii_lowercase):
    return ''.join(random.choices(char_set, k=length))

# Function to generate a random birth date within a specified range
def generate_random_date(start_year=1970, end_year=2005):
    start_date = datetime(start_year, 1, 1)  # Define start date
    end_date = datetime(end_year, 12, 31)  # Define end date
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))  # Generate random date
    return random_date.strftime("%d %B %Y")  # Return formatted date

# Function to create a random user profile
def create_random_profile():
    username = generate_random_string(10)  # Generate random username
    email = f"{username}@inbox.lv"  # Create email using the username
    password = generate_random_string(10, char_set=string.ascii_letters + string.digits)  # Generate random password
    inbox_answer = generate_random_string(6, char_set=string.ascii_lowercase + string.digits)  # Generate inbox security answer
    date_of_birth = "01 January 2000"  # Fixed date of birth
    creation_date = datetime.now().strftime("%d/%m/%Y")  # Get the current date as account creation date
    first_name = names.get_first_name()  # Generate random first name
    last_name = names.get_last_name()  # Generate random last name
    display_name = username  # Use username as display name
    region = "Egypt"  # Set default region

    # Create a profile template string
    profile = f"""
Email: {email}
Passwords(Email - Epic Games): {password}{random.randint(100, 999)}
InBox question : What is your pet's name?
InBox Answer the question : {inbox_answer}
Date of birth: {date_of_birth}
Creation date: {creation_date}
Name(First - Last): {first_name} {last_name}
Displayname: {display_name}
Region: {region}
Unlocked cars: backfire - breakout - dominus - gizmo - hotshot - merc - octane - paladin - road hog - venom - x-devil

payment method: Vodafone cash - insta pay (01064374797)
"""

    return profile  # Return the generated profile

# Function to display the generated profile in a GUI window
def display_profile_in_window():
    def generate_and_display():
        profile = create_random_profile().strip()  # Generate a new profile and remove leading/trailing whitespace
        result_label.configure(state="normal")  # Make text box editable temporarily
        result_label.delete("1.0", "end")  # Clear previous profile
        result_label.insert("1.0", profile)  # Insert new profile
        result_label.configure(state="disabled")  # Make text box read-only again
        
        # Copy the profile to clipboard
        root.clipboard_clear()  # Clear clipboard contents
        root.clipboard_append(profile)  # Copy new profile to clipboard
        
        # Show temporary message indicating copy was successful
        status_label.configure(text="Profile copied to clipboard!", text_color="green")
        root.after(2000, lambda: status_label.configure(text="", text_color="green"))  # Clear message after 2 seconds

    # Initialize the customtkinter window
    root = ctk.CTk()
    root.title("Random Profile Generator")  # Set window title
    root.geometry("600x400")  # Set window size
    root.resizable(False, False) # Disable window resizing

    # Create a button to generate the profile
    generate_button = ctk.CTkButton(root, text="Generate Profile", command=generate_and_display)
    generate_button.pack(pady=10)  # Add button to window with padding

    # Create a text widget to display the profile result
    result_label = ctk.CTkTextbox(root, width=580, height=300, wrap="word")
    result_label.pack(padx=10, pady=5, fill="both", expand=True)  # Configure text box properties

    # Create a label to show clipboard status
    status_label = ctk.CTkLabel(root, text="", height=20)
    status_label.pack(pady=5)

    # Make the text widget initially empty and read-only
    result_label.configure(state="disabled")

    # Run the application
    root.mainloop()

# Run the GUI application if the script is executed directly
if __name__ == "__main__":
    display_profile_in_window()