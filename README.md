# Ompractice Take Home Assignment (October 2021)
This is the code sample that will be used for the technical screen when **take-home assignment** is selected as the interviewee's preference.

1. Fork this repository
1. Set up your local environment by following the **Setup** instructions below
1. In the `frontend` React app, create a page that **fetches data from the backend and lists out how many hours per month that each teacher is teaching online classes**.
    
    For example, Vinny may be teaching 60 minutes in January, 120 minutes in February, and 85 minutes in March while Mindy is teaching 160, 90, and 115 respectively.

    You can display this information any way that you see fit, whether that is with a table, a graph, or simply sections on a page.
    
1. Please share your code with Ompractice before your technical screen so that they can review it in advance and prepare questions.

## FAQ

### How will this be assessed?
We will be looking for the following:

- You've solved the assignment (i.e. you list out hours each teacher is teaching per month)
- You've demonstrated you know how to create React components
- You've demonstrated you know how to make API calls
- You follow modern, reasonable conventions when writing JavaScript code
- You can talk through your thought processes during the interview
- You can clearly talk through the enhancements you'd make to this codebase -- whether or not you had time to fully implement them

### Which endpoint should I use to grab class data?
http://localhost:8000/api/classes/

The above endpoint has already been created for you, but you are welcome to change it or write a new one that better fits your approach.

### How long should I spend on this?
**1-2 hours** at most. We are sensitive to the fact you're taking time out of your day to complete this part of the technical interview, and so we only expect that you to complete the crux of the assignment (i.e. building a React page that fetches data from the server and displays it as described above). Depending on how quickly you complete this part, you are welcome to make enhancements, but that is not required.

### But it will take me more than a couple hours to make the page pretty / improve the API endpoint / write test coverage / et cetera...
After two hours, if you haven't gotten to all of the enhancements that you'd like to do to show off your skills, don't worry! Instead, **list out the enhancements you would make** and be prepared to talk through them during the technical interview. "I wanted to do XYZ but didn't have time to implement it" is absolutely fine so long as you can clearly walk through your thought process and software development approaches during the actual interview.

### Why did you give us starter code?
We are sensitive to your time and care more that you can show off your code-writing and code-comprehension skills than that you can create boilerplate Django and Next code.

### Can I change the backend and API endpoint?
Absolutely! For the sake of time, we implemented a very simple API endpoint for you to fetch the online class list from, but you are more than welcome to make changes to this endpoint. You can also just leave it as-is and be prepared to talk through the changes you would make during the interview.

### How pretty do I need to make this?
It's up to you! If you're a pixel-pusher and you have time to spare after completing the main part of the assignment, go to town showing off your CSS skills. However, if your strengths lie elsewhere, focus your limited time on showing off those instead. Additionally, you can always jot down the changes you would make given more time and simply talk through them during the interview process.

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

- Endpoint from which to GET a list of classes: http://localhost:8000/api/classes/
- Admin endpoint for viewing data (use your superuser account to log in): http://localhost:8000/admin/

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