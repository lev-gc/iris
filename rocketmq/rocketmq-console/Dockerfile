FROM maven:3.6.3-openjdk-8
WORKDIR /workspace
RUN wget https://github.com/apache/rocketmq-externals/archive/rocketmq-console-1.0.0.zip; \
  unzip rocketmq-console-1.0.0.zip; \
  cd rocketmq-externals-rocketmq-console-1.0.0/rocketmq-console/; \
  mvn clean package -Dmaven.test.skip=true

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

ENV \
NAMESRV_ADDR=127.0.0.1:9876 \
CONTEXT_PATH="" \
VIP_CHANNEL=false \
JAVA_OPTS="-Xmx512m -Xms512m -Xss512k -XX:MaxDirectMemorySize=128M -Dfile.encoding=UTF-8"

WORKDIR /opt/rocketmq-console
COPY --from=0 /workspace/rocketmq-externals-rocketmq-console-1.0.0/rocketmq-console/target/rocketmq-console-ng-1.0.0.jar /opt/rocketmq-console/
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
