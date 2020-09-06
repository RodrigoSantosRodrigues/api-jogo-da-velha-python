# -*- coding: utf-8 -*-
# src/app.py
"""
                           API
    ------------------------------------------------------------------------
                        Create app
    ------------------------------------------------------------------------
"""
from flask import Flask, Response
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from .config import app_config
from .controllers.VelhaController import velha_api as velha_blueprint


def create_app(env_name):
    """
        param: env_name

        DOC API USING SWAGGER UI
        Create app
    """
    # app initiliazation
    app = Flask(__name__)
    #CORS(app, resources={r"/api/*": {"origins": "*"}})
    CORS(app)

    app.config.from_object(app_config[env_name])

    ### swagger specific ###
    swagger_url = '/apidocs'
    api_url = '/static/api/api.yml'
    swagger_blueprint = get_swaggerui_blueprint(
        swagger_url,
        api_url,
        config={
            'app_name': "API Jogo da Velha",
            'layout': "BaseLayout",
            'filter': True
        }
    )
    app.register_blueprint(swagger_blueprint, url_prefix=swagger_url)
    ### end swagger specific ###

    app.register_blueprint(velha_blueprint, url_prefix='/v1/api/game')

    @app.route('/', methods=['GET'])
    def index():
        """
        Home
        """
        return Response(
        mimetype="application/json",
        response={"Bem vindo ao Jogo da Velha - Documentação: /apidocs"},
        status=200
        )

    return app
  