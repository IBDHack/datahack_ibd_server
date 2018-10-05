FROM python:3.6

ADD . .

RUN pip install -r requirements.txt

# Main Command
ENTRYPOINT python server.py

