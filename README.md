# API Tester

![IMG_20250527_220332](https://github.com/user-attachments/assets/3602b816-7213-408f-be01-e7f01a54f1f5)


**API Tester** is a lightweight, terminal-based Python application designed to quickly test HTTP APIs. It allows users to input any API URL, optionally include custom headers, and view structured responses with color-coded logs and formatted JSON.

![API Tester Banner](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Features

- **Clean Interface**: Terminal-clearing, color-enhanced ASCII UI
- **Custom Headers**: Optionally add your own headers to requests
- **Formatted Output**: Pretty-printed JSON or raw text response
- **Color-coded Logging**: Info, success, warning, error, and input messages highlighted
- **Cross-platform Compatibility**: Works on Windows, macOS, and Linux
- **Response Saving**: Save API responses to timestamped files

---

## Requirements

- Python 3.x  
- [`requests`](https://pypi.org/project/requests/)  
- [`colorama`](https://pypi.org/project/colorama/) (for cross-platform colored output)

---

## Installation

### 1. Clone the Repository
```
git clone https://github.com/root-cyze/Api-Tester
```
cd Api-Tester

2. Install Dependencies

pip install -r requirements.txt

If you don’t have a requirements.txt yet, you can install manually:

pip install requests colorama


---

# Usage

Start the application by running:

python main.py

Then:

Enter the API URL you want to test

Choose whether to add headers

View the formatted response

Optionally save the result to a local .txt file



---

# Example

[INPUT 2025-05-27 21:58:05] Enter the API URL: https://xxxx
[SUCCESS 2025-05-27 21:58:07] API responded successfully.
[INFO 2025-05-27 21:58:07] Response:
{
    "slip": {
        "id": 86,
        "advice": "Never write in an email to someone, something which you wouldn't say to that person's face."
    }
}


---

# Contributing

Contributions, bug reports, and feature requests are welcome!

1. Fork the repo


2. Create a new branch (git checkout -b feature-name)


3. Commit your changes (git commit -m 'Add new feature')


4. Push to the branch (git push origin feature-name)


5. Open a Pull Request




---

# License

This project is licensed under the MIT License.

---

# Contact

Maintained by @root-cyze
