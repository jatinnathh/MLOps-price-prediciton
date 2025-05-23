import logging 
from abc import ABC,abstractmethod
from typing import Any

import pandas as pd
from sklearn.base import RegressorMixin
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import StandardScaler


logging.basicConfig(level=logging.INFO , format="%(asctime)s-(%levelname)s-%(message)s")

class ModelBuildingStrategy(ABC):

    @abstractmethod
    def build_and_train_model(delf,X_train:pd.DataFrame,y_train:pd.Series)->RegressorMixin:
        pass


class LinearRegressionStrategy(ModelBuildingStrategy):

    def build_and_train_model(self,X_train:pd.DataFrame,y_train:pd.Series)-> Pipeline:

        if not isinstance(X_train,pd.DataFrame):
            raise TypeError("X_Train must be a data frame ")
        if not isinstance(y_train,pd.Series):
            raise TypeError("y_Train must be a series  ")
        

        logging.info("INitializing Linaer Regression Modle")

        pipeline=Pipeline(
            [
                ("scaler",StandardScaler()),
                ("model",LinearRegression()),
            ]
        )

        logging.info("Traning linear model")
        pipeline.fir(X_train,y_train)

        logging.info("Model trianing completed")
        return pipeline
    
 
class ModelBuilder:

    def __init__(self,strategy:ModelBuildingStrategy):
        self._strategy=strategy

    def set_strategy(self,strategy:ModelBuildingStrategy):
        logging.info("Switching model building strategy.")
        self._strategy = strategy

    def build_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> RegressorMixin:
        logging.info("Building and training the model using the selected strategy.")
        return self._strategy.build_and_train_model(X_train, y_train)