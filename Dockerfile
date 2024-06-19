FROM python:3.9

WORKDIR /app

COPY ./src/bot ./src/bot
COPY ./requirements.txt ./requirements.txt
COPY ./main.py ./main.py

RUN pip install -r requirements.txt

EXPOSE 3000

CMD [ "python", "./main.py"]