FROM python:3

WORKDIR /app

# copia tudo para o container
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]
