import os
import redis


class RedisClient:
    """
    Wrapper class for Redis connection and basic operations.
    """

    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        """
        Initialize the Redis client.

        Args:
            host (str): Redis host address.
            port (int): Redis port number.
            db (int): Redis database index.
        """
        self.redis = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

    def get(self, key: str):
        """
        Get a value from Redis by key.

        Args:
            key (str): Redis key to retrieve.

        Returns:
            str | None: Value from Redis or None if not found.
        """
        return self.redis.get(key)
