FROM us-west1-docker.pkg.dev/kameds-f228e/test-repo/ss-core:develop

COPY ./app/ /app
RUN pip install -r requirements.txt --no-cache-dir

CMD ["python3", "run.py"]