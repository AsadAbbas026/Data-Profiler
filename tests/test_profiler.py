# tests/test_profiler.py

import unittest
import pandas as pd
from data_profiler.profiler import DataProfiler

class TestDataProfiler(unittest.TestCase):
    def setUp(self):
        data = {
            'col1': [1, 2, None, 4, 5],
            'col2': [10, 20, 30, 40, 50]
        }
        self.df = pd.DataFrame(data)
        self.profiler = DataProfiler(self.df)

    def test_summary_statistics(self):
        summary = self.profiler.summary_statistics()
        self.assertTrue('col1' in summary.columns)

    def test_missing_values_report(self):
        missing_values = self.profiler.missing_values_report()
        self.assertEqual(missing_values['col1'], 1)

if __name__ == '__main__':
    unittest.main()
