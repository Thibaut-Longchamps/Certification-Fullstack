import uvicorn
from fastapi import FastAPI
import mlflow
from pydantic import BaseModel
from typing import Literal, List, Union
from fastapi import FastAPI, File, UploadFile
import pandas as pd
import json
import mlflow.pyfunc

### 
# Here you can define some configurations 
###

"""
# Machine-Learning 

## Where you can:
* `/predict` if one person is likely to quit the company
* `/batch-predict` where you can upload a file to get predictions for several employees


Check out documentation for more information about endpoint.
"""


description ="""

# Welcome to this machine learning API. This API is designed to predict optimize rental prices

Where you can:
* `/predict` the best price for a daily car rental

"""

app = FastAPI(
    title='Rental Price Optisation API',
    description=description
)   
    
class PredictionFeatures(BaseModel):
    model_key: str        
    mileage: Union[int, float]
    engine_power: Union[int, float] 
    fuel: str
    paint_color: str
    car_type: str
    private_parking_available: bool  
    has_gps: bool  
    has_air_conditioning: bool  
    automatic_car: bool  
    has_getaround_connect: bool  
    has_speed_regulator: bool  
    winter_tires: bool  
    
###
# Here you define enpoints 
###

@app.post("/predict", tags=["Machine Learning"])
async def predict(features: PredictionFeatures):

    rental_price= pd.DataFrame({
        "model_key": [features.model_key],
        "mileage":[features.mileage],
        "engine_power": [features.engine_power],
        "fuel": [features.fuel],
        "paint_color": [features.paint_color],
        "car_type":[features.car_type],
        "private_parking_available": [features.private_parking_available],
        "has_gps": [features.has_gps],
        "has_air_conditioning": [features.has_air_conditioning],
        "automatic_car": [features.automatic_car],
        "has_getaround_connect":[features.has_getaround_connect],
        "has_speed_regulator": [features.has_speed_regulator],
        "winter_tires": [features.winter_tires]
         })
    
    
    logged_model = 'runs:/e2cf6ec283184468879ec9ad764187ce/getaround_price_optimization'
    
    # Load model as a PyFuncModel.
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    # Predict on a Pandas DataFrame.
    prediction = loaded_model.predict(pd.DataFrame(rental_price))
    
    response = {
        "rental_price_per_day": prediction.tolist()[0]
        }

    return response

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000) # Here you define your web server to run the `app` variable (which contains FastAPI instance), with a specific host IP (0.0.0.0) and port (4000)
    