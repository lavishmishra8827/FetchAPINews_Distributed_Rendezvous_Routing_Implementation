from flask_restful import Resource
import logging as logger
class TaskById(Resource):
	def get(self,taskId):
		logger.debug("inside get method of Taskbyid")
		return {"message":"inside get method of Taskbyid. Task-Id={}".format(taskId)},200
	def post(self,taskId):
		logger.debug("inside post method of Taskbyid")
		return {"message":"inside post method of Taskbyid. Task-Id={}".format(taskId)},200
	def put(self,taskId):
		logger.debug("inside put method of Taskbyid")
		return {"message":"inside put method of Taskbyid. Task-Id={}".format(taskId)},200
	def delete(self,taskId):
		logger.debug("inside delete method of Taskbyid")
		return {"message":"inside delete method of Taskbyid. Task-Id={}".format(taskId)},200
