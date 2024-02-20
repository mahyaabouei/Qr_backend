from mongoengine import Document , StringField , DateTimeField
from bson import ObjectId

# برای وارد کردن شماره تماس و ذخیره در دیتابیس 

class ModelPhone (Document) :
    mobile = StringField ()
    createad = DateTimeField()


    def __repr__(self):
        return f'ModelPhone({self.mobile})'