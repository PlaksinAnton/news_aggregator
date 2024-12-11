FROM python:3.12-slim

WORKDIR /news

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

EXPOSE 8082

# CMD [ "python3", "app.py" ]
CMD ["gunicorn", "-b", "0.0.0.0:8082", "app:app"]