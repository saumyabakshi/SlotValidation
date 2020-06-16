FROM python:3.7.4-alpine3.10

ADD ValidatValues/requirements.txt /app/requirements.txt
RUN /env/bin/pip install --no-cache-dir -r /app/requirements.txt
ADD ValidatValues /app
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "ValidatValues.wsgi:application"]