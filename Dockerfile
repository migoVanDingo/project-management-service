FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (including git)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Verify git installation
RUN git --version

# Set environment variable for GitPython
ENV GIT_PYTHON_GIT_EXECUTABLE=/usr/bin/git

# Copy the current directory contents into the container
COPY . /app

RUN pip install --upgrade pip

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 5013

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5013"]
