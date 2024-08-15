#!/usr/bin/emnv python3
"""Module for Task 0
"""
import redis
import uuid
from typing import Any, Callable, Union


class Cache:
    '''Represents an object for storing data in a Redis data storage.
    '''
    def __init__(self) -> None:
        '''Initializes a Cache instance.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores a value in a Redis data storage and returns the key.
        '''

        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
