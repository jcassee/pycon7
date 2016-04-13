FROM python:3.5

MAINTAINER Joost Cassee <joost@cassee.net>

# Add parameterized entrypoint
ADD https://github.com/jcassee/parameterized-entrypoint/releases/download/0.9.0/entrypoint_linux_amd64 /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint

# Install Python packages
RUN pip install uwsgi psycopg2

# Configure run behavior
EXPOSE 80
ENTRYPOINT ["entrypoint", "--"]
CMD ["scripts/server.sh"]

# Copy sources
WORKDIR /srv
COPY . /srv
COPY local_settings.py.tmpl /templates/srv/local_settings.py

# Install dependencies
RUN pip install -r requirements.txt
