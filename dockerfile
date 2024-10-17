FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
COPY app.py ./
COPY final_models ./

RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*
    

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
