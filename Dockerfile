# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies from requirements.txt (if you have one)
# RUN pip install --no-cache-dir -r requirements.txt

# If your script doesn't have external dependencies, skip the previous step

# Set the entry point to the Python script
CMD ["python", "./color_alert.py"]
