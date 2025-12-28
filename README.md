📥 Step 1: Download the project
Option A: Using Git (recommended)
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

Option B: Without Git

Click the green Code button on GitHub

Click Download ZIP

Extract the ZIP file

Then open the project folder.

🧪 Step 2: Create a virtual environment

Inside the project folder, run:

python -m venv venv

Activate it

Windows

venv\Scripts\activate


Mac / Linux

source venv/bin/activate


You will see (venv) — this is good 👍

📦 Step 3: Install required packages

Run this command:

pip install -r requirements.txt


Wait until it finishes.

🗄 Step 4: Set up the database

Run:

python manage.py migrate

🚀 Step 5: Start the project

Run:

python manage.py runserver


You will see something like:

Starting development server at http://127.0.0.1:8000/

🌍 Step 6: Open the website

Open your browser and go to:

👉 http://127.0.0.1:8000/

🎉 You are done! The project is running.

🛑 If something goes wrong

Try these:

Make sure Python is installed

Make sure (venv) is activated

Run commands inside the project folder

❤️ Made with Django

This project uses:

Django

Tailwind CSS

SQLite (default database)