# YTDL
A locally-hosted solution for downloading videos.

## Running the app
First, clone the repo wherever you'd like. Open up `docker-compose.yml` and update the second volume to point wherever you want the files to be stored when they are downloaded. After that, simply run `docker compose up -d` and open up your browser to `localhost:5000`. The port can be changed in `docker-compose.yml` if desired.
