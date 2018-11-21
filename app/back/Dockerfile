FROM python:3-alpine

WORKDIR ./

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir logs

COPY . .

CMD  ["python" , "-u" , "./webservice.py"]
