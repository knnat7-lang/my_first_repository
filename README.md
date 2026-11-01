# My First Python Repository

## 1. Project Description

This is a beginner Python project that demonstrates
how to manage application configuration using
environment variables and the python-dotenv library.

The program loads configuration settings from a .env file,
checks required variables, uses default values for optional
settings, and displays whether a secret API key is loaded
without revealing its actual value.

## 2. Requirements

Before running this project, make sure you have:

- Python 3.10 or higher
- Git
- pip

## 3. Project Structure

my_first_repository/
│
├── .venv/
├── .env
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── main.py
└── requirements.txt

## 4. Installation

### Step 1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

Navigate to the project directory:

cd my_first_repository

### Step 2. Create a virtual environment

python -m venv .venv

### Step 3. Activate the virtual environment

For Windows PowerShell:
For powershell
.venv\Scripts\Activate.ps1

For macOS / Linux:
source .venv/bin/activate

### Step 4. Install dependencies

pip install -r requirements.txt

## 5. Configuration

The project uses a .env file to store configuration
variables.

First, create your local .env file by copying
the example configuration.

For Windows PowerShell:

Copy-Item .env.example .env

For macOS / Linux:

cp .env.example .env

Open the .env file and replace the example values
with your own configuration.

### Environment Variables

| Variable  | Required | Description                  |
| --------- | -------- | ---------------------------- |
| APP_NAME  | Yes      | Name of the application      |
| API_KEY   | Yes      | Secret API key               |
| LOG_LEVEL | No       | Logging level. Default: INFO |

### Example .env configuration

env
APP_NAME=My First Python Project
API_KEY=your_secret_api_key
LOG_LEVEL=DEBUG

Never commit your .env file to GitHub.

The .env file is excluded through .gitignore.

The .env.example file contains placeholder values
and can safely be committed to the repository.

## 6. Run the Project

After configuring the .env file, run:

python main.py

### Expected Output

Application name: My First Python Project
API_KEY loaded: True
Log level: DEBUG

The program displays the application name,
checks whether the API key is loaded,
and displays the logging level.

The actual API key is never printed.

### Missing Required Variables

If APP_NAME or API_KEY is missing,
the program terminates with a clear error message.

For example:

Error: API_KEY is missing!

### Default Value

LOG_LEVEL is an optional environment variable.

If LOG_LEVEL is not specified in the .env file,
the program automatically uses INFO.

Example output:

Application name: My First Python Project
API_KEY loaded: True
Log level: INFO

## 7. Git and Version Control

This project demonstrates basic Git operations:

- git init
- git add
- git commit
- git status
- git branch
- git switch
- git merge
- git log

### Branch Workflow

A separate branch named add-version-feature
was created to develop a new application version feature.

The following Git commands were used:

git switch main
git switch -c add-version-feature

After adding the application version feature:

git add main.py
git commit -m "Add application version"

The feature branch was merged into main:

git switch main
git merge add-version-feature

This demonstrates how to develop a feature
in a separate branch and merge it into the main branch.

## 8. Security Incident and Fix

As an additional Git practice exercise,
a fake .env file was intentionally committed
to demonstrate how to fix accidentally tracked secrets.

The file was subsequently removed from Git tracking
using:

git rm --cached .env

The .env file was also added to .gitignore
to prevent it from being committed again.

### Important Security Note

Removing .env from Git tracking does not remove
the file from previous commits or Git history.

If a real API key or other secret is exposed,
it must be revoked or rotated immediately.

Simply deleting the file or adding it to .gitignore
does not make an exposed secret safe again.

Only fake test credentials were used
for this exercise.

## 9. .gitignore

The following files and directories are excluded
from Git tracking:

# Python virtual environment

.venv/
venv/

# Environment variables and secrets

.env

# Python cache

**pycache**/
\*.py[cod]

# Operating system files

.DS_Store
Thumbs.db
Desktop.ini

# IDE and editors

.idea/
.vscode/

# Test and coverage files

.pytest_cache/
.coverage
htmlcov/

# Distribution files

dist/
build/
\*.egg-info/

## 10. License

This project is licensed under the MIT License.

See the LICENSE file for more information.

## 11. Author

Created as a beginner Python learning project.

The purpose of this project is to practice:

- Python programming
- Environment variables
- Configuration management
- Git and GitHub
- Virtual environments
- Project documentation
- Basic security practices
