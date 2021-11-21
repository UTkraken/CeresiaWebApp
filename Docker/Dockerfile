FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /CeresiaWebApp
COPY requirements.txt /CeresiaWebApp
RUN pip install -r requirements.txt
COPY . /ceresia_web_app/

# in ceresia_web_app => docker build ./Docker