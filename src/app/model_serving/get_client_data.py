import os
import logging
from typing import List, Dict, Any
from ..config.redis_connection import RedisClient



def get_predictions(
        model_name: str, 
        client_codes: List[str], 
    ) -> List[Dict[str, Any]]:
    """
    Retrieve predictions from Redis for a list of customer codes and a model name.

    If the list of client codes is empty, fetch all keys from Redis that contain the model name
    and use their suffixes (after the model_name prefix) as client codes.

    Args:
        model_name (str): The name of the model (used as a prefix in Redis keys).
        client_codes (List[str]): List of customer codes to retrieve predictions for. If empty,
                                  fetch all keys matching the model prefix.
        redis_client (redis.StrictRedis): Redis client instance already connected.

    Returns:
        List[Dict[str, Any]]: List of dictionaries mapping full Redis keys to prediction values.
                              Keys with no associated value will be returned with `None`.
                              
    """
    # Redis connection
    host = os.getenv("REDIS_HOST")
    password = os.getenv("REDIS_PASSWORD")

    redis_client = RedisClient(host=host, password=password)
    
    if not client_codes:
        try:
            pattern = f"{model_name}:*"
            keys = redis_client.keys(pattern)
            client_codes_filter = [key.decode().split(":", 1)[1] for key in keys if key.decode().startswith(model_name)]
        except Exception as e:
            logging.error(f"Error fetching keys from Redis with pattern {pattern}: {e}")
            return []
    else:
        client_codes_filter = client_codes

    list_of_predictions = []

    for code in client_codes_filter:
        predictions = {}
        key = f"{model_name}:{code}"
        try:
            value = redis_client.get(key)
            if value is not None:
                predictions[key] = value.decode()  # Assuming value is stored as bytes
            else:
                predictions[key] = None
            list_of_predictions.append(predictions)
        except Exception as e:
            logging.warning(f"Failed to retrieve data for {key} from Redis: {e}")

    return list_of_predictions