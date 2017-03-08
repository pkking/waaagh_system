# db configs
db_name = "blog"
db_test_name = "test_blog"
db_user = "blog"
db_password = "blog"
db_host = "127.0.0.1"
db_driver = "psycopg2"
db_type = "postgresql"

class Config(object):
    INFO_LOG = "info.log"
    ERROR_LOG = "error.log"
    DEBUG = False
    SECRET_KEY = 'pkking123456'
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}/{}".format(
    db_type, db_driver, db_user, db_password, db_host, db_name)

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    #DEBUG = True
    INFO_LOG = "info-testing.log"
    ERROR_LOG = "error-testing.log"
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}/{}".format(
    db_type, db_driver, db_user, db_password, db_host, db_test_name)

