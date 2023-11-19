FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN python manage.py makemigrations
# RUN python manage.py migrate

EXPOSE 3000

CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]
