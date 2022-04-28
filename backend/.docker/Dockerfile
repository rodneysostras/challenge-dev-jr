FROM python:3.10.4-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /dev/app/backend

RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
    gcc python3-dev \
    postgresql libpq-dev \
    && find / -type f -iname \*.apk-new -delete \
    && rm -rf /var/cache/apk/* \
    && mkdir -p /dev/app/backend

COPY ../ /dev/app/backend/

EXPOSE 8080

ENTRYPOINT ["/bin/sh"]
