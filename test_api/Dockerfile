FROM python:3.13-alpine 
# Use the latest Python 3.13 Alpine image

WORKDIR /app 
# Set the working directory to /app

RUN apk add --no-cache gcc musl-dev libffi-dev
# Install build dependencies
# Install any other dependencies you need for your application
# For example, if you're using FastAPI, you might need to install uvicorn and fastapi

COPY requirements.txt .
# Copy the requirements file to the container
# This file should contain all the dependencies your application needs
# For example:
# fastapi
# uvicorn
# If you're using other libraries, make sure to include them in the requirements.txt file

RUN pip install --no-cache-dir -r requirements.txt
# Install the Python dependencies
# The --no-cache-dir option prevents pip from caching the installed packages, reducing the image size
# If you have a requirements-dev.txt file for development dependencies, you can install it here as well

COPY ./app ./app
# Copy the application code to the container
# Make sure to adjust the path according to your project structure
# If your application code is in a different directory, change the path accordingly
# For example, if your application code is in a directory named "src", you would use COPY ./src ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Start the application using Uvicorn
# The app.main:app part should be adjusted according to your application structure
# For example, if your FastAPI app is in a file named "main.py" inside the "app" directory, you would use app.main:app
# If you're using a different ASGI server, you can replace "uvicorn" with the appropriate command
# If you want to run the application in development mode, you can use the --reload option

