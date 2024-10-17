# pull the official docker image
FROM python:3.11.1-slim

# set work directory
WORKDIR /app

# set env variables
COPY ./requirements.txt /app/requirements.txt

# install dependencies
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install -y netcat \
    && apt-get clean

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip
# copy project
COPY . /app/

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0","--port", "8000"]