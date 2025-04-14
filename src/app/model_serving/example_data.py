import uuid
from datetime import datetime

def event_format(data, key):
    data_formatted = {
        "entity": f"{key.split(":")[1]}",
        "data": data,
        "model_name": f"{key.split(":")[0]}",
        "specversion": "1.0.0",
        "datacontenttype": "application/json",
        "id": uuid.uuid4(),
        "eventtype": "ml_model_output",
        "eventdate": datetime.now().isoformat()    
    }
    return data_formatted
    
    
    
    

def final_data(example_data):
    formatted_data = {}
   
    for key in example_data.keys():
        formatted_data[key] = event_format(example_data[key], key)
          
    return formatted_data
    


EXAMPLE_DATA = {
    "model_recommendation:123": {"predict": "product_A", "score": 0.92},   
    "model_recommendation:456": {"predict": "product_A", "score": 0.58},
    "model_recommendation:789": {"predict": "product_B", "score": 0.74},
    "model_recommendation:234": {"predict": None, "score": None},
    "model_recommendation:567": None,
    "model_churn:123": {"predict": 0, "score": 0.18},
#    "model_churn:456": {"predict": 0, "score": 0.18},
    "model_churn:789": {"predict": 1, "score": 0.74},    
}



EXAMPLE_DATA_FORMATTED = final_data(EXAMPLE_DATA)
