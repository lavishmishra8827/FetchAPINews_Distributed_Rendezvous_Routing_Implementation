docker build -t flaskimage "flask-crud-rest-app\\"
docker run -lt -p 5000:5000 -e port=5000 flaskimage 
docker run -lt -p 5001:5001 -e port=5001 flaskimage 
docker run -lt -p 5002:5002 -e port=5002 flaskimage 

docker build -t fetchnewsapi "FetchAPINews\\"
docker run -lt  fetchnewsapi


docker build -t custom_mysql_image "MYSQL instance setup\\"
docker-compose --file "MYSQL instance setup\\docker-compose.yml" up
docker exec -it mysqlinstancesetup_custom_mysql_cont_1 bash
docker stop id
docker restart id

