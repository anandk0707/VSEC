FROM python:3.10-slim

WORKDIR /app

COPY model/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY model/ .

EXPOSE 8000

CMD ["python", "app.py"]
