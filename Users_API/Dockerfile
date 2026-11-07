# Image 2: GET /get_users API on port 3000
FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 3000
CMD ["python3", "app.py"]
