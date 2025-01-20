FROM python:3.10.0-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /app

COPY config.py /app/config.py

CMD ["flask", "--app", "ModulesFolder", "run", "-h", "0.0.0.0", "-p", "5000"]


