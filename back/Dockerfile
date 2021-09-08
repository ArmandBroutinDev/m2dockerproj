FROM python:3.6-slim

WORKDIR /home/armand/dev/M2/projet/back
COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    vim 
 
RUN pip3 install -r ./requirements.txt

EXPOSE 3305

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3305"]