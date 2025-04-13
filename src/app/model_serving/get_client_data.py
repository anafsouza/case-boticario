from typing import List, Dict
from ..config.redis_connection import RedisClient


def get_predictions(model_name: str, client_codes: List[str], redis_client: RedisClient) -> Dict[str, dict]:
    """
    Retrieve predictions from Redis for a list of customer codes and model name.

    Args:
        model_name (str): The name of the model (used as prefix in keys).
        client_codes (List[str]): List of customer codes to retrieve predictions for.

    Returns:
        Dict[str, str]: Dictionary mapping code to prediction data (JSON string or similar).
    """
    predictions = {}
    for code in client_codes:
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