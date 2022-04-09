FROM python:3.8
WORKDIR /code
COPY requirement.txt ./

RUN pip install --no-cache-dir -r requirement.txt

COPY . .