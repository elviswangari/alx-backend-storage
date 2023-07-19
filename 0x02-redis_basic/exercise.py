#!/usr/bin/env python3
'''
basics of redis
'''
from typing import Union
from uuid import uuid4
import redis


class Cache:
    '''
    class for cache defination in
    redis
    '''
    def __init__(self):
        '''
        instantiate redis
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        generates random key
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key
