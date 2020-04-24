FROM python:3.7.5-alpine

RUN apk update && apk add libpq

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    && apk del --no-cache .build-deps

RUN apk add build-base jpeg-dev zlib-dev

RUN apk add freetype-dev musl-dev libpng-dev

	#libjpeg-dev libjpeg8-dev libpng3 libfreetype6-dev

ENV LIBRARY_PATH=/lib:/usr/lib

RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow==5.4.1

WORKDIR /usr/src/barcode

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/barcode

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#ENTRYPOINT ["python"]
COPY . /usr/src/barcode