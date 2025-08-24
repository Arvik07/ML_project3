
from networksecurity.components import data_ingestion
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__=='__main__':
    try:
        trainpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the Data Ingestion process.")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion process completed.")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Initiate the Data Validation process.")
        data_validation_artifact =data_validation.initiate_data_validation()
        logging.info("Data Validation process completed.")        
        print(data_validation_artifact)
        data_transformation_config = DataTransformationConfig(trainpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        logging.info("Initiate the Data Transformation process.")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation process completed.")
        print(data_transformation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)
