#!/usr/bin/env python
'''
return list of school
'''


def schools_by_topic(mongo_collection, topic):
    '''
    return a list
    '''
    topic = {'topic': {'$selectMatch': {'$eq': topic}}}
    return [item for item in mongo_collection.find(topic)]
