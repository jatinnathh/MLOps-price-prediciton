from abc import ABC , abstractmethod
import pandas as pd

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self,df:pd.DataFrame):
        pass

class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self,df:pd.DataFrame):
        print("\nData types and non=null counts:")
        print(df.info())


class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self,df:pd.DataFrame):
        print("Summary Statistics(numerical)")
        print(df.describe())
              
        print("\n\nSummary Statistics (categorical)")
        print(df.describe(include=['O']))

class DataInspector:
    def __init__(self,strategy: DataInspectionStrategy):
        self._strategy=strategy

    def set_strategy(self,strategy=DataInspectionStrategy):
        self._strategy=strategy

    def execute_inspection(self,df:pd.DataFrame):
        self._strategy.inspect(df)
