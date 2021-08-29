FROM debian:stretch-slim

RUN apt-get update && \
    apt-get install -y build-essential libffi-dev git pkg-config python python3 && \
    rm -rf /var/lib/apt/lists/* && \
    git clone https://github.com/micropython/micropython.git && \
    cd micropython && \
    git submodule update --init && \
    cd mpy-cross && \
    make && \
    cd .. && \
    cd ports/unix && \
    make axtls && \
    make && \
    make install && \
    cd ../../.. && \
    rm -rf micropython