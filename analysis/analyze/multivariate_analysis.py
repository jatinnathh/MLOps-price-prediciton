from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class MultivariateAnalysisTemplate(ABC):
    def analyze(self,df:pd.DataFrame):
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)

    @abstractmethod
    def generate_correlation_heatmap(self,df:pd.DataFrame):
        pass

    @abstractmethod
    def generate_pairplot(self,df:pd.DataFrame):
        pass


class SimpleMultivariateAnalysis(MultivariateAnalysisTemplate):
    def generate_correlation_heatmap(self, df:pd.DataFrame):
        plt.figure(figsize=(12,10))
        sns.heatmap(df.corr(),annot=True,fmt='.2f',cmap="coolwarm",linewidth=0.5)
        plt.title("correlation heatmap")
        plt.show()
        
    def generate_pairplot(self, df:pd.DataFrame):
        
        sns.pairplot(df)
        plt.suptitle("Pair Plot of Selected Features", y=1.02)
        plt.show()
        