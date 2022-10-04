from flask_restful import Resource
import logging as logger
class Task(Resource):
    def get(self):
        logger.debug("Get method executed")
        return {"message":"Inside get method"},200
    def post(self):
        logger.debug("Post method executed")
        return {"message":"Inside post method"},200
    def delete(self):
        logger.debug("Delete method executed")
        return {"message":"Inside delete method"},200
    def put(self):
        logger.debug("Put method executed")
        return {"message":"Inside put method"},200
