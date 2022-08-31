FROM python:3.9

WORKDIR /ScreenshotGen

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

COPY ./drivers/chromedriver_linux64/chromedriver ./drivers/chromedriver_linux64/chromedriver

CMD ["python", "./app/main.py"]