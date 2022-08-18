FROM us-west1-docker.pkg.dev/kameds-f228e/test-repo/ss-core:develop

COPY ./app/ /app
RUN echo "nameserver 8.8.8.8" >> /etc/resolv.conf
RUN pip install -r requirements.txt --no-cache-dir


CMD ["python3", "run.py"]