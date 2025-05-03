# Random Profile Generator

A simple application that generates random user profiles for use with inbox.lv. The application includes a graphical user interface (GUI) for easy interaction and profile generation.

## Features

- Generate random usernames, emails, passwords, and other profile details.
- User-friendly GUI for generating and displaying profiles.
- Customizable profile generation with options for different regions.
- Automatic clipboard copying of generated profiles.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Lordiod/random-profile-generator.git
   ```
2. Navigate to the project directory:
   ```
   cd random-profile-generator
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command in the terminal:
```
python main.py
```

Alternatively, you can use:
```
python -m src.gui
```

This will open the GUI window where you can generate random profiles by clicking the "Generate Profile" button.

## Project Structure

```
Random-Profile-Generator-for-inbox.lv/
├── data/
│   └── regions.json       # Available regions for profile generation
├── src/
│   ├── __init__.py        # Package initialization
│   ├── gui.py             # GUI implementation
│   └── profile_generator.py # Profile generation logic
├── LICENSE                # MIT License
├── README.md              # Project documentation
├── main.py                # Main entry point
└── requirements.txt       # Project dependencies
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.