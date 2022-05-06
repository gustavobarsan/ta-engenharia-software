FROM python:3.10.4-slim

COPY ./src /app/src

COPY requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENV PYTHONPATH="/app/src"

EXPOSE 8000

CMD PYTHON_URLS=http://*:$PORT uvicorn src.app:app
# CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
