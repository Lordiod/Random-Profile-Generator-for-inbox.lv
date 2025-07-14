# Random Profile Generator for inbox.lv

A blazing-fast random profile generator for creating inbox.lv accounts, optimized for **millisecond startup times**.

---

## Why This Project?

- **Ultra-fast startup**: Launches in milliseconds
- **Minimal dependencies**: Only loads what's needed, when needed
- **Multiple interfaces**: Use via GUI, CLI, or as a Python module
- **Cross-platform**: Works on Windows, macOS, and Linux

---

## Installation

1. **Clone the repository**
   ```
   git clone https://github.com/Lordiod/random-profile-generator.git
   cd random-profile-generator
   ```
2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

---

## Usage

### 1. GUI Application (Fast)
```bash
python main.py
```
Or double-click `launch.bat` (Windows)

### 2. Command Line (Instant)
```bash
python cli.py
```
Generates a profile instantly, no GUI.

### 3. Import as a Module
```python
from src.profile_generator_fast import create_random_profile_fast
profile = create_random_profile_fast()
```

---

## Features

- **Instant startup**: Millisecond launch times
- **Auto clipboard**: Profiles auto-copied
- **Flexible interfaces**: GUI & CLI
- **Cross-platform**: Windows, macOS, Linux

---

## Performance

| Launch Method | Startup Time | Memory Usage |
|---------------|--------------|--------------|
| Original      | ~2-3 seconds | High         |
| Optimized GUI | ~500ms       | Medium       |
| CLI Mode      | ~100ms       | Low          |

---

## Example Output

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

---

## Project Structure

```
Random-Profile-Generator-for-inbox.lv/
├── src/
│   ├── __init__.py
│   ├── gui.py
│   └── profile_generator.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Contributing

Contributions are welcome! Open an issue or submit a pull request.

---

## License

MIT License – see [LICENSE](LICENSE) for details.
