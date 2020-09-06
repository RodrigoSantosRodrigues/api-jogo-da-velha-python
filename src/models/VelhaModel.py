# -*- coding: utf-8 -*-
# src/models/VelhaModel.py
"""
                        Tic-Toc-Toe
    ------------------------------------------------------------------------
                           Model
    ------------------------------------------------------------------------
"""
from marshmallow import fields, Schema

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
