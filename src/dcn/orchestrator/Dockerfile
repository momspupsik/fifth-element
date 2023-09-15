FROM alpine:latest
RUN apk update && apk add --no-cache python3 py3-pip
RUN pip install opcua
COPY scripts/dcn.py /.
COPY scripts/process.py /.