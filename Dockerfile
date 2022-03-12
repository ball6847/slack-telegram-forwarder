FROM python:3.8

WORKDIR /app

ADD requirements.txt /app
RUN pip install -r requirements.txt

ADD main.py /app
RUN chmod a+x /app/main.py
CMD ["python", "-u", "/app/main.py"]
