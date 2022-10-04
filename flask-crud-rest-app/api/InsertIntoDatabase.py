from flask_restful import Resource
from flask import request,redirect
import logging as logger
from .User import User
class InsertIntoDatabase(Resource):
    def get(self,Id,name):
        logger.debug("inside get method of InsertIntoDatabase")
        userobject=User(Id,name)
        insertion_status=userobject.insertintodatabase()
        #return insertion_status
        return {"message":"inside get method of InsertIntoDatabase. Task-Id={}, Name={}".format(Id,name)},200
    def post(self):
        try:
            if 'Id' not in request.form:
                return 'Id not received'
            Id =request.form['Id']
            if 'name' not in request.form:
                return 'name not received'
            name=request.form['name']
            logger.debug("inside post method of InsertIntoDatabase")
            userobject=User(Id,name)
            insertion_status=userobject.insertintodatabase()
            return redirect("/")
            #return {"message":"inside post method of InsertIntoDatabase. Task-Id={}, Name={}".format(Id,name)},200
        except Exception as e:
            return str(e)
    def put(self,Id,name):
        logger.debug("inside put method of InsertIntoDatabase")
        userobject=User(Id,name)
        insertion_status=userobject.insertintodatabase()
        return {"message":"inside put method of InsertIntoDatabase. Task-Id={}, Name={}".format(Id,name)},200
    def delete(self,Id,name):
        logger.debug("inside delete method of InsertIntoDatabase")
        userobject=User(Id,name)
        insertion_status=userobject.insertintodatabase()
        return {"message":"inside delete method of InsertIntoDatabase. Task-Id={}, Name={}".format(Id,name)},200
