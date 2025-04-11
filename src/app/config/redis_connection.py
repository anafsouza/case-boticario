import os
import redis


class Singleton(type):
    """
    A metaclass for creating Singleton classes.
    Ensures only one instance exists across the application.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class RedisClient(metaclass=Singleton):
    """
    Wrapper class for Redis connection and basic operations.
    """

    def __init__(
        self, host: str = "localhost", 
        password: str = None, 
        port: int = 6379, 
        db: int = 0
    ):
        """
        Initialize the Redis client.

        Args:
            host (str): Redis host address.
            host (str): Redis password.
            port (int): Redis port number.
            db (int): Redis database index.
        """
        self.host = host
        self.password = password
        self.db = db
        self.port = port
        self.redis = redis.StrictRedis(
            host=self.host, 
            password=self.password, 
            port=self.port, 
            db=self.db, 
            decode_responses=True
        )

    def get(self, key: str):
        """
        Get a value from Redis by key.

        Args:
            key (str): Redis key to retrieve.

        Returns:
            str | None: Value from Redis or None if not found.
        """
        return self.redis.get(key)
