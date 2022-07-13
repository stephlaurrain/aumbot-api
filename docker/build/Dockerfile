FROM debian:bullseye-slim

ENV DEBIAN_FRONTEND noninteractive
ENV LSB_RELEASE=bullseye

WORKDIR "/root"
ADD /install/bdd/createdb.sql ./install/createdb.sql
RUN apt-get update && apt-get install -y nano \
    apt-utils \    
    xz-utils \ 
    wget \
    gnupg \
    ca-certificates \ 
    apt-transport-https \    
    supervisor \
    net-tools \
    mariadb-server --no-install-recommends; \  
    /etc/init.d/mariadb start; \
    mysql -u root < ./install/createdb.sql;
COPY /conf/50-server.cnf /etc/mysql/mariadb.conf.d/50-server.cnf
WORKDIR "/root" 
#RUN mkdir /root/tmp; \
#  apt-get clean; \  
COPY conf/supervisord.conf /etc/supervisor/conf.d
EXPOSE 3306
ENTRYPOINT ["/usr/bin/supervisord"]
