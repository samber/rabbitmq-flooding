
FROM python:3.5

ENV PTHONBUFFERED=0

ENTRYPOINT ["python"]

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY producer.py producer.py
COPY consumer.py consumer.py
