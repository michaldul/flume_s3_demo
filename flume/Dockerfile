FROM probablyfine/flume:latest

ENV FLUME_AGENT_NAME a1

ENV HADOOP_VERSION=3.1.0
ENV HADOOP_HOME=/opt/lib/hadoop-$HADOOP_VERSION

RUN mkdir /opt/lib && \
    wget -q http://www.eu.apache.org/dist/hadoop/core/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz -O /opt/lib/hadoop-$HADOOP_VERSION.tar.gz
RUN tar xzf /opt/lib/hadoop-$HADOOP_VERSION.tar.gz -C /opt/lib
RUN rm /opt/lib/hadoop-$HADOOP_VERSION.tar.gz

RUN cp /opt/lib/hadoop-$HADOOP_VERSION/share/hadoop/tools/lib/hadoop-aws-$HADOOP_VERSION.jar /opt/flume/lib/

RUN rm /opt/flume/lib/httpclient-4.2.1.jar
RUN rm /opt/flume/lib/jackson*

COPY rabbitmq-flume-plugin-standalone-1.0.3.jar /opt/flume/lib/
COPY aws-java-sdk-1.11.347.jar /opt/flume/lib/

ADD flume-env.sh /opt/flume-config/flume-env.sh
ADD flume.conf /opt/flume-config/flume.conf
