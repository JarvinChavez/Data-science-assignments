# analysis/kde.py

import pandas as pd
import seaborn as sns
from .base import AnalysisStrategy

class KDEStrategy(AnalysisStrategy):
    """
    Plots a Kernel Density Estimate for a specified column.
    """

    def __init__(self, column: str):
        self.column = column

    def run(self, df: pd.DataFrame):
        sns.kdeplot(df[self.column], fill=True)
        sns.plt.show()
