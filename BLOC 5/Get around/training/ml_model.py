import argparse
import pandas as pd
import time
import mlflow
from mlflow.models.signature import infer_signature
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
import os

if __name__ == "__main__":
    os.environ["APP_URI"] = "https://server-mlflow-d231fb5910ab.herokuapp.com/"
    mlflow.set_tracking_uri(os.environ["APP_URI"])

    ### MLFLOW Experiment setup
    # Set environment variables
    experiment_name = "new_ml-flow-experiment-getaround2"
    # Set experiment's info
    mlflow.set_experiment(experiment_name)
    # Get our experiment info
    experiment = mlflow.get_experiment_by_name(experiment_name)

    client = mlflow.tracking.MlflowClient()

    run = client.create_run(experiment.experiment_id)

    print("Training model...")

    # Call mlflow autolog
    mlflow.sklearn.autolog(log_models=False)  # We won't log models right away

    # Parse arguments given in shell script
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_depth", default=10)
    parser.add_argument("--learning_rate", default=0.05)
    parser.add_argument("--n_estimators", default=150)
    parser.add_argument("--colsample_bytree", default=0.5)
    parser.add_argument("--subsample", default=0.8)
    args = parser.parse_args()

    # Import dataset
    df = pd.read_csv("/data/clean_pricing_project.csv")

    # X, y split
    target_col_name = "rental_price_per_day"
    X = df.loc[:, df.columns != target_col_name]
    y = df.loc[:, target_col_name]

    # Train / test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Preprocessing
    categorical_features = X_train.select_dtypes("object").columns  # Select all the columns containing strings
    categorical_transformer = OneHotEncoder(drop='first', handle_unknown='ignore', sparse=False)

    numerical_feature_mask = ~X_train.columns.isin(X_train.select_dtypes("object").columns)  # Select all the columns containing anything else than strings
    numerical_features = X_train.columns[numerical_feature_mask]
    numerical_transformer = StandardScaler()

    preprocessor = ColumnTransformer(
        transformers=[
            ("categorical_transformer", categorical_transformer, categorical_features),
            ("numerical_transformer", numerical_transformer, numerical_features)
        ]
    )

    # Pipeline
    param_grid = {
        'Regressor__max_depth': [int(args.max_depth)],
        'Regressor__learning_rate': [float(args.learning_rate)],
        'Regressor__n_estimators': [int(args.n_estimators)],
        'Regressor__colsample_bytree': [float(args.colsample_bytree)],
        'Regressor__subsample': [float(args.subsample)]
    }

    model = GridSearchCV(
        estimator=Pipeline(steps=[
            ("Preprocessing", preprocessor),
            ("Regressor", XGBRegressor())
        ], verbose=True),
        param_grid=param_grid,
        cv=KFold(n_splits=4),
        verbose=True
    )

    # Log experiment to MLFlow
    with mlflow.start_run(run_id=run.info.run_id) as run:
        model.fit(X_train, y_train)
        predictions = model.predict(X_train)

        # Log model separately to have more flexibility on setup
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="getaround_price_optimization",
            registered_model_name="getaround_xgbg_best_test",
            signature=infer_signature(X_train, predictions)
        )

        best_params = model.best_params_
        print("Best parameters:", best_params)

        mlflow.log_params(best_params)
        mlflow.log_metric("best_score", model.best_score_)

        # Enregistrer le modèle
        mlflow.sklearn.log_model(model.best_estimator_, "getaround_xgbg_best_test")

    print("...Done!")

