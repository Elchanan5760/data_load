FROM python:3.12-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

COPY . . /app/
# Expose the port where server will run
EXPOSE 5000

# Command to start training service
CMD ["/bin/bash", "-c", "--", "while true; do sleep 30; done;"]