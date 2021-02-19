FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt

CMD ["python", "AITradingPlatform/manage.py", "createsuperuser"]
