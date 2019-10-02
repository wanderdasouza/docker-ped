FROM python:alpine

WORKDIR /usr/hacktoberfest

COPY app.py requirements.txt ./

ENV PORT=8080 \
    HOST=0.0.0.0

EXPOSE ${PORT}

RUN pip install -r requirements.txt

CMD python app.py
