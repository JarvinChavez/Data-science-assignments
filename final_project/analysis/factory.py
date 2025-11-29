# analysis/factory.py

from .basic_stats import BasicStatsStrategy
from .histograms import HistogramStrategy
from .kde import KDEStrategy
from .distributions import DistributionStrategy

def create_strategy(name: str, **kwargs):
    """
    Factory function to create an analysis strategy by name.

    Parameters:
        name (str): The name of the strategy (e.g., "basic_stats", "histogram").
        kwargs: Optional parameters required by specific strategies (e.g., column="age").

    Returns:
        An instance of the requested AnalysisStrategy.

    Raises:
        ValueError: If the strategy name is unknown.
    """
    name = name.lower()
    
    if name == "basic_stats":
        return BasicStatsStrategy()
    
    if name == "histogram":
        if "column" not in kwargs:
            raise ValueError("HistogramStrategy requires a 'column' argument")
        return HistogramStrategy(kwargs["column"])
    
    if name == "kde":
        if "column" not in kwargs:
            raise ValueError("KDEStrategy requires a 'column' argument")
        return KDEStrategy(kwargs["column"])
    
    if name == "distribution":
        if "column" not in kwargs:
            raise ValueError("DistributionStrategy requires a 'column' argument")
        return DistributionStrategy(kwargs["column"])
    
    raise ValueError(f"Unknown strategy: {name}")
