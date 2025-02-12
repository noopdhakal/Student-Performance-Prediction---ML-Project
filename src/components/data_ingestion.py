# all the codes that reading the code then data validation and transformation
## data sources can be from big data team, or from cloud or anything

import os
import sys
from src.exception import CustomException # for exception
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from  dataclasses import dataclass


## any input required probably give in this data ingestion config
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', "train.csv")  ## all the output sotred into this artifacts folder 
    test_data_path: str=os.path.join('artifacts', "test.csv") 
    raw_data_path: str=os.path.join('artifacts', "raw.csv") 


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() ## three path would be saved inside this particular variable
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv') ## can be from anywhere UI, API
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True) ## raw data path is saved into csv file

            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return ( 
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()