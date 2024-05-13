FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./packages ./packages

COPY ./app ./app

EXPOSE 8080

CMD exec uvicorn app.server:app --host 0.0.0.0 --port 8080
