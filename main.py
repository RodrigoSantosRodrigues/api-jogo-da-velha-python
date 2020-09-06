# -*- coding: utf-8 -*-
# encoding: utf-8
# /run.py
"""
                          Tic-Toc-Tpe API
    ------------------------------------------------------------------------
                         App for production
    ------------------------------------------------------------------------
"""
import os
from dotenv import load_dotenv, find_dotenv

from src.app import create_app

load_dotenv(find_dotenv(filename='.env'))

app = create_app(os.getenv('FLASK_ENV'))
