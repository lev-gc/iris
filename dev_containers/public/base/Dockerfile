FROM ubuntu:24.04

# set LANG
ENV LANG C.UTF-8


# install pkg
RUN apt-get update  \
    # install git
    && apt-get install -y git \
    # clean apt cache
    && apt-get clean  \
    && rm -rf /var/lib/apt/lists/*
