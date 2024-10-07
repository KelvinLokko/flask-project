# Flask Application - Basic Project

## Overview
This is a basic Flask web application that serves as a starting point for building web applications with Flask. The application is designed to demonstrate the core functionality of a Flask app, including routing, serving HTML content, and basic CSS styling.

## Features
- **Home Page**: A simple homepage that displays "Hello, Flask!" when accessed.
- **Navigation**: An optional navigation bar for easy access to different routes within the application.
- **Basic Styling**: Basic CSS styling to enhance the look and feel of the application.
- **Dynamic Routes**: Includes predefined routes that can be used as a template to add more functionalities.

## Installation
To run this application on your local machine, follow these steps:

1. **Create and Activate a Virtual Environment**:
   - Open Command Prompt and navigate to your project directory:

     ```bash
     cd path\to\my_flask_project
     ```

   - Create a virtual environment:

     ```bash
     python -m venv myenv
     ```

   - Activate the virtual environment:

     ```bash
     myenv\Scripts\activate
     ```

     After activating the virtual environment, your command prompt should show `(myenv)` at the beginning.

2. **Install Dependencies**:
   - Install the required dependencies listed in `requirements.txt`:

     ```bash
     pip install -r requirements.txt
     ```

   - If you don't have a `requirements.txt` file, manually install Flask:

     ```bash
     pip install Flask
     ```

3. **Run the Application**:
   - With the dependencies installed, start the Flask app:

     ```bash
     python app.py
     ```

   - By default, the application will run on `http://127.0.0.1:5000/`. Open a web browser and go to that URL to view the homepage.

## Usage
- **Home Page**: Displays a welcome message and provides navigation links.
- **About Page**: You can create an additional `about` route in `app.py` to include details about your application.
- **Services and Contact Pages**: These can be added by creating new HTML templates and defining routes for them in `app.py`.



