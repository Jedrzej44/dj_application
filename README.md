# Car Rental Website

The project is a web application for a car rental service which allows users to check what cars are available today and reserve one of them. 
Application built with Django & CSS.

## Features

- View cars available today
- Filter cars by type, color, seats, and price per day
- Make reservation
- Admin panel with editable Cars, Clients and Reservations
- Responsive design using Bootstrap

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Jedrzej44/dj_application.git

2. Create a virtual environment and activate it:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install requirements:
   pip install -r requirements.txt
   
4. Apply migrations and run server:
    ```sh
    python manage.py makemigrations
    
    python manage.py migrate
    
    python manage.py runserver

6. Open your browser and visit http://127.0.0.1:8000 to see the application in action.

## Usage

See home page by typing http://127.0.0.1:8000/home - from this view you can navigate to make a reservation.
Check also http://127.0.0.1:8000/admin to see admin panel.





   
