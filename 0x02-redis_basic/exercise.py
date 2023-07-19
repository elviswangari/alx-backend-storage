#!/usr/bin/env python3
'''
basics of redis
'''
from typing import Callable, Optional, Union
from uuid import uuid4
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''
    returns a callable
    '''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''decorated function wrapper'''
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


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

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        generates random key
        '''
        keys = str(uuid4())
        self._redis.set(keys, data)
        return keys

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''
        convert to desired format
        '''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        '''
        parametize Cache.get with correct format
        '''
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        '''
        parametize Cache.get with correct format
        '''
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
