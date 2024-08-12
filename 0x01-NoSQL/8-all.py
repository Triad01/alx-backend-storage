#!/usr/bin/env python3


def list_all(mongo_collection):
    """
        lists all documents in a collection
    """
    documents = mongo_collection.find()
    if (documents == "null"):
        return []
    else:
        return documents
