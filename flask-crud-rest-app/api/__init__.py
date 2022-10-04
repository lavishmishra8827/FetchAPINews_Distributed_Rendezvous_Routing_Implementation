from flask_restful import Api
from app import app
from .Task import Task #find you why you required using .
from .TaskById import TaskById
from .InsertIntoDatabase import InsertIntoDatabase
from .FetchFromDatabase import FetchFromDatabase
restServer=Api(app)
restServer.add_resource(Task,"/api/v1.0/task")
restServer.add_resource(TaskById,"/api/v1.0/TaskById/id/<string:taskId>")
#restServer.add_resource(InsertIntoDatabase,"/InsertIntoDatabase/id/<string:Id>/name/<string:name>")
restServer.add_resource(InsertIntoDatabase,"/InsertIntoDatabase/")
restServer.add_resource(FetchFromDatabase,"/FetchFromDatabase/")