FROM python:3.12-slim

WORKDIR /db_accessor

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8082

CMD [ "python3", "app.py" ]