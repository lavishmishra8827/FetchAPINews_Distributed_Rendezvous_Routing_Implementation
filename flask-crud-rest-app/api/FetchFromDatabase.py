from flask_restful import Resource
from flask import request
import logging as logger
from .User import User
class FetchFromDatabase(Resource):
    def get(self):
        try:
            logger.debug("inside get method of FetchFromDatabase")
            userobject=User()
            returned_rows=userobject.fetchfromdatabase()
            #return insertion_status
            return returned_rows,200
        except Exception as e:
            return str(e)
    def post(self):
        try:
            userobject=User()
            returning_dict={}
            databasename="testdatabase"
            returning_dict['max_port_no']=userobject.get_max_port_no(databasename,"NodeTopicMapping")
            returning_dict['min_port_no']=userobject.get_min_port_no(databasename,"NodeTopicMapping")
            returning_dict['alltopics']=userobject.listalltopics(databasename,"NodeTopicMapping")
            print('request reaching here')
            userid =request.form['userid']
            #topic=request.form["topic"]
            print(userid)
            print("userid in FetchFromDatabase is ",userid)
            logger.debug("inside post method of FetchFromDatabase")
            
            topic_given=request.form['topic']
            if topic_given=="":
                returning_dict['lst']=[]
                return returning_dict,200

            topic_splitted=topic_given.split('_')
            subscribe_or_unsubscribe=topic_splitted[0]
            if subscribe_or_unsubscribe=='Subscribe' or subscribe_or_unsubscribe=="Unsubscribe":
            
                topic="_".join(topic_splitted[1:])
            else:
                topic=topic_given
            tablename="NodeTopicMapping"
            portno=request.form['portno']
            present_or_not=userobject.check_topic_presence(topic,databasename,tablename,portno)
            print("subscribe_or_unsubscribe is ",subscribe_or_unsubscribe)
            if present_or_not:
                if subscribe_or_unsubscribe=="Subscribe":
                    tablename="SubscribedTopics"
                    result,message=userobject.subscribe_to_topic(userid,topic,databasename,tablename)
                    if not result:
                        return 'Error is '+message,404
                elif subscribe_or_unsubscribe=="Unsubscribe":
                    tablename="SubscribedTopics"
                    print("Unsubscribe called")
                    result,message=userobject.unsubscribe_to_topic(userid,topic,databasename,tablename)
                    if not result:
                        return 'Error is'+message,404
                
                #check here whether topic is present in database
                #userobject=User()
                returning_dict['lst']=userobject.fetchfromdatabase(userid,databasename,topic)
                print("length of returned rows=",len(returning_dict['lst']))
                return returning_dict,200
                
            else:
                returning_dict['lst']='topic not present'
                return returning_dict,404
        except Exception as e:
            print(str(e))
            return str(e),404
    def put(self):
        logger.debug("inside put method of FetchFromDatabase")
        userobject=User(Id,name)
        insertion_status=userobject.insertintodatabase()
        return {"message":"inside put method of FetchFromDatabase. Task-Id={}, Name={}".format(Id,name)},200
    def delete(self):
        logger.debug("inside delete method of FetchFromDatabase")
        userobject=User(Id,name)
        insertion_status=userobject.insertintodatabase()
        return {"message":"inside delete method of FetchFromDatabase. Task-Id={}, Name={}".format(Id,name)},200
