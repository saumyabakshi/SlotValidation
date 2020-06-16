FROM python:3.7.4-alpine3.10

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ADD . /usr/src/app

EXPOSE 8000

CMD exec gunicorn ValidateValues.wsgi:application --bind 0.0.0.0:8000 --workers 1
