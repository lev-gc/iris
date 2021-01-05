FROM openjdk:8-jre-slim

RUN set -eux; \
  apt-get update; \
  apt-get install -y --no-install-recommends \
  busybox \
  curl \
  ; \
  rm -rf /var/lib/apt/lists/*; \
  ln -s /bin/busybox /bin/ps; \
  ln -s /bin/busybox /bin/ping; \
  ln -s /bin/busybox /bin/ifconfig; \
  ln -s /bin/busybox /bin/curl; \
  ln -s /bin/busybox /bin/vi
