# flask-app-docker
This repository provides a base and example project for an application that can be containerized with Docker.


# App run commands
docker build -t survey-app .
docker run -p 5001:5001 survey-app

docker run -p 5000:5000 -e DATABASE_URL="your-database-url" survey-app