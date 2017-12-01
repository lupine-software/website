# encoding: utf-8

from flask_dotenv import DotEnv


class Config(object):  # pylint: disable=no-init
    @classmethod
    def init_app(cls, app, env_name='development'):
        app.config.from_object(CONFIG[env_name])

        env = DotEnv()
        env.init_app(app, verbose_mode=True)


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(Config):
    DEBUG = False
    TEMPLATES_AUTO_RELOAD = False
    STORAGE_BUCKET_HOST = 'localhost'
    STORAGE_BUCKET_NAME = ''
    STORAGE_BUCKET_PATH = '/'


CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
