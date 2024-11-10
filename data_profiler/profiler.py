# data_profiler/profiler.py

import pandas as pd

class DataProfiler:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def summary_statistics(self):
        """Generate summary statistics for numerical columns."""
        return self.df.describe()

    def missing_values_report(self):
        """Detect missing values in the dataset."""
        return self.df.isnull().sum()

    def detect_outliers(self, z_thresh=3):
        """Detect outliers using Z-score method."""
        from scipy import stats
        numeric_cols = self.df.select_dtypes(include=[float, int])
        outliers = (abs(stats.zscore(numeric_cols)) > z_thresh).any(axis=1)
        return self.df[outliers]
