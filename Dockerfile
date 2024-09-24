FROM python:3.12.5

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt && \
	python manage.py makemigrations && \
	python manage.py migrate

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
