# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only the requirements.txt from one level up
COPY ../requirements.txt /app/requirements.txt

# Copy all app code from current folder
COPY . /app/

# Install dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Start the FastAPI server
CMD ["python", "-m", "uvicorn", "chatty_heart:app", "--host", "0.0.0.0", "--port", "8000"]
