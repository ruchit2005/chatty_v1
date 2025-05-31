# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY backend/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire backend codebase
COPY backend/ .

# Expose FastAPI port
EXPOSE 8000

# Start the FastAPI server using correct module path
CMD ["uvicorn", "model.chatty_heart:app", "--host", "0.0.0.0", "--port", "8000"]
