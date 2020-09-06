# -*- coding: utf-8 -*-
#/src/controller/VelhaController.py
"""
                         Tic-Toc-Toe
    ------------------------------------------------------------------------
                         EndPoints
    ------------------------------------------------------------------------
"""
import uuid
from flask import request, json, Response, Blueprint, session
from ..models.VelhaModel import MovementSchema

velha_api = Blueprint('velha_api', __name__)
movement_schema = MovementSchema()

@velha_api.route('', methods=['POST'])
def create_game():
    """Create session game

    Returns a match id
    """
    try:
        uid = str(uuid.uuid4())
        session[uid] = {'id':uid}
        return custom_response({
            'id': uid,
            'firstPlayer': 'X'
            },
            200
        )
    except Exception as erro:
        print(erro)
        return custom_response({
            'erro': 'Not request'
            },
             400
        )


@velha_api.route('/<string:id>/movement', methods=['POST'])
def play_game(id):
    """movement game

    Returns the result of the current move
    """
    try:
        req_data = request.get_json()
        print(id)
        data_session = session.get(id)
        return custom_response({
            'data': data_session
            },
            200
        )
    except:
        return custom_response({
            'erro': 'Not request'
            },
            400
        )


def custom_response(res, status_code):
    """Custom Response Function

    Responsible for returning requests
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
