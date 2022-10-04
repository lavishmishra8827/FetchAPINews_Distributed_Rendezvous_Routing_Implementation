import mysql.connector
import logging as logger
class User:
    def __init__(self,*args):
        if len(args)==2:
            self.__id__=args[0]
            self.__name__=args[1]
    def printdata(self):
        print("Id="+self.__id__+"Name="+self.__name__)
    def make_connection(self):
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
    '''
    def insertintodatabase(self):
        try:
            mycursor,db=self.make_connection()
        except Exception as e:
            return 'Error in making database connection :'+str(e)
        
        try:
            mycursor.execute("Insert into "+database+".INFO values ('"+self.__id__+"','"+self.__name__+"');")
            db.commit()
            print("Inserted")
            db.close()
            return 1
        except Exception as e:
            print("Error received is ",str(e))
            db.rollback()
            db.close()
            return 0
    def fetchfromdatabase(self):
        try:
            mycursor,db=self.make_connection()
        except Exception as e:
            return 'Error in making database connection :'+str(e)
        try:
            mycursor.execute("Select * from "+database+".INFO;")
            rows=mycursor.fetchall()
            logger.debug(str(rows))
            #print("Inserted")
            db.close()
            return rows
        except Exception as e:
            print("Error received is ",str(e))
            db.rollback()
            db.close()
            return 0
    '''
    def get_max_port_no(self,database,tablename):
        try:
            mycursor,db=self.make_connection()
        except Exception as e:
            return 'Error in making database connection :'+str(e)
        try:
            #Node1 is hardcoded for now, find a way to get it
            query="select max(Portno) from "+database+"."+tablename+";"
            print(query)
            mycursor.execute(query)
            rows=mycursor.fetchall()
            topics_stored=list(rows)
            max_port=topics_stored[0][0]
            return max_port
        except Exception as e:
            print("Error received is ",str(e))
            db.rollback()
            db.close()
            return 5000
    def get_min_port_no(self,database,tablename):
        try:
            mycursor,db=self.make_connection()
        except Exception as e:
            return 'Error in making database connection :'+str(e)
        try:
            #Node1 is hardcoded for now, find a way to get it
            query="select min(Portno) from "+database+"."+tablename+";"
            print(query)
            mycursor.execute(query)
            rows=mycursor.fetchall()
            topics_stored=list(rows)
            min_port=topics_stored[0][0]
            return min_port
        except Exception as e:
            print("Error received is ",str(e))
            db.rollback()
            db.close()
            return 5000
    def listalltopics(self,database,tablename):
        try:
            mycursor,db=self.make_connection()
        except Exception as e:
            return 'Error in making database connection :'+str(e)
        try:
            #Node1 is hardcoded for now, find a way to get it
            query="select Topic from "+database+"."+tablename+";"
            print(query)
            mycursor.execute(query)
            rows=mycursor.fetchall()
            topics_stored=list(rows)
            print("topics list we got is \n")
            print(topics_stored)
            db.close()
            return topics_stored
        except Exception as e:
            print("Error received is ",str(e))
            db.rollback()
            db.close()
            return []
        
    def check_topic_presence(self,topic,database,tablename,portno):
        try:
            mycursor,db=self.make_connection()
        except Exception as e:
            return 'Error in making database connection :'+str(e)
        try:
            #Node1 is hardcoded for now, find a way to get it
            query="select Topic from "+database+"."+tablename+" where Portno="+portno+";"
            print(query)
            mycursor.execute(query)
            rows=mycursor.fetchall()
            topics_stored=list(rows)
            print("topics list we got is \n")
            print(topics_stored)
            db.close()
            found=0
            for i in topics_stored:
                if topic==i[0]:
                    found=1
                    break
            
            if found==1:
                return True
            else:
                return False
        except Exception as e:
            print("Error received is ",str(e))
            db.rollback()
            db.close()
            return False
            
    def isSubscribed(self,userid,topic,databasename,tablename):
        try:
            mycursor,db=self.make_connection()
        except Exception as e:
            return 'Error in making database connection :'+str(e)
        try:
            #Node1 is hardcoded for now, find a way to get it
            query="select * from "+databasename+"."+tablename+" where UserId='"+userid+"' and Topic='"+topic+"';"
            mycursor.execute(query)
            rows=mycursor.fetchall()
            if len(rows)>=1:
                return True
            return False
        except Exception as e:
            print('Error is ',e)
            return False
    def subscribe_to_topic(self,userid,topic,databasename,tablename):
        if self.isSubscribed(userid,topic,databasename,tablename):
            return True,'Success'
        else:
            try:
                mycursor,db=self.make_connection()
            except Exception as e:
                return 'Error in making database connection :'+str(e)
            try:
                #Node1 is hardcoded for now, find a way to get it
                #query="select * from "+databasename+"."+tablename+" where UserId='"+userid+"' and Topic='"+topic+"';"
                query="Insert into "+databasename+"."+tablename+" values('"+userid+"','"+topic+"')";
                mycursor.execute(query)
                
                db.commit()
                db.close()
                return True,'Success'
                
            except Exception as e:
                db.rollback()
                db.close()
                print('Error is ',e)
                return False
    def unsubscribe_to_topic(self,userid,topic,databasename,tablename):
        if not self.isSubscribed(userid,topic,databasename,tablename):
            return True,'Success'
        else:
            try:
                mycursor,db=self.make_connection()
            except Exception as e:
                return 'Error in making database connection :'+str(e)
            try:
                #Node1 is hardcoded for now, find a way to get it
                #query="select * from "+databasename+"."+tablename+" where UserId='"+userid+"' and Topic='"+topic+"';"
                query="delete from "+databasename+"."+tablename+" where UserId='"+userid+"' and Topic='"+topic+"';"
                print('query for unsubscribe_to_topic is ',query)
                mycursor.execute(query)
                db.commit()
                db.close()
                print('row should have been deleted now')
                return True,'Success'
                
            except Exception as e:
                db.rollback()
                db.close()
                print('Error is ',e)
                return False
            
    def fetchfromdatabase(self,userid,database,tablename):
        if self.isSubscribed(userid,tablename,database,"SubscribedTopics"):
        
            try:
                mycursor,db=self.make_connection()
            except Exception as e:
                return 'Error in making database connection :'+str(e)
            try:
                '''
                mycursor.execute("select rowdisplayed from "+database+".requested where ID='"+userid+"';")
                rowDisplayStart=mycursor.fetchall()[0][0]
                mycursor.execute("select max(rowvalue) from "+database+"."+tablename+"")
                maxrowvalue=mycursor.fetchall()[0][0]
                print(maxrowvalue)
                #rowDisplayStart=62
                print(rowDisplayStart,type(rowDisplayStart))
                value1=rowDisplayStart
                value2=rowDisplayStart+1
                value3=rowDisplayStart+2
                if value1>maxrowvalue:
                    value1-=maxrowvalue
                if value2>maxrowvalue:
                    value2-=maxrowvalue
                if value3>maxrowvalue:
                    value3-=maxrowvalue
                fetch3Feeds="select Title,Author,Description,URL,URLToImage,Content from "+database+"."+tablename+" where rowvalue in ("+str(value1)+","+str(value2)+","+str(value3)+");"
                mycursor.execute(fetch3Feeds)
                rows=mycursor.fetchall()
                '''
                #print(rows)
                #logger.debug(str(rows))
                query="select Title,Author,Description,URL,URLToImage,Content from "+database+"."+tablename
                '''
                if topic!='AllFeeds':
                    query+=" where Topic='"+topic+"'"
                '''
                query+=" order by RAND() LIMIT 3"
                print(query)
                mycursor.execute(query)
                rows=mycursor.fetchall()
                db.close()
                '''
                result=self.updatedatabase(userid,database,tablename)
                if result!=1:
                    print("couldn't update database, still returning values")
                '''
                return rows
            except Exception as e:
                print("Error received is ",str(e))
                db.rollback()
                db.close()
                return 0,404
        else:
            return []
    '''
    def updatedatabase(self,userid,database,tablename):
        try:
            mycursor,db=self.make_connection()
        except Exception as e:
            return 'Error in making database connection :'+str(e)
        try:
            mycursor.execute("select rowdisplayed from "+database+".requested where ID='"+userid+"';")
            rowDisplayStart=mycursor.fetchall()[0][0]
            updateRowDisplay="update "+database+".requested set rowdisplayed="+str(rowDisplayStart+3)+" where ID='"+userid+"';"
            print(updateRowDisplay)
            mycursor.execute(updateRowDisplay)
            db.commit()
            print(rowDisplayStart+3,'updated')
            #logger.debug(str(rows))
            #print("Inserted")
            db.close()
            return 1
        except Exception as e:
            print("Error received is ",str(e))
            #logger.log("Error received is "+str(e))
            db.rollback()
            db.close()
            return 0
    '''
