FROM python:3

COPY requirements.txt /tmp

RUN pip install -U pip && \
    pip install -r /tmp/requirements.txt

COPY data /app/data
COPY namegen.py server.py /app/
WORKDIR /app

CMD [ "python", "./server.py" ]