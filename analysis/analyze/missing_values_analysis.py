from abc import ABC,abstractmethod

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class MissingValueAnalysisTemplate(ABC):
    def analyze(self,df:pd.DataFrame):

        self.identify_missing_values(df)
        self.visualize_missing_values(df)

    @abstractmethod
    def identify_missing_values(self,df:pd.DataFrame):
        pass

    @abstractmethod
    def visualize_missing_values(self,df:pd.DataFrame):
        pass


class SimpleMissingValuesAnalysis(MissingValueAnalysisTemplate):
    def identify_missing_values(self, df:pd.DataFrame):
        print("\nMissing values count by column : ")
        missing_vaues=df.isnull().sum()
        print(missing_vaues[missing_vaues>0])

    def visualize_missing_values(self, df):
        print("\nVisualizing Missing values")
        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(),cbar=False,cmap='viridis')
        plt.title("Missing values Heatmap")
        plt.show()

        