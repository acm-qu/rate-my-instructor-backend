# Setup the image that everything will depend on
FROM python:3.14-slim

# Create a folder in the container to work with
WORKDIR /src

# Copy everything from here to the container
COPY . .

RUN apt-get update && apt-get install -y python3

RUN pip3 install -r app/requirements.txt

# Make the scripts executable
RUN chmod +x ./scripts/*

# Run the application
# -s: strict mode
CMD ["./scripts/run.sh", "--strict"]