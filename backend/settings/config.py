import os 


class Environment(object):
    """ Principal configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')



class DevelopEnvironment(Environment):
    """ Environment Develop configuration class. """
    DEBUG = True


class ProductionEnvironment(Environment):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False



app_config = {
    'development': DevelopEnvironment,
    'production': ProductionEnvironment
}