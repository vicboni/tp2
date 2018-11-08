FROM python:3-alpine

WORKDIR /home/victor/Desktop/MicroServices/tp2/app/front

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD  ["python" , "-u" , "./front.py"]
