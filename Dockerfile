FROM tiangolo/uvicorn-gunicorn-fastapi:latest
EXPOSE 80
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
COPY . /app
# ARG BUILD_ENV=dev
# RUN rm .env && \
#     mv .env.${BUILD_ENV} .env && \
#     apk --update --no-cache add vim less bash curl cmake git gcc musl-dev postgresql-libs postgresql-dev build-base python-dev py-pip jpeg-dev zlib-dev libffi-dev && \
#     python3 -m pip install -r requirements.txt
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser
CMD ["uvicorn","--host","0.0.0.0","--port","80","--workers","4","--no-access-log","--use-colors","--log-level","info" ,"main:app"]