import requests
import mysql.connector
def make_connection():
        '''
        host="localhost"
        user="user1"
        passwd="user1root"
        db=mysql.connector.connect(host=host,user=user,passwd=passwd,auth_plugin='mysql_native_password')
        '''
        host="host.docker.internal"
        user="root"
        passwd="examplepassword"
        port=8080
        db=mysql.connector.connect(host=host,user=user,passwd=passwd,port=port,auth_plugin='mysql_native_password')
        mycursor=db.cursor()
        return mycursor,db
def insertintodatabase(databasename,tablename,row_to_insert):
        print("executing function")
        try:
            mycursor,db=make_connection()
        except Exception as e:
            return 'Error in making database connection :'+str(e)
        print('connection made')
        try:
            #we need to complete this now
            query="Insert Into "+databasename+"."+tablename
            #+" ("
            '''
            for key in row_to_insert.keys():
                if key==None:
                    query+="null,"
                else:
                    query+="'"+key.replace("\n","").replace("\t"," ").replace("'","\"")+"',"
                #print(query)
            query=query[:-1]
            '''
            query+=" values("
            for value in row_to_insert.values():
                if value==None:
                    query+="null,"
                else:
                    query+="'"+value.replace("\n","").replace("\t"," ").replace("'","\"")+"',"
                #print(query)
            query=query[:-1]
            query+=");"
            print(query)
            #mycursor.execute("Insert into "+databasename+"."+tablename+" values ('"+self.__id__+"','"+self.__name__+"');")
            mycursor.execute(query)
            db.commit()
            print("Inserted")
            db.close()
            return 1
        except Exception as e:
            print("Error received is ",str(e))
            db.rollback()
            db.close()
            return 0
''' 
response=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=dd6d6d5889c84fbc9c2d5d1eaddcc065")
topic="technology"


response=requests.get("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=7a11f7c147d64d7ba4da33b553c06ca0")
topic="apple"
'''
response=requests.get("https://newsapi.org/v2/everything?q=apple&from=2021-10-22&to=2021-10-22&sortBy=popularity&apiKey=7a11f7c147d64d7ba4da33b553c06ca0")
topic="techcrunch"

techNewsData=response.json()
#print(techNewsData)
#for key in techNewsData.keys():
    #print(key)
databasename="testdatabase"
tablename="TECHNEWS"

articles=techNewsData["articles"]
row_dict={}
for article in articles:

    row_dict['rowvalue']=None
    row_dict['SourceID']=article['source']['id']
    row_dict['SourceName']=article['source']['name']
    row_dict['Author']=article['author']
    row_dict['Title']=article['title']
    row_dict['Description']=article['description']
    row_dict['URL']=article['url']
    row_dict['URLToImage']=article['urlToImage']
    row_dict['PublishedAt']=article['publishedAt']
    row_dict['Content']=article['content']
    
    if (row_dict['SourceID']==None):
        row_dict['SourceID']="null"
    if (row_dict['SourceName']==None):
        row_dict['SourceName']="null"
    if (row_dict['Author']==None):
        row_dict['Author']="null"
    if (row_dict['Title']==None):
        row_dict['Title']="null"
    if (row_dict['Description']==None):
        row_dict['Description']="null"
    if (row_dict['URL']==None):
        row_dict['URL']="null"
    if (row_dict['URLToImage']==None):
        row_dict['URLToImage']="null"
    if (row_dict['PublishedAt']==None):
        row_dict['PublishedAt']="null"
    if (row_dict['Content']==None):
        row_dict['Content']="null"
    row_dict['Topic']=topic

    print(insertintodatabase(databasename,tablename,row_dict))

