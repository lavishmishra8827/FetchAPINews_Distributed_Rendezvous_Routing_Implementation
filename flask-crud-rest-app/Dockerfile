from python:3-alpine
ENV port=5000
RUN pip install --upgrade pip
WORKDIR /flask-crud-rest-app
COPY . /flask-crud-rest-app
RUN pip install -r requirements.txt
EXPOSE ${port}
EXPOSE 8080
ENTRYPOINT ["python3"]
CMD ["app.py"]