FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

ARG SECRET_KEY
ENV SECRET_KEY=${SECRET_KEY}
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
