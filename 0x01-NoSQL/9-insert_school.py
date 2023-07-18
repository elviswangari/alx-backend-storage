#!/usr/bin/env python3
'''
inserting a document
'''


def insert_school(mongo_collection, **kwargs):
    '''
    insert into collection
    '''
    results = mongo_collection.insert_one(kwargs)
    return results.inserted_id
