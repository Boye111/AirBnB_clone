#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
class Review that inherits from basemodel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ public classattributes of place, user and text """
    place_id = ''
    user_id = ''
    text = ''
