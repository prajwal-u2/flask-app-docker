# Docker Containerization Guide

This repository demonstrates how to containerize a Flask application using Docker. The example app is a survey application that connects to a PostgreSQL database.

## What is Docker?

Docker allows you to package your application and its dependencies into a container that can run consistently across different environments. This ensures your app works the same way on your machine, your teammate's machine, and in production.

---

## Use Case 1: Just Run the App

**When to use:** You just want to run the application without building anything.

### Pull and run the published image
```bash
docker pull ghcr.io/prajwal-u2/flask-app-docker:latest
docker run -p 5001:5001 -e DATABASE_URL="postgresql://user:password@host:5432/dbname" ghcr.io/prajwal-u2/flask-app-docker:latest
```

**Note:** On macOS/Windows, use `host.docker.internal` instead of `localhost` to connect to services running on your host machine.

The app will be available at `http://localhost:5001`

---

## Use Case 2: Build and Modify the App

**When to use:** You want to modify the code, build your own image, or publish your own version.

### Build the Docker image
```bash
docker build -t survey-app .
```

### Run your built image
```bash
docker run -p 5001:5001 survey-app
```

Or with custom database URL:
```bash
docker run -p 5001:5001 -e DATABASE_URL="postgresql://user:password@host:5432/dbname" survey-app
```

### Publish to GitHub Container Registry (GHCR)

1. **Login to GHCR**
   Create a GitHub Personal Access Token with `write:packages` and `read:packages` permissions, then login:
   ```bash
   echo YOUR_GITHUB_TOKEN | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
   ```

2. **Build with GHCR tag**
   ```bash
   docker build -t ghcr.io/prajwal-u2/flask-app-docker:latest .
   ```

3. **Push to GHCR**
   ```bash
   docker push ghcr.io/prajwal-u2/flask-app-docker:latest
   ```

---

## Key Docker Concepts

- **Dockerfile**: Instructions for building your container image
- **Image**: A packaged application with all dependencies
- **Container**: A running instance of an image
- **Registry**: A place to store and share Docker images (like GHCR or Docker Hub)

## Project Structure

- `Dockerfile` - Defines how to build the container
- `survey_app.py` - Flask application
- `templates/` - HTML templates
- `static/` - CSS and JavaScript files
