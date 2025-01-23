FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

<<<<<<< HEAD
VOLUME /etc/letsencrypt/live/v2736677.hosted-by-vdsina.ru

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-certfile", "/etc/letsencrypt/live/v2736677.hosted-by-vdsina.ru/fullchain.pem", "--ssl-keyfile", "/etc/letsencrypt/live/v2736677.hosted-by-vdsina.ru/privkey.pem"]
=======
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-certfile", "sert.pem", "--ssl-keyfile", "key.pem"]
>>>>>>> 44287f65940c005d5c5d021f9c551bd2a99e726d
