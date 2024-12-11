FROM python:3.12-slim

WORKDIR /ai_simmarizer

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

EXPOSE 8084

# CMD [ "python3", "app.py" ]
CMD ["gunicorn", "-b", "0.0.0.0:8084", "app:app"]