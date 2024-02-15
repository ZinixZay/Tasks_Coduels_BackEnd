FROM python:latest
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --user -r requirements.txt
COPY . /code/
EXPOSE 8000
CMD python tycoon/manage.py runserver 0.0.0.0:8000