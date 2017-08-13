#!/usr/bin/python
import logging


class Config(object):
    DEBUG = False
    TESTING = False
    USE_X_SENDFILE = False
    CSRF_ENABLED = True

    SECRET_KEY = "agarywr34^^23gy!"

    DATABASE = {
        'name': 'crontabpy',
        'engine': 'peewee.MySQLDatabase',
        'host': 'localhost',
        'user': 'root',
        'passwd': '123456789',
    }


class Dev(Config):
    DEBUG = True

class Testing(Config):
    TESTING = True
    CSRF_ENABLED = False