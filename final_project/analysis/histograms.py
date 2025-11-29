# analysis/histograms.py

import pandas as pd
import matplotlib.pyplot as plt
from .base import AnalysisStrategy

class HistogramStrategy(AnalysisStrategy):
    """
    Plots a histogram for a specified column.
    """

    def __init__(self, column: str):
        self.column = column

    def run(self, df: pd.DataFrame):
        df[self.column].hist()
        plt.title(f"Histogram of {self.column}")
        plt.xlabel(self.column)
        plt.ylabel("Frequency")
        plt.show()
