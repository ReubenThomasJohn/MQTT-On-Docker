FROM python:3.8-slim-buster
WORKDIR /subscriber
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . . 
EXPOSE 81
# CMD ["python3", "-u", "testing.py", "--host=0.0.0.0" ]
CMD python3 -u push_to_influx.py 
#-h 0.0.0.0 -p 80