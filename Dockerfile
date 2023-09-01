# Sets the base image for subsequent instructions
FROM python:3.11.5-alpine
# Sets the working directory in the container  
WORKDIR /app
# Copies the dependency files to the working directory
COPY requirements.txt /app/requirements.txt
# Install dependencies
RUN pip install -r requirements.txt
# Copies everything to the working directory
COPY . /app
# Command to run on container start    
CMD [ "gunicorn" , "-b", "0.0.0.0:5000", "app:app" ]