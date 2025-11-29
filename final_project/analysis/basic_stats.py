# analysis/basic_stats.py

import pandas as pd 
from .base import AnalysisStrategy 

class BasicStatsStrategy(AnalysisStrategy): 
    """
    Computes and prints basic descriptive statistics for all columns.
    """

    def run(self, df: pd.DataFrame):
        print("=== BASIC STATISTICS ===")
        print(df.describe(include='all'))   