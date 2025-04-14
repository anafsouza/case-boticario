FROM python:3.10


# Upgrade libraries
RUN apt update && apt upgrade -y

# Copy repository content to app
COPY . /app
WORKDIR /app/src

# Pip dependencies 
RUN pip install pip --upgrade && \
    pip install -r/app/src/requirements.txt --use-deprecated=legacy-resolver

# Expose api serving port 
EXPOSE 5000


# Add user and group app
RUN useradd -ms /bin/bash app
USER app


# Execute container
CMD ["sh", "-c", "python api_main.py"]