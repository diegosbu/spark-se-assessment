import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'sqlite:///'
database_name = 'diagnostic'

class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'diagnostic_secret123')
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = 'postgres://sdwmnaccpuamvo:d135e73ecacbdb9e4ef11a1930e9dcb859d73f4a2893b3894853d9498664e705@ec2-34-205-209-14.compute-1.amazonaws.com:5432/datclj7ukgcuv6'


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'diagnostic_secret'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://sdwmnaccpuamvo:d135e73ecacbdb9e4ef11a1930e9dcb859d73f4a2893b3894853d9498664e705@ec2-34-205-209-14.compute-1.amazonaws.com:5432/datclj7ukgcuv6'