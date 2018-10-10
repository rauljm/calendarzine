

class BaseConfig:
    pass


class DevelopmentConfig:

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/development.db'


class ProductionConfig:

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/production.db'


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
