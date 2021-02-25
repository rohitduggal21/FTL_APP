### FTL_APP
    - Objective:
                  (1) Populate a backend-database using django's custom management command with 2 data models. 
                  (2) Create an API endpoint for the generated data.
                  (2) Deploy the application on PythonAnywhere.

    - Dependencies:
                  (1) django: pip3 install django
                  (2) Faker: pip3 install Faker
                 
    - Overview:
                  (1) getData app under the PROJECT_DIR (FTL_APP) contains the model definitions(models.py) and views(views.py) that drive this application.
                  (2) getData/management/commands/populate_data.py is responsible for generating dummy data with the help of Faker library.
               
    - Instructions:
                  (1) Get inside FTL_APP repository.
                  (2) Execute: python3 manage.py migrate
                  (3) For a test run, execute python3 manage.py runserver, go to localhost:8000 on a web browser, you should see a welcome message.
                  (4) To populate dummy data, execute: python3 manage.py populate_data
                  (5) Go to localhost:8000/getData on a web browser to see the populated data.
