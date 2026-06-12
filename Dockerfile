# Setup the image that everything will depend on
FROM python:3.14-alpine

# Create a folder in the container to work with
WORKDIR /backend

# Copy everything from here to the container
COPY . .

# Run big commands
# Make a venv and install dependencies, with cache cleanup
RUN apk add --no-cache bash python3 py3-pip && rm -rf /var/cache/apk/* && python3.14 -m venv .venv && .venv/bin/pip install --no-cache-dir -r app/requirements.txt

# Make the scripts executable
RUN chmod +x ./run.sh

# Port used by the backend
EXPOSE 8080

# Run the application
CMD ["/bin/bash", "./run.sh", "--strict"]