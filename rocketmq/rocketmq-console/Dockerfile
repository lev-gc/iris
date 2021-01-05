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

ENV NAMESRV_ADDR=127.0.0.1:9876
ENV CONTEXT_PATH=""
ENV VIP_CHANNEL=false
ENV JAVA_OPTS="-Xmx512m -Xms512m -Xss512k -XX:MaxDirectMemorySize=128M -Dfile.encoding=UTF-8"

WORKDIR /opt/rocketmq-console
ADD rocketmq-console-ng-1.0.0.jar /opt/rocketmq-console/
EXPOSE 9888

ENTRYPOINT ["sh", "-c", "java \
  $JAVA_OPTS \
  -Drocketmq.namesrv.addr=$NAMESRV_ADDR \
  -Dserver.port=9888 \
  -Dserver.contextPath=$CONTEXT_PATH \
  -Drocketmq.config.isVIPChannel=$VIP_CHANNEL \
  -jar \
  /opt/rocketmq-console/rocketmq-console-ng-1.0.0.jar\
  "]
