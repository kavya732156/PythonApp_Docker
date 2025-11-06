# Use an official Python image as the base
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file to install dependencies
COPY requirements.txt .

# Install the required Python packages
RUN pip install -r requirements.txt

# Copy all files from current folder to container
COPY . .

# Command to run the application
CMD ["python", "app.py"]
