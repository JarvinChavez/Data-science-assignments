# abstract base classesss
from abc import ABC, abstractmethod
import pandas as pd


class AnalysisStrategy(ABC):
    """
    Base class for all analysis strategies.
    Every analysis class must implement the run() method.
    """

    @abstractmethod
    def run(self, df: pd.DataFrame):
        """
        Execute the analysis on the provided dataframe.

        Parameters:
            df (pd.DataFrame): The dataset to analyze.

        Returns:
            Any: Strategies may return figures, stats, or None,
                 depending on their purpose.
        """
        pass
