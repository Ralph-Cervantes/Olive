FROM python:3.11-slim

WORKDIR /app

COPY pipelines/requirements.txt .
COPY data ./data
RUN pip install --no-cache-dir -r requirements.txt

COPY pipelines/dogs.py .

CMD ["python", "-u", "/app/dogs.py"]
