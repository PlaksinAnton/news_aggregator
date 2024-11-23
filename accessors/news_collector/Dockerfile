FROM python:3.12-slim

WORKDIR /news_collector

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8083

CMD [ "python3", "app.py" ]