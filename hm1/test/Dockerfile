FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    python3-dev \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

FROM python:3.7
EXPOSE 80
EXPOSE 443
ENV PYTHONPATH "${PYTHONPATH}:/test"
COPY . /app
WORKDIR /app 
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

