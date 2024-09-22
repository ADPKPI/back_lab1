FROM python:3.11.3-slim-bullseye

WORKDIR /lab1

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /lab1

CMD flask --app lab1 run -h 0.0.0.0 -p $PORT