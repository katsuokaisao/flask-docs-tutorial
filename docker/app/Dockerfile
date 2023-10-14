FROM python:3.12.0-alpine3.18

WORKDIR /app

RUN apk update && \
    apk add --no-cache \
    bash \
    vim \
    && rm -rf /var/cache/apk/*

RUN pip install --upgrade pip && \
    pip install pipenv

COPY ./app/ .

RUN pipenv install

CMD ["bash", "-c", "pipenv run flask --app flaskr --debug run -h 0.0.0.0 -p 4567"]