FROM python:3.12-slim
WORKDIR /app
COPY python /app/python
CMD ["python3", "-m", "unittest", "discover", "-s", "python/tests", "-t", "python"]
