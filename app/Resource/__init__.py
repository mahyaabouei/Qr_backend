from flask_restful import Api
from .AddPhone.Add import AddPhoneNumber
api = Api()


api.add_resource(AddPhoneNumber, '/addphone/add')