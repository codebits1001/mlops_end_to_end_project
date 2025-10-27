'''# A very important role in end to end model deployments. 

# Read the dataset from the some specific source, ( from many possiblities)


import os 
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass # @dataclass automatically generates an initializer for you.
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")
        try:
            df = pd.read_csv('../data/AB_NYC_2019.csv')
            logging.info('Read the datasets as data_frame')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True) #"Create the folder (artifacts/) where the training data file will be saved, if it doesn't already exist."
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)

            logging.info("Train Test Split: Inititated")
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = True)
        except:
            pass


# os.path.join() --> function from Python’s os.path module that helps you safely and correctly build file paths by joining directory and file names together.
'''

# Now we will work upon the pipeline of DataIngestion and how we can do 
'''
1. Since our dataset first will be of raw data, we create seperate folders for them to stored,
i. train_data_path.csv, folder-> artifacts, 
ii. test_data_path.csv, folder-> artifacts,
iii. raw_data_path.csv, folder-> artifacts

so we will build first our config class, with class level variables, along with the file name we want and 
inside the folder we want.

Steps: 
1. Create the cofig class with class level variables.
2. Create the DataIngestion calss with constructor and initializing the variables inisde this class with 
   instance of the config class so that variable can used class level variables from config class
3. Inside the data_ingestion class create the function(initiate_data_ingestion)
    i. First read the csv file from anyhwere or from the source you have
    ii. make directories for raw_data
    iii. move the csv raw data to respective created directory
    iv. Do train test split and stored the seperate files as well with same path and approach
'''

import pandas as pd
from src.exception import CustomException
from src.logger import logging

from dataclasses import dataclass
import os
import sys
from sklearn.model_selection import train_test_split


# Create the config class for the datasets we want to work with their respective folders and file path 
@dataclass
class DataIngestionConfig():
    raw_data_path:str = os.path.join('artifacts', 'raw_data.csv')
    train_data_path: str = os.path.join('artifacts', 'train_data.csv')
    test_data_path: str = os.path.join('artifacts', 'test_data.csv')


# Create the dataIngestion class 

class DataIngestion():
    def __init__(self):

        self.ingestion_config = DataIngestionConfig() # we instantiate the config class with our class level variable of DataIngestion

    # Creating the another function for initiating the DataIngestion:

    def initiate_ingestion(self):

        logging.info('DataIngestion Process Initiated:')
        try:
            df = pd.read_csv('notebook/data/AB_NYC_2019.csv' )
            logging.info('Dataset succesfully read, entering the next process')
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)

            logging.info('Initializing the train_test_split')
            train_set, test_set = train_test_split(df, test_size = 0.3, random_state = 42)
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info('Sucessfully splited and save in respective directores: Ingestion of the Data is completed')
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e, sys)
        # Completed that's it

if __name__=='__main__':
    obj = DataIngestion()
    obj.initiate_ingestion()


