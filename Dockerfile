FROM python:3.7-alpine

ENV PYTHONBUFFERED 1
RUN mkdir /code
COPY . /code/

WORKDIR /code
RUN apk add linux-headers
RUN apk --no-cache --update-cache add bash gcc gfortran python python-dev \ 
    py-pip build-base wget freetype-dev libpng-dev openblas-dev libxml2-dev libxslt-dev
RUN pip install numpy
RUN pip install pandas
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]
