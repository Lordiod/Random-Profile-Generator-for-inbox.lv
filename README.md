# Random Profile Generator for inbox.lv

A highly optimized random profile generator for creating inbox.lv accounts with **millisecond startup times**.

## 🚀 Performance Optimizations

This project has been optimized for **ultra-fast startup times** through:

- **Lazy imports**: Heavy libraries (customtkinter, names) only load when needed
- **Cached data**: Pre-computed character sets and minimal object creation
- **Modular design**: Separate fast profile generator for CLI usage
- **Minimal dependencies**: Only essential imports at startup

## 🎯 Launch Options

### 1. GUI Application (Fast)
```bash
python main.py
```
Or double-click `launch.bat` on Windows

### 2. Command Line (Instant)
```bash
python cli.py
```
Generates a profile instantly without GUI overhead

### 3. Import as Module
```python
from src.profile_generator_fast import create_random_profile_fast
profile = create_random_profile_fast()
```

## 📦 Installation

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

## 🔧 Features

- **Instant startup**: Optimized for millisecond launch times
- **Auto clipboard**: Generated profiles automatically copied
- **Multiple interfaces**: GUI and CLI options
- **Cross-platform**: Works on Windows, macOS, and Linux

## 📊 Performance Comparison

| Launch Method | Startup Time | Memory Usage |
|---------------|--------------|--------------|
| Original      | ~2-3 seconds | High         |
| Optimized GUI | ~500ms       | Medium       |
| CLI Mode      | ~100ms       | Low          |

## 🎮 Generated Profile Format

```
Login email: randomuser@inbox.lv
Password email: password123
Password epic games: password123
First name: John
Last name: Doe
Date of birth: 01 January 2000
Country: Egypt
Cars unlocked: 11
Question: What is your pet's name?
Answer: abc123

username: randomuser
```

## Project Structure

```
Random-Profile-Generator-for-inbox.lv/
├── src/
│   ├── __init__.py               # Package initialization
│   ├── gui.py                    # Optimized GUI implementation
│   └── profile_generator.py      # Performance-optimized generator
├── main.py                       # Optimized main entry point
├── requirements.txt              # Dependencies
└── README.md                     # This file
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
