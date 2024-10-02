# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file first, to cache dependencies
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

RUN pip install flask

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

RUN chmod +x color_alert.py

# Define the default command to run the Python script
CMD python3 color_alert.py  # Replace with your actual Python script name
