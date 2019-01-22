FROM centos:6.7
ADD /${PATH}/jre-8u181-linux-x64.tar.gz /usr/home/java/
RUN { \
        echo; \
        echo 'JAVA_HOME=/usr/home/java'; \
        echo 'export JRE_HOME=/usr/home/java/jre1.8.0_181'; \
        echo 'export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH'; \
        echo 'export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH'; \
        echo; \
    } >> /etc/profile \
    && { \
        echo; \
        echo 'source /etc/profile'; \
        echo; \
    } >> ~/.bashrc
