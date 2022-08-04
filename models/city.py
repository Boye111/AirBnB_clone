#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
City inherits from basemodel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """ public class attribute state_id and name """
    state_id = ''
    name = ''
