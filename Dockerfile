FROM python:3.8.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]

