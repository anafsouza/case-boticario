from typing import List, Dict
from ..config.redis_connection import RedisClient


def get_predictions(model_name: str, client_codes: List[str], redis_client: RedisClient) -> Dict[str, dict]:
    """
    Retrieve predictions from Redis for a list of customer codes and model name.

    Args:
        model_name (str): The name of the model (used as prefix in keys).
        codes (List[str]): List of customer codes.
        redis_client (RedisClient): Redis client instance.

    Returns:
        Dict[str, str]: Dictionary mapping code to prediction data (JSON string or similar).
    """
    predictions = {}
    for code in client_codes:
        key = f"{model_name}:{code}"
        value = redis_client.get(key)
        if value is not None:
            predictions[code] = value
        else:
            predictions[code] = None  # or "not found" if you prefer
    return predictions
