from mongoengine import connect

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your_secret_key'
    DBNAME = 'QR'
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost:27017/'+DBNAME,
    }
    HOST = '0.0.0.0'
    PORT = 8080

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    HOST = '0.0.0.0'



config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

connect(host=Config.MONGODB_SETTINGS['host'])