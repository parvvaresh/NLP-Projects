FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
COPY app.py ./
COPY static ./
COPY templates ./
COPY final_models ./
COPY pipline_predict.py ./

RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*
    

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
