# Use an official Python runtime as a parent image
FROM ubuntu_python3-5

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
ENTRYPOINT ["python3", "/app/main.py","-a", "http://192.168.251.193:4001", "-i", "1", "-b", "10"]

