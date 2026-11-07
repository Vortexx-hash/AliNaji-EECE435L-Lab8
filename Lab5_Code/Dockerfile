# Image 1: Lab 5 Flask + SQLite user API on port 5000
FROM python:3.12-alpine

WORKDIR /app

# copy only the requirements first so the dependency layer is cached
COPY requirements.docker.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the code (venv etc. are excluded by .dockerignore)
COPY . /app

EXPOSE 5000
CMD ["python3", "app.py"]
