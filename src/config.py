# -*- coding: utf-8 -*-
# /src/config.py
"""
                              Config
    ------------------------------------------------------------------------
                        Flask Environment Configuration
    ------------------------------------------------------------------------
"""
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(filename="/.env"))

class Development():
    """Development environment configuration"""
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')

class Production():
    """Production environment configurations"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')

class Testing():
    """Testing environment configuration"""
    TESTING = True
    SECRET_KEY = os.getenv('SECRET_KEY')

app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}

app_host = {
    'host': os.getenv('APP_HOST').join(':').join(os.getenv('APP_PORT'))
}
