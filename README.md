### FTL_APP
    - Dependencies:
                  (1) django: pip3 install django
                  (2) Faker: pip3 install Faker
                  
    - Instructions:
                  (1) Get inside FTL_APP repository.
                  (2) Execute: python3 manage.py migrate
                  (3) For a test run, execute python3 manage.py runserver, go to localhost:8000 on a web browser, you should see a welcome message.
                  (4) To populate dummy data, execute: python3 manage.py populate_data
                  (5) Go to localhost:8000/getData on a web browser to see the populated data.
