#!/bin/sh

#install mongodb
#安装教程 https://blog.csdn.net/rzrenyu/article/details/79472509
install_mongodb(){
    echo "start install mongodb......"
    tar -zxvf ./mongodb-linux-x86_64-rhel70-4.0.2.tgz 
    mv mongodb-linux-x86_64-rhel70-4.0.2 /usr/local/mongodb
    mkdir -p /usr/local/mongodb/data/db
    mkdir -p /usr/local/mongodb/logs
    mkdir -p /etc/mongodb
    cp ./mongodb.conf /etc/mongodb/
    # 系统环境变量配置(最好手动去配置)
    grep MONGODB_HOME /etc/profile
    if [ $? != 0 ];then
        echo "export MONGODB_HOME=/usr/local/mongodb" >> /etc/profile
        echo "export PATH=\$PATH:\$MONGODB_HOME/bin" >> /etc/profile
        source /etc/profile
    fi
    # 启动mongodb服务
    mongod -f /etc/mongodb/mongodb.conf
    # 停止mongodb服务
    #mongod -f /etc/mongodb/mongodb.conf  --shutdown
    echo "mongodb install finished!"
}

#install redis
#如果编译失败，可能是gcc没有安装，安装教程：https://www.linuxidc.com/Linux/2017-03/142319.htm
install_redis(){
    echo "start install redis......"
    tar -zxvf ./redis-4.0.11.tar.gz
    cd ./redis-4.0.11
    make
    make install
    rm -rf ./redis-4.0.11
    mkdir -p /etc/redis
    cp ./redis.conf /etc/redis/
    mkdir -p /var/log/redis
    mkdir -p /var/lib/redis
    # 启动redis服务
    redis-server /etc/redis/redis.conf
    echo "redis install finished!"
}


# mv ./*  /usr/lib64/python2.7/site-packages/
# 安装pip、gcc
# sudo yum -y install epel-release
# sudo yum -y install python-pip
# sudo yum -y install gcc gcc-c++

#install tutorial
install_tutorial(){
    echo "start install tutorial......"
    zip tutorial.zip   
    mkdir -p /var/www/
    mv ./tutorial /var/www/
}
setup(){
    install_mongodb
    install_redis
}

setup
