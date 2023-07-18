#!/usr/bin/env python
'''
return list of school
'''


def schools_by_topic(mongo_collection, topic):
    '''
    return a list
    '''
    topics = {'topics': {'$elemMatch': {'$eq': topic}}}
    return [item for item in mongo_collection.find(topics)]
