FROM python:3.12-slim

WORKDIR /news_collector

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

EXPOSE 8083

# CMD [ "python3", "app.py" ]
CMD ["gunicorn", "-b", "0.0.0.0:8083", "app:app"]