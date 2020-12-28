FROM python:3.6-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/traffic_director_system

COPY requirements.txt start-server.sh /opt/traffic_director_system/
COPY . /opt/traffic_director_system/
WORKDIR /opt/traffic_director_system
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /opt/traffic_director_system

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
RUN ls
CMD ["/opt/traffic_director_system/start-server.sh"]
