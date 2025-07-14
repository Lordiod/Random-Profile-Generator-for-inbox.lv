def display_profile_in_window():
    # Lazy import to speed up startup - only import GUI when actually needed
    from customtkinter import CTk, CTkButton, CTkTextbox, CTkLabel
    from src.profile_generator import create_random_profile
    
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

    root = CTk()
    root.title("Random Profile Generator")
    root.geometry("600x400")
    root.resizable(False, False)

    generate_button = CTkButton(root, text="Generate Profile", command=generate_and_display)
    generate_button.pack(pady=10)

    result_label = CTkTextbox(root, width=580, height=300, wrap="word")
    result_label.pack(padx=10, pady=5, fill="both", expand=True)

    status_label = CTkLabel(root, text="", height=20)
    status_label.pack(pady=5)

    result_label.configure(state="disabled")

    root.mainloop()