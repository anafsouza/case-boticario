# Model Store

**Model Store** is a lightweight FastAPI-based service that centralizes access to **batch prediction results** from multiple machine learning models.

Each model's predictions are stored in **Redis**, indexed by a unique combination of `model_name` and a `uuid` representing the prediction instance. The API exposes a unified interface where clients can retrieve prediction outputs for any model without needing to know how or where the prediction was generated.

This makes it ideal for systems where:

* Model inference is done asynchronously or in batch,
* Prediction results are cached,
* Multiple teams or systems need consistent access to those results.

---

## 🚀 What This Project Does

* Acts as a **read-only interface** to Redis-stored prediction results from multiple models
* Provides a **single endpoint** to retrieve any prediction using the model name and an ID
* Simplifies access to ML outputs for downstream applications, dashboards, or services
* Improves decoupling: the prediction logic and retrieval logic live independently
* Enables scaling and standardization across multiple ML pipelines


---

## 📬 Example API Request with JSON Body

The API exposes a POST endpoint to fetch batch predictions for multiple entities by specifying the model name and a list of codes (UUIDs or identifiers).

### 🔹 Endpoint

```
POST /predict
```

### 🔹 Request Body Example

```json
{
  "model_name": "model_recommendation",
  "codes": [
    "123",
    "456",
    "789"
  ]
}
```

> **Note:** The `codes` list represents the UUIDs or unique identifiers of the prediction instances you want to retrieve.

### 🔹 Example Request Using `curl`

```bash
curl -X POST "http://localhost:5000/predict" \
     -H "Content-Type: application/json" \
     -d '{
           "model_name": "model_recommendation",
           "codes": ["123", "456", "789"]
         }'
```

### 🔹 Sample Response

```json
{
  "predictions": [
    {
      "model_recommendation:123": {
        "entity": "123",
        "data": {
          "predict": "product_A",
          "score": 0.92
        },
        "model_name": "model_recommendation",
        "specversion": "1.0.0",
        "datacontenttype": "application/json",
        "id": "8f06d725-d9f8-4c5d-80b7-d332cbd1ea60",
        "eventtype": "ml_model_output",
        "eventdate": "2025-06-17T11:37:02.880108"
      }
    },
    {
      "model_recommendation:456": {
        "entity": "456",
        "data": {
          "predict": "product_A",
          "score": 0.58
        },
        "model_name": "model_recommendation",
        "specversion": "1.0.0",
        "datacontenttype": "application/json",
        "id": "65a90fc1-15fe-42b3-9bbf-e6dd365f6228",
        "eventtype": "ml_model_output",
        "eventdate": "2025-06-17T11:37:02.880130"
      }
    },
    {
      "model_recommendation:789": {
        "entity": "789",
        "data": {
          "predict": "product_B",
          "score": 0.74
        },
        "model_name": "model_recommendation",
        "specversion": "1.0.0",
        "datacontenttype": "application/json",
        "id": "c4e3a1cf-f1e2-44e0-bbf0-e64361409fd8",
        "eventtype": "ml_model_output",
        "eventdate": "2025-06-17T11:37:02.880136"
      }
    }
  ]
}
```

---

## ✨ Key Features

* ✅ **Modular code structure** for easy maintenance and scaling
* 🧠 **Redis integration** for background tasks or fast caching
* ❤️ **Health check endpoints** for uptime monitoring
* 📚 **Swagger UI** auto-generated from FastAPI
* 🧪 **Testing suite** using `pytest`
* 📦 **Docker-ready** for smooth containerization
* 🔁 **CI/CD automation** via Azure Pipelines

---

## 🗂️ Project Structure

```bash
model-store/
├── src/
│   └── app/
│       ├── config/           # Redis setup and health check config
│       ├── model_serving/    # Logic for model handling and services
│       ├── schemas/          # Request/response validation with Pydantic
│       ├── api_main.py       # Main FastAPI app instance
│       └── api.py            # Optional routing/controller logic
├── tests/                    # Unit tests
├── requirements.txt          # Dependencies
├── azure-pipelines.yml       # CI pipeline config
├── Dockerfile                # Container image definition
├── .gitignore
├── README.md
└── CHANGELOG.md              # Version history
```

---

## 🐳 Running with Docker

1. **Build the Docker image:**

```bash
docker build -t model-store .
```

2. **Run the container:**

```bash
docker run -d -p 5000:5000 model-store:latest
```

3. **Access the API docs:**

```
http://localhost:5000/docs
```

---

## 💻 Running Locally (No Docker)

1. **Clone the repository:**

```bash
git clone https://github.com/anafsouza/model-store.git
cd model-store
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate     # On Linux/macOS
venv\Scripts\activate        # On Windows
```

3. **Install dependencies:**

```bash
pip install -r src/requirements.txt
```

4. **Run the application:**

```bash
python src/api_main.py
```

5. **Open the documentation in your browser:**

```
http://localhost:5000/docs
```

---

## 🧪 Running Tests

Run all unit tests with:

```bash
pytest tests/
```

Tests are designed to validate routes, configuration logic, and service integrity.

---

## 🔄 Continuous Integration (CI)

The project uses **Azure Pipelines** for CI. The pipeline defined in `azure-pipelines.yml` performs the following:

* Dependency installation
* Code testing with `pytest`
* (Optional) Build and publish steps for production deployments

---

## 📚 Documentation & References

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Pydantic Docs](https://docs.pydantic.dev/)
* [Redis Docs](https://redis.io/)
* [Docker Guide](https://docs.docker.com/)
* [Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/)



