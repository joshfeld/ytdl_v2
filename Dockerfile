# syntax=docker/dockerfile:1
FROM python:3.10
WORKDIR /ytdl
ENV FLASK_APP=ytdl.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt-get update && apt-get install ffmpeg -y
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install youtube-dl
EXPOSE 5000
COPY . .
CMD ["flask", "run"]