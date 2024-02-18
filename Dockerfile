# Start from base Python image
FROM python:3.8-alpine

# Set working directory
WORKDIR /home

# Install Bash
RUN apk add --no-cache bash

# Create directories for data and output
RUN mkdir -p /home/data /home/output

# Copy all files from host to container's /home/data
COPY . /home/data  

# Copy result.txt to /home/output
RUN touch /home/output/result.txt

# Copy over the python script
COPY start.py /home/data/

# Give execute permissions to script and write permissions to file
RUN chmod +x /home/data/start.py
RUN chmod +w /home/output/result.txt

# Run the python script when container starts  
CMD ["python", "/home/data/start.py"]
