# analysis/distributions.py

import pandas as pd
from .base import AnalysisStrategy

class DistributionStrategy(AnalysisStrategy):
    """
    Prints value counts and relative frequencies for a column.
    Useful for both categorical and discrete numerical variables.
    """

    def __init__(self, column: str):
        self.column = column

    def run(self, df: pd.DataFrame):
        counts = df[self.column].value_counts()
        print(f"=== DISTRIBUTION OF {self.column} ===")
        print(counts)
        print("\nRelative frequencies:")
        print(counts / counts.sum())
