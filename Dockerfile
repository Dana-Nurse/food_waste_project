# Start with the Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy only the requirements file first (for efficient layer caching)
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the Flask environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expose the port Flask runs on
EXPOSE 5000

# Start the app
CMD ["flask", "run", "--host=0.0.0.0"]
