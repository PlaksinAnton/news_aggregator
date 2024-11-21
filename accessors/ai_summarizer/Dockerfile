FROM python:3.12-slim

WORKDIR /ai_simmarizer

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8084

CMD [ "python3", "app.py" ]