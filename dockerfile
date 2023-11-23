FROM python:3.11-alpine3.17

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0"]

EXPOSE 5000