# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD ./install-sensor.sh /app

# Install any needed packages specified in requirements.txt
RUN /app/install-sensor.sh --quiet

# Make port 80 available to the world outside this container
EXPOSE 4001


# Run app.py when the container launches
ENTRYPOINT ["/app/resmon-sensor","-a", "http://217.182.73.67:4001", "-i", "15", "-b", "10", "-n", "jenkins"]

