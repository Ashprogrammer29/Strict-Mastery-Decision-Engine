FROM python:3.11-alpine
RUN adduser -D master_user
USER master_user
WORKDIR /app
COPY mastery_engine.py .
ENTRYPOINT ["python", "mastery_engine.py"]