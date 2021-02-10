FROM python:3.8.6-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .
ENV FLASK_APP=api.py

RUN chmod 0777 -R /app

ENTRYPOINT [ "flask" ]
CMD [ "run", "--host", "0.0.0.0" ]
