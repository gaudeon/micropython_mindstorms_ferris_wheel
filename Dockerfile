FROM alpine:latest

RUN apk update && \
    apk add micropython --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted

ENTRYPOINT ["/usr/bin/micropython"]