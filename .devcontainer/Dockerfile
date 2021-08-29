FROM alpine:latest

RUN apk update && \
    apk add bash git python3 py3-pip --no-cache && \
    apk add micropython --no-cache --repository http://dl-2.alpinelinux.org/alpine/edge/testing/ --allow-untrusted