#!/usr/bin/env python3
"""Module 9 task
"""


def insert_school(mongo_collection, **kwargs):
    """nserts a new document in a collection based on kwargs
    """
    obj = mongo_collection.insert_one(kwargs)
    return obj.inserted_id
