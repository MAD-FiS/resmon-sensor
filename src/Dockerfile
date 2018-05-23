# Use an official Python runtime as a parent image
FROM python:3.5

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements

# Make port 80 available to the world outside this container
EXPOSE 4001

# Define environment variable
ENV NAME World


# Run app.py when the container launches
ENTRYPOINT ["python3", "/app/main.py","-a", "http://217.182.73.67:4001", "-i", "15", "-b", "10", "-n", "workstation1"]

