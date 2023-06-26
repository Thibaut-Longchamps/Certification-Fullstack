
### Link Vydiard video: https://secure.vidyard.com/organizations/3270029/players/m2NMusJNEmq2PmMdjNav9P?edit=true



## Welcome to this get around project: 

Getaround is the Airbnb for cars. You can rent cars from any person for a few hours to a few days! Founded in 2009, this company has known rapid growth. In 2019, they count over 5 million users and about 20K available cars worldwide.


## Goals:

The aim of this project is to find a maximum time threshold between each rental that will enable the company to minimise its cancellations.
The second objective is to build a machine learning algorithm to predict the optimal price for a day's rental.

Good viewing ! :)

## Structure:

notebooks:
- Exploratory data analysis : 01_preprocessing_delay.ipynb & 02_preprocessing_pricing.ipynb
- model training: ml_model.ipynb
- project description: 01-Getaround_analysis.ipynb

cake_app:
- configuration file for dashbord (color...): .streamlit 
- script dashbord: app.py
- clean csv: clean_file_delay.csv ( = getaround_delay_analysis.csv with preprocessing)
- Dockerfile
- depencies: requirements.txt

ml_flow:
- image: Dockerfile
- Depencies: requirements.txt

training:
- clean data for machine learning: clean_pricing_project.csv
- image: Dockerfile
- Depencies: requirements.txt
- Machine learning script with best model (XGBOOST Gridsearch): ml_model.py

api:
/docker
- image: Dockerfile
- Depencies: requirements.txt
- script FastAPI: app.py

data: csv data




## LOCAL SERVER
-----------------------------------------------------------------------------------

streamlit:  run this command in the terminal (/cake_app)
When you connect please upload and submit the file 'clean_file_delay.csv' in cake_app repository for visualization

# create image
docker build . -t my_getaround_image      

# run contener
docker run -it -v "$(pwd):/home/app" -e PORT=80 -p "4000:80" <YOUR_IMAGE_NAME>     

# port mapping (in the contener bash)
streamlit run --server.port 80 --server.address 0.0.0.0 app.py    

# Open local server
localhost:80 (windows)
0.0.0.0:80 (mac, linux)

-----------------------------------------------------------------------------------------

mlflow server:  run this command in the terminal (/ml_flow)

# create image
docker build . -t <YOUR_IMAGE_NAME>

# define environment variables, port mapping and run contener
docker run -it -p 4000:80 -v "$(pwd):/home/app" -e PORT=80 -e AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY_ID> -e AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACESS_KEY> -e BACKEND_STORE_URI=nothing -e ARTIFACT_STORE_URI=<YOUR_ARTEFACT_STORE_URI> <YOUR_IMAGE_NAME>

# Open local server
localhost:80 (windows)
0.0.0.0:80 (mac, linux)

----------------------------------------------------------------------------------------------

fast api:    run this command in the terminal (/api)

# create image
docker build . -t <YOUR_IMAGE_NAME>

# run contener, port mapping & set environment variables
docker run -it -v "$(pwd):/home/app" -p 4000:4000 -e PORT=4000 -e MLFLOW_TRACKING_URI=<YOUR_MLFLOW_TRACKING_URI> -e AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY_ID> -e AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESS_KEY> -e BACKEND_STORE_URI=<YOUR_BACKEND8STORE_URI> -e ARTIFACT_STORE_URI=<YOUR_ARTIFACT_STORE_URI> <YOUR_IMAGE_NAME>

# Open local server
localhost:4000 (windows)
0.0.0.0:4000 (mac, linux)


If you want to push these app on heroku please do not forget set up environment variables on heroku.

----------------------------------------------------------------------------------------------------

## APP WEB LINK :

# fast-api-price-optimisation: https://fast-api-price-optimisation-d4d8b772232c.herokuapp.com/docs
end point: /docs (documentation)
           /predict (predictions for one sample)

# mlflow server: https://server-mlflow-d231fb5910ab.herokuapp.com/
The best model is silent-gull-319: getaround_price_optimization (model: getaround_xgbg_best_test)

# streamlit dashbord: https://getaroundapp-78c3d79ff9d2.herokuapp.com/
When you connect please upload and submit the file 'clean_file_delay.csv' in cake_app repository for visualization


technology used for structure:

Docker / FastAPI / Streamlit / MLflow / Heroku / S3 / POSTGRESQL