# My First Python Repository

## Description

This is my first Python project.
The program loads configuration variables
from a .env file using python-dotenv.

It reads:

- APP_NAME: application name
- API_KEY: secret API key

The program displays the application name
and checks whether the API key is loaded
without revealing the secret.

## Requirements

- Python 3
- python-dotenv

## Installation

1. Clone the repository:
   git clone https://github.com/knnat7-lang/my_first_repository.git

2. Create a virtual environment:

   python -m venv .venv

3. Activate the virtual environment:

   Windows PowerShell:

   .venv\Scripts\Activate.ps1

4. Install dependencies:

   pip install -r requirements.txt

5. Create your .env file using .env.example
   as a template.

6. Run the program:

   python main.py

## Environment Variables

The project requires:

| Variable | Description      |
| -------- | ---------------- |
| APP_NAME | Application name |
| API_KEY  | Secret API key   |

Never commit your .env file.

## Project Structure

my_first_repository/

- main.py
- .env
- .env.example
- .gitignore
- README.md
- requirements.txt

## Author

My First Python Project
