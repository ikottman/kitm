FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/app

COPY kitm.py .

ENTRYPOINT [ "/usr/local/bin/python", "kitm.py"]