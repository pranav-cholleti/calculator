# Calculator

## Description
A simple calculator web application built with Django. This project allows users to perform basic arithmetic operations through a web interface.

## Features
-   Addition
-   Subtraction
-   Multiplication
-   Division

## Tech Stack
-   **Backend:** Python, Django
-   **Frontend:** HTML

## Installation
1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd calculator
    ```
2.  Set up a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  Install Django:
    ```bash
    pip install django
    ```
4.  Run migrations (if any database setup is needed):
    ```bash
    python manage.py migrate
    ```

## Usage
1.  Run the Django development server:
    ```bash
    python manage.py runserver
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:8000/`.
3.  Use the interface to input numbers and select an operation to see the result.

## Project Structure
-   `calculator/`: Django project settings and configuration.
    -   `settings.py`: Project settings.
    -   `urls.py`: Main URL routing.
-   `calculatorapp/`: The main Django application.
    -   `views.py`: Handles the logic for calculator operations and rendering templates.
    -   `urls.py`: Application-specific URL routing.
    -   `models.py`: (Not used for this simple calculator, but part of Django app structure).
    -   `templates/`: Contains HTML templates for the user interface.
        -   `home.html`: The main page with input fields and operation selection.
        -   `result.html`: Displays the calculation result.
-   `manage.py`: Command-line utility for Django project management.
