FROM python:3.11
 
WORKDIR /app

COPY . /app

EXPOSE 5001

RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]