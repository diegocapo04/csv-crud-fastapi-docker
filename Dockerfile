FROM python:3.11.13

WORKDIR /app

COPY main.py .
COPY api_operations.py .
COPY csv_operations.py .
COPY csv_files/file.csv .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","main:app","--host","127.0.0.1","--port","8000"]