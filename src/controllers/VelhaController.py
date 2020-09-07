# -*- coding: utf-8 -*-
#/src/controller/VelhaController.py
"""
                         Tic-Toc-Toe
    ------------------------------------------------------------------------
                         EndPoints
    ------------------------------------------------------------------------
"""
import uuid
from flask import request, json, Response, Blueprint
from ..models.VelhaModel import VelhaModel, MovementSchema
from ..helpers.Game import Game

velha_api = Blueprint('velha_api', __name__)
movement_schema = MovementSchema()

@velha_api.route('', methods=['POST'])
def create_game():
    """Create session game

    Returns a match id
    """
    try:
        uid = str(uuid.uuid4())
        game = Game()
        post = VelhaModel({
            'id':uid,
            'round_player': game.player,
            'matrix': game.matrix,
            'round_game': game.round_game
            }
        )
        post.save()
        return custom_response({
            'id': uid,
            'firstPlayer': game.player
            },
            201
        )
    except Exception as exc:
        return custom_response({
            'error':'Exception: {}'.format(exc)
            },
            500
        )


@velha_api.route('/<string:id>/movement', methods=['POST'])
def play_game(id):
    """movement game

    Returns the result of the current move
    """
    try:
        req_data = request.get_json()
        movement_schema.load(req_data)

        if req_data.get('id') != id:
            return custom_response({
                'msg': "Id da url é diferente do id do payload"
                },
                400
            )
        
        player_session = VelhaModel.get_macth(id)
        if not player_session:
            return custom_response({
                'msg': "Partida não encontrada"
                },
                400
            )

        if req_data.get('player') != player_session.get('round_player'):
            return custom_response({
                'msg': "Não é turno do jogador"
                },
                400
            )
        
        game = Game(player_session.get('matrix'), player_session.get('round_game'), player_session.get('round_player'))
        played = game.set_movement(req_data['position'].get('x'), req_data['position'].get('y'))
        if not played:
            return custom_response({
                'msg': "Jogada inválida"
                },
                400
            )
        post = VelhaModel({
            'id': id,
            'round_player': game.player,
            'matrix': game.matrix,
            'round_game': game.round_game
            }
        )
        post.update()

        end_game = game.check_game_over()
        if end_game:
            return custom_response({
                'status': 'Partida finalizada',
                'winner': end_game
                },
                200
            )

        data = VelhaModel.get_macth(id)

        return custom_response({
            'data': data,
            'msg': 'Jogada feita com sucesso'
            },
            200
        )
    except Exception as exc:
        return custom_response({
            'error':'Exception: {}'.format(exc)
            },
            500
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
