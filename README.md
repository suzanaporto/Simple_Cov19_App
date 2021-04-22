# Simple Cov19 App

Simple web app using Flask as an example to explain how Docker works.

## How to run

- Using the virtual environment approach
  - Create a venv
    ```
    python -m venv venv
    source covid19_api/bin/activate
    ```
  - Install requirements.txt
    ```
    pip install -r requirements.txt
    ```
  - Set environment variables
    ```
    export FLASK_APP=main.py
    ```
  - Run the app
    ```
    flask run
    ```

- Using the Docker approach
  - Run docker-compose commands
    ```
    docker-compose build && docker-compose up -d
    ```