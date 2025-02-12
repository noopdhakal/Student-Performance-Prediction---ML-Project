# purpose -->  feature engineering, data cleaning, convert categorical into numerical

import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer ## used to create a pipeline
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        # This function is responsible for data transformation

        try:
            numerical_coumns = ['writing_score', 'reading_score']
            categorical_coumns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]


            ## handle missing values

            # creating pipeline on training data set
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),## imputer --> handle missing values
                    ("scaler", StandardScaler()) # for scale
                ]

                 )

                ## similarly for categorical pipeline
            cat_pipeline=Pipeline(
                    steps = [
                        ("imputer",  SimpleImputer(strategy="most_frequent")),
                        ("one_hot_encoder", OneHotEncoder())
                        ("scarer", StandardScaler())
                    ]     
            )


            logging.info("Numerical columns standard scaling completed")

            logging.info("Categorical columns encoding completed")
            ## combine numerical pipeline and categorical pipeline

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_coumns)
                    ("cat_pipeline", cat_pipeline, categorical_coumns)
                ]
            )

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)

def initiate_data_transformation(self, train_path, test_path):
    try:
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        logging.info("Read train and test data completed")

        logging.info("Obtaining preprocessing object")

        preprocessing_obj = self.get_data_transformer_object()

        target_column_name = "math_score"
        numerical_columns = ["writing_score", "reading_score"]

        input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
    except:
        pass