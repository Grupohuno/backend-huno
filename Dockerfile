FROM python:3.10-alpine3.15
# This command I copied it from an issue in stackoverflow so I can use psycopg2
RUN \
 apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev libffi-dev

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt --no-cache-dir 

# This command I copied it from an issue in stackoverflow so I can use psycopg2 
RUN apk --purge del .build-deps

# Copy files to image
COPY . .
RUN chown daemon:daemon -R /app

# RUN adduser -D user
# USER user
RUN addgroup -S appgroup && adduser -S nir -G appgroup
RUN chown nir:appgroup /app/manage.py
RUN chmod +x /app/manage.py
USER nir

CMD python3 manage.py runserver 0.0.0.0:8000
