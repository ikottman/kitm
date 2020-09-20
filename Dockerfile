FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/app

COPY kitm.py .
ENV PORT 9999
ENTRYPOINT [ "/usr/local/bin/python", "kitm.py"]