# Ompractice Take Home Assignment (October 2021)

1. This application fetches month-wise data for each teacher and renders it in a table
2. Set up your local environment by following the **Setup** instructions below
3. A new endpoint has been created to fetch month-wise teacher data
4. A Next.js app for frontend is developed with components and classes for each taking into account best pracitces that should be used while developing Next.js (React) app
    

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

Note the following endpoints:

- Endpoint from which to GET month-wise time for each teacher: http://localhost:8000/api/teachers/info
- Admin endpoint for viewing data (use your superuser account to log in): http://localhost:8000/admin/

### Frontend (Next.js React app)

#### Install Node.js, npm, yarn, and next

1. [Download and install Node.js and npm](https://nodejs.org/en/)
1. Install yarn, which we will use to run the Next project:
    ```
    npm install --global yarn
    ```
1. Install Next.js
    ```
    npm install next
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

## Suggestions and Enhancement
Following are the suggestions to enhance the overall experience
1. Graphs for each teacher can be displayed. Select the name of a teacher from the dropdown to display the graph
2. All of the teachers data can be shown in a single graph with color-coding. Months can be plotted on X-axis whereas hours can be plotted on Y-axis
3. A dashboard can be developed where different types of graphs or stats can be viewed