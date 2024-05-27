from python:3.10-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip

RUN pip install -r /requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 3000

ENTRYPOINT [ "python" ]

CMD ["main.py" ]