FROM python:3.10-slim

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

EXPOSE 8000

CMD ["uvicorn", "model.chatty_heart:app", "--host", "0.0.0.0", "--port", "8000"]
