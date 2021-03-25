FROM python:3.6
 
WORKDIR /usr/src/app

COPY main1.py /usr/src/app  
 
ENTRYPOINT ["python", "./main1.py"]
