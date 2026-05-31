# Setup the image that everything will depend on
FROM python:3.14-slim

RUN apt-get update && apt-get install -y python3

RUN pip3 install -r app/requirements.txt

# Create a folder in the container to work with
WORKDIR /src

# Copy everything from here to the container
COPY . .

# Make the scripts executable
RUN chmod +x ./scripts/*

# Run the application
# -s: strict mode
RUN ./scripts/run.sh --strict