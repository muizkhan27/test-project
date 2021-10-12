# Ompractice Take Home Assignment (October 2021)
This is the code sample that will be used for the technical screen when **take-home assignment** is selected as the interviewee's preference.

1. Fork this repository
1. Set up your local environment by following the **Setup** instructions below
1. In the `frontend` React app, create a page that **lists out how many hours per month that each teacher is teaching online classes**.
    
    For example, Vinny may be teaching 60 minutes in January, 120 minutes in February, and 85 minutes in March while Mindy is teaching 160, 90, and 115 respectively.

    You can display this information any way that you see fit, whether that is with a table, a graph, or simply sections on a page.

## Setup

### Backend (Django REST Framework)

#### Set up a Python virtual environment
In the VS Code terminal, in your project's directory, run this command:

Mac or Linux:
```
python -m venv .venv
```

Windows:
```
py -m venv .venv
````

If this is successful, you should see a new .venv directory appear in your project directory. This will be ignored by source control because of the .gitignore file.

#### Activate your Python virtual environment

Mac or Linux:
```
source .venv/bin/activate
```

Windows:
```
source env\Scripts\activate
```

#### Install packages

[Install pip](https://pip.pypa.io/en/stable/installation/#supported-methods):
```
python -m ensurepip --upgrade
```

Run these commands to navigate into the backend directory and install required packages:
```
cd ./backend
pip install -r requirements.txt
```

#### Run migrations

From the `backend` directory, run all of the migration scripts:
```
python ./manage.py migrate
```

#### Create a superuser

Replace admin@example.com with your own email address
```
python manage.py createsuperuser --email admin@example.com --username admin
```

#### Run the server

From the `backend` directory, run the server:
```
python ./manage.py runserver
```

### Frontend (Next.js React app)

#### Install Node.js, npm, and yarn

1. [Download and install Node.js and npm](https://nodejs.org/en/)
1. Install yarn, which we will use to run the Next project:
    ```
    npm install --global yarn
    ```

#### Run the web app

1. Change into the `frontend directory`
    ```
    cd ./frontend
    ```
1. Start the app in development mode
    ```
    yarn dev
    ```