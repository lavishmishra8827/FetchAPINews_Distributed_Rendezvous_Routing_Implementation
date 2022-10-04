#docker build 
#docker run mysqlinstance


#docker-compose stop



#docker-compose -f stack.yml up
#docker run -p 174.168.1.100:8080:3306 



docker build -t custom_mysql_image .
docker-compose --file docker-compose.yml up

to run the bash terminal for your container
docker exec -it mysqlinstancesetup_custom_mysql_cont_1 bash