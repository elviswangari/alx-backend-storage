#!/usr/bin/env python3
'''
return list of school
'''


def schools_by_topic(mongo_collection, topic):
    '''
    return a list
    '''
    topics = {'topics': {'$eq': topic}}
    return [item for item in mongo_collection.find(topics)]
