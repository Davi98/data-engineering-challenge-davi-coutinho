
# Use the official lightweight Python image.
# https://hub.docker.com/_/python
# docker build -t challenge .  
# docker run -p 8080:8080 challenge


FROM python:3.7-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
EXPOSE 8080
# Install production dependencies.
RUN pip install -r requirements.txt
# RUN python -m tests.test


# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.

COPY commands.sh /scripts/commands.sh
RUN ["chmod", "+x", "/scripts/commands.sh"]
ENTRYPOINT ["/scripts/commands.sh"]
# ENTRYPOINT ["python"] 
# CMD ["webapp.py"]
# ENTRYPOINT [ "python" ]
# CMD ["-m tests.test"]