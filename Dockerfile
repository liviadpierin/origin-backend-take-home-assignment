# Use official Python image as parent
FROM python:3-alpine

# Install temporary dependencies needed for WSGI installation
RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev
			
# Installing WSGI			
RUN apk add --no-cache pcre

# Set the working directory to /app
WORKDIR /app

# Copy /app local contents into the container /app
ADD ./app /app

# Copy the requirements into the container at /etc
ADD ./requirements.txt /etc

# Install all dependencies specified in requirements.txt
RUN pip install -r /etc/requirements.txt

# Delete dependencies no longer needed
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*

# Make port 8080 available from outside container
EXPOSE 8080