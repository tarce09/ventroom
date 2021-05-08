# Foxxie
Anonymous Chat room using ASGI with profanity filter and sentiment analyzer.
The main purpose is to provide a safe space for people to vent their emotions out. Our goal is to help achieve a better future in the field of mental health.


1. Install [Docker](https://docs.docker.com/get-docker/)
2. Run redis server `docker run -p 6379:6379 -d redis:5 `  
3. Install requirements using pip, from requirements.txt  
4. `python ventroom/manage.py makemigrations`
5. `python ventroom/manage.py migrate`
6. `python ventroom/manage.py runserver`
