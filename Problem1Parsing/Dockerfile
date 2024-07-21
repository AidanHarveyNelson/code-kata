FROM python:3.9.19-slim

COPY *.py software/
WORKDIR software

CMD [ "python", "main.py", "--output", "output", "--records", "2000"]
