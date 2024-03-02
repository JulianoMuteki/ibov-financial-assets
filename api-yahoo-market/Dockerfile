FROM python:3.8
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r /app/requirements.txt

EXPOSE 5001
CMD [ "python", "api-yahoo.py" ]