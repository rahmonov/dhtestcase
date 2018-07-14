FROM python:3.6

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:ubuntugis/ppa
RUN apt-get update; exit 0
RUN apt-get install -y python3-dev gdal-bin

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app
WORKDIR /app

ENV PYTHONUNBUFFERED 1
EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
