# 🚗 Getaround – Rental Price Optimization & Delay Management

## Project Overview

**Getaround** is a peer-to-peer car rental platform (like Airbnb for cars).  
This project addresses two business needs:

1. **Minimizing cancellations** by finding the optimal delay between rentals.
2. **Predicting the optimal daily rental price** using machine learning.

---

# Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
# Install common dependencies (edit as needed)
```bash
pip install -r api/requirements.txt
pip install -r ml_flow/requirements.txt
```
---

## 🧠 Machine Learning Model

- **Best model**: `VotingRegressor` (ensemble of XGBoost + others)
- Trained in: `notebooks/ml_model.ipynb`
- 💾 Saved as: `ml_best_model.pkl`
- Used by: FastAPI for real-time predictions

### To regenerate the model

```bash
jupyter notebook notebooks/ml_model.ipynb
```

This creates the file:

```text
ml_best_model.pkl
```

### Load the model manually

```python
import pickle

with open("ml_best_model.pkl", "rb") as f:
    model = pickle.load(f)
```

---

## 🗂️ Project Structure

```text
.
notebooks/
├── 01_preprocessing_delay.ipynb       # EDA - delay
├── 02_preprocessing_pricing.ipynb     # EDA - pricing
├── ml_model.ipynb                     # VotingRegressor training
├── 01-Getaround_analysis.ipynb        # Summary & visuals

cake_app/
├── .streamlit/
├── app.py                             # Streamlit dashboard
└── clean_file_delay.csv               # Preprocessed data

ml_flow/
├── Dockerfile                         # MLflow server image
└── requirements.txt

training/
├── clean_pricing_project.csv
├── ml_model.py                        # Model training script
└── requirements.txt

api/
├── app.py                             # FastAPI app
├── Dockerfile
└── requirements.txt
```

---

## 💻 Technologies Used

- Python (scikit-learn, XGBoost, Pandas)
- Voting Regressor
- Docker
- FastAPI (API)
- Streamlit (Dashboard)
- MLflow (Model tracking)
- Heroku (Deployment)
- S3 & PostgreSQL

---

## 🔐 Environment Variables

Set these variables in your \`.env\` or Docker environment.

### Example

```env
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
BACKEND_STORE_URI=postgresql://user:pass@host:5432/mlflow
ARTIFACT_STORE_URI=s3://your-bucket-name/path/
MLFLOW_TRACKING_URI=https://your-mlflow.herokuapp.com
PORT=4000
```

---

## Local Execution (Docker)

### ▶️ 1. Streamlit Dashboard

```bash
cd cake_app
docker build . -t getaround_streamlit
docker run -p 8501:80 -v "\$(pwd):/home/app" getaround_streamlit
```

🔗 Open: http://localhost:8501  
📂 Upload \`clean_file_delay.csv\` for visualization.

---

### ▶️ 2. MLflow Tracking Server

```bash
cd ml_flow
docker build . -t getaround_mlflow

docker run -p 5000:80 -v "\$(pwd):/home/app" \
  -e PORT=80 \
  -e AWS_ACCESS_KEY_ID=your_key \
  -e AWS_SECRET_ACCESS_KEY=your_secret \
  -e BACKEND_STORE_URI=your_postgres_uri \
  -e ARTIFACT_STORE_URI=your_s3_uri \
  getaround_mlflow
```

🔗 Open: http://localhost:5000

---

### ▶️ 3. FastAPI (Price Prediction API)

```bash
cd api
docker build . -t getaround_api

docker run -p 4000:80 -v "\$(pwd):/home/app" \
  -e PORT=80 \
  -e MLFLOW_TRACKING_URI=https://your-mlflow.herokuapp.com \
  -e AWS_ACCESS_KEY_ID=your_key \
  -e AWS_SECRET_ACCESS_KEY=your_secret \
  -e BACKEND_STORE_URI=your_postgres_uri \
  -e ARTIFACT_STORE_URI=your_s3_uri \
  getaround_api
```

🔗 API Access: http://localhost:4000  
📄 Docs UI: http://localhost:4000/docs

---

##  Example Prediction Request

```json
POST /predict
{
  "model_key": "Citroën",
  "mileage": 45000,
  "engine_power": 110,
  "fuel": "diesel",
  "paint_color": "black",
  "car_type": "sedan",
  "private_parking_available": true,
  "has_gps": true,
  "has_air_conditioning": true,
  "automatic_car": false,
  "has_getaround_connect": true,
  "has_speed_regulator": false,
  "winter_tires": false
}
```

---

## Ports & Access Table

| Service   | Container Port | Host Port | Access URL                                     |
|-----------|----------------|-----------|------------------------------------------------|
| FastAPI   | \`80\`           | \`4000\`    | [http://localhost:4000](http://localhost:4000) |
| MLflow    | \`80\`           | \`5000\`    | [http://localhost:5000](http://localhost:5000) |
| Streamlit | \`80\`           | \`8501\`    | [http://localhost:8501](http://localhost:8501) |

---

## Deployed Apps (Heroku) 

=> ⚠️ Note: The deployed applications are no longer available online

| Component | Link                                                                 |
|-----------|----------------------------------------------------------------------|
| Streamlit | [Getaround Streamlit](https://getaroundapp-78c3d79ff9d2.herokuapp.com/)     |
| FastAPI   | [FastAPI Docs](https://fast-api-price-optimisation-d4d8b772232c.herokuapp.com/docs) |
| MLflow    | [MLflow UI](https://server-mlflow-d231fb5910ab.herokuapp.com/)             |

---

## 📁 Data Files

| File                        | Description                             |
|-----------------------------|-----------------------------------------|
| \`clean_file_delay.csv\`      | For Streamlit visualization             |
| \`clean_pricing_project.csv\` | For training pricing ML model           |
| \`ml_best_model.pkl\`         | Trained VotingRegressor for FastAPI     |

---


## Final Recommendation

Report & Recommandations:
Only 7% of rentals are delayed which is relatively low.

We can notice that most of the delays concern significant delays, ie more than one hour. It would be wise to offer a discount to customers in case of punctuality to encourage them to be on time.

The connect checkin_type represents only 20% of rentals, but more than 24% of cancellations. Perhaps not having to meet the next tenant in person to hand over the keys makes you less punctual.

It is interesting to note that out of all the problematic delays (checkout vs time delta) only 194 lead to a cancellation, ie less than 1%.

It is surprising that all rental cancellations occur when the delivery of the vehicle was done on time. The people who created the dataset should be interviewed for more information about how the data was collected. (This finding may also be due to the fact that I took the decision to set the nan values ​​of the delay_at_checkout_in_minutes to 0)

According to this data, it is not necessary to set a maximum period between rentals in order to minimise cancellations and turnover loss.

---


## Author

**Thibaut Longchamps**  
🔗 [GitHub](https://github.com/Thibaut-Longchamps)





