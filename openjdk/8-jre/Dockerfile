FROM openjdk:8-jre-slim

# procps -> ps
# telnet -> telnet
# iputils-ping -> ping
# net-tools -> ifconfig
# curl -> curl
# vim -> vim
RUN set -eux; \
  apt-get update; \
  apt-get install -y --no-install-recommends \
  procps \
  telnet \
  iputils-ping \
  net-tools \
  curl \
  vim \
  ; \
  rm -rf /var/lib/apt/lists/*
