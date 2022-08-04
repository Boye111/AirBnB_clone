#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class User that inherits from BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """ manages public class attributes """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
