from python:3-alpine
RUN pip install --upgrade pip
WORKDIR /FetchAPINews
COPY . /FetchAPINews
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["fetch_and_store.py"]