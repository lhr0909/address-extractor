FROM python:3.7.9

# libpostal
ARG COMMIT
ENV COMMIT ${COMMIT:-master}
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /

RUN apt-get update && apt-get install -y \
    autoconf automake build-essential curl git libsnappy-dev libtool pkg-config

RUN git clone https://github.com/openvenues/libpostal -b $COMMIT

COPY ./build_libpostal.sh /libpostal/

WORKDIR /libpostal
RUN ./build_libpostal.sh

# python app
ENV PORT=7000
RUN pip install poetry

COPY . /opt/app

WORKDIR /opt/app
RUN poetry install

RUN make nltk-download
CMD poetry run uvicorn api.main:app --host 0.0.0.0 --port $PORT
