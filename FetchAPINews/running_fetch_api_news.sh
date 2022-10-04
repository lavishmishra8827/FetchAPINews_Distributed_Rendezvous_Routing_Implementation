docker build -t flaskimage .
docker run -lt -p 5000:5000 flaskimage