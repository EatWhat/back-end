FROM alpine
MAINTAINER two@qq1285580823
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    cp /etc/apk/repositories /etc/apk/repositories.bak && \
    echo "http://mirrors.aliyun.com/alpine/v3.4/main/" > /etc/apk/repositories && \
    apk update && \
    apk add python3 && \
    apk add mysql-client && \
    pip3 install --upgrade pip && \
    pip3 install tornado && \
    pip3 install pyyaml && \
    pip3 install pymysql

ADD . /eatwhat
WORKDIR /eatwhat


CMD ["bash"]
