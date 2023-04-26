FROM python:3

ENV AWS_ACCESS_KEY_ID=your_access_key_id
ENV AWS_SECRET_ACCESS_KEY=your_secret_access_key

WORKDIR /app

RUN pip install boto3

COPY . .

CMD ["python", "app/index.py"]