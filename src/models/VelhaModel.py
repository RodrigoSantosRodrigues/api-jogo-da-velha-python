# -*- coding: utf-8 -*-
# src/models/VelhaModel.py
"""
                        Tic-Toc-Toe
    ------------------------------------------------------------------------
                           Model
    ------------------------------------------------------------------------
"""
from flask import session
from marshmallow import fields, Schema

class VelhaModel:
    """Schema for coord

    Schema definition for validation and serialization
    """
    def __init__(self, data):
        """
        Class constructor
        """
        self.id= data.get('id')
        self.round_player= data.get('round_player')
        self.matrix= data.get('matrix')
        self.round_game= data.get('round_game')

    def save(self):
        """save
        """
        session[self.id] = {
            'id': self.id,
            'round_player': self.round_player,
            'matrix': self.matrix,
            'round_game': self.round_game
        }

    def update(self):
        """update
        """
        session[self.id] = {
            'id': self.id,
            'round_player': self.round_player,
            'matrix': self.matrix,
            'round_game': self.round_game
        }

    @staticmethod
    def get_macth(id):
        return session.get(id)

class CoordSchema(Schema):
    """Schema for coord

    Schema definition for validation and serialization
    """
    x = fields.Int(required = True)
    y = fields.Int(required = True)

class MovementSchema(Schema):
    """Schema for movement

    Schema definition for validation and serialization
    """
    id = fields.UUID(required = True)
    player = fields.Str(required = True)
    position = fields.Nested(CoordSchema, required = True)
