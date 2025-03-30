# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose Flask server port
EXPOSE 5000

# Start the Flask server
CMD ["python", "server.py"]

