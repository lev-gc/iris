# rocketmq-console

The image of rocketmq-console for rocketmq.

## Steps

- Build with the maven images;
- Get the source code from [rocketmq-externals](https://github.com/apache/rocketmq-externals), tag: [rocketmq-console-1.0.0](https://github.com/apache/rocketmq-externals/archive/rocketmq-console-1.0.0.zip);
- Extract the source code and cd to the path `/rocketmq-console`;
- Run command `mvn clean package -Dmaven.test.skip=true` to build the jar;
- Copy the jar to the jre image;
