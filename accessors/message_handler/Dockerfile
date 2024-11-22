FROM python:3.12-slim

WORKDIR /message_handler

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8085

CMD [ "python3", "app.py" ]