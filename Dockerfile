FROM python:3.12-slim

WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir \
    flask \
    flask-sqlalchemy \
    python-dotenv \
    psycopg2-binary \
    gunicorn

# Copy application files
COPY survey_app.py .
COPY templates/ ./templates/
COPY static/ ./static/

# Set default DATABASE_URL 
ENV DATABASE_URL="postgresql://postgres@host.docker.internal:5432/hw1_survey"

# Expose Flask port
EXPOSE 5001

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "survey_app:app"]
