FROM python:3.8-slim-buster

WORKDIR /home/app
COPY requeriments.txt .
COPY api.py .
EXPOSE 8000
RUN pip install -r requeriments.txt
CMD [ "uvicorn", "api:app", "--host", "0.0.0.0"]