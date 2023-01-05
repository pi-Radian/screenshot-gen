#!/usr/bin/env -S docker build . --tag=dude/man:v2 --network=host --file

FROM python:3.9

WORKDIR /ScreenshotGen

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

#COPY ./drivers/chromedriver_linux64/chromedriver ./drivers/chromedriver_linux64/chromedriver
COPY ./drivers/install_chrome.sh ./drivers/install_chrome.sh
RUN sh ./drivers/install_chrome.sh

RUN mkdir ./tmp

CMD ["nohup", "python", "./app/main.py", "&"]




#docker build -t screenshot-gen .
#docker images
#
#docker run -p 8000:8000 screenshot-gen
#docker ps
#docker exec -it eb3e0b92df1b /bin/sh
