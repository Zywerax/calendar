FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY main.py .

# Kopiuj cały projekt do kontenera
COPY . .

CMD ["python", "main.py"]
