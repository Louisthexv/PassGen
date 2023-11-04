# Password Replacement Tool

## Introduction

The Password Replacement Tool is a Python script designed to enhance the security of your stored passwords by generating strong and memorable passphrases. It is intended for users who have identified compromised passwords and want to replace them with stronger alternatives.

## Motivation

The idea for this tool was born out of the need to strengthen passwords in the wake of discovering leaked credentials. Services like "Have I Been Pwned" and password management tools often detect and alert users to potentially compromised passwords. Exporting saved passwords from browsers or password managers as CSV files led to the creation of this tool. Rather than using random, complex, and difficult-to-remember passwords, the tool generates passphrases that offer both security and memorability.

## Features

- Replaces existing passwords with passphrases.
- Utilizes a customizable dictionary of words, enabling passphrases in multiple languages.
- Removes accents and special characters to improve password compatibility.
- Generates passphrases comprising two random words and a two-to-four-digit number for added security.

## Prerequisites

To use this tool, you'll need:

- Python installed on your system.
- The 'unicodedata' library, which can be installed using 'pip install unicodedata'.

## Usage

1. Clone or download the repository to your local machine.

2. Install the required 'unicodedata' library if not already installed: `pip install unicodedata`.

3. Prepare a CSV file with the following structure:
   - Column A: URLs or website names
   - Column B: Usernames
   - Column C (starting from C2): Existing passwords you want to replace

4. Customize the 'spanish_dictionary.txt' file or use dictionaries in other languages as needed. Place them in the same directory.

5. Run the tool with the following command:

python password_replacement.py input.csv output.csv

Replace 'input.csv' with the name of your input CSV file and 'output.csv' with the desired output filename.

6. The tool will generate new passwords in column D (starting from D2) in the output CSV file.

## Recommendations

- Create a virtual environment (venv) to isolate the tool's dependencies and not interfere with your system's Python environment.
- Consider using containerization technologies like Docker to run the script in a controlled environment.

## Author

Louisthexv

## License
