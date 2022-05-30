FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /amcefAPI
COPY . /amcefAPI
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000
