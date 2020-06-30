FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7




ENV settings=prod


COPY . /app
WORKDIR /app
