FROM python:3.13-slim

RUN pip install \
    fastapi \
    uvicorn[standard]

WORKDIR /app

COPY main.py .

# Порт для FastAPI
EXPOSE 8000

CMD ["python", "main.py"]