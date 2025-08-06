def display_profile_in_window():
    # Lazy import to speed up startup - only import GUI when actually needed
    import customtkinter as ctk

    from src.profile_generator import create_random_profile

    # Set dark mode and a colorful theme
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")  # Options: "blue", "green", "dark-blue"

    def generate_and_display():
        profile = create_random_profile().strip()
        result_textbox.configure(state="normal")
        result_textbox.delete("1.0", "end")
        result_textbox.insert("1.0", profile)
        result_textbox.configure(state="disabled")

        root.clipboard_clear()
        root.clipboard_append(profile)

        status_label.configure(
            text="Profile copied to clipboard!", text_color="#4ADE80"
        )  # green accent
        root.after(2000, lambda: status_label.configure(text="", text_color="#4ADE80"))

    root = ctk.CTk()
    root.title("Random Profile Generator")
    root.geometry("650x420")
    root.resizable(False, False)

    # Main frame for padding and grouping
    main_frame = ctk.CTkFrame(
        root,
        corner_radius=18,
        fg_color=("#23272F", "#181A20"),
        border_width=2,
        border_color="#3B82F6",
    )
    main_frame.pack(padx=18, pady=18, fill="both", expand=True)

    title_label = ctk.CTkLabel(
        main_frame,
        text="Random Profile Generator",
        font=("Segoe UI", 24, "bold"),
        text_color="#60A5FA",
    )
    title_label.pack(pady=(10, 2))

    generate_button = ctk.CTkButton(
        main_frame,
        text="Generate Profile",
        command=generate_and_display,
        fg_color="#3B82F6",
        hover_color="#2563EB",
        text_color="#FFFFFF",
        font=("Segoe UI", 16, "bold"),
        corner_radius=12,
        border_width=0,
        width=180,
        height=38,
    )
    generate_button.pack(pady=(8, 12))

    result_textbox = ctk.CTkTextbox(
        main_frame,
        width=600,
        height=230,
        wrap="word",
        font=("Consolas", 14),
        fg_color="#181A20",
        text_color="#F3F4F6",
        border_width=2,
        border_color="#3B82F6",
        corner_radius=10,
    )
    result_textbox.pack(padx=8, pady=6, fill="both", expand=True)

    status_label = ctk.CTkLabel(
        main_frame,
        text="",
        height=22,
        font=("Segoe UI", 13, "italic"),
        text_color="#4ADE80",
    )
    status_label.pack(pady=(4, 15))

    result_textbox.configure(state="disabled")

    root.mainloop()
