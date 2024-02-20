from flask_restful  import Resource , reqparse , abort
from app.Model.AddPhone import ModelPhone
import datetime 

"""
را اسکن میکنند  شماره تماس باید وارد کنندqr code وقتی 
با وارد کردن شماره تماس از سمت کاربر
 شماره تماس در دیتابیس ذخیره میشود 
"""

parser = reqparse.RequestParser ()
parser.add_argument ('mobile', type = str , help = 'شماره همراه را وارد کنید' , required  =True)


# شماره تماس را گرفته و همراه با  تاریخ در دیتابیس ذخیره میکند 

class AddPhoneNumber (Resource) :
    def post (self) :
        args = parser.parse_args ()
        mobile = ModelPhone (
            mobile = args ['mobile'],
            createad = datetime.datetime.now(),

            )
        mobile.save ()
        return True


        
