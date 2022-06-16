#!/bin/sh
docker build -t challenge . \
&& docker run  -p 8080:8080 -e GOOGLE_APPLICATION_CREDENTIALS=credentials.json challenge
