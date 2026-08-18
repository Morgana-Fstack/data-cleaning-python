import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pratica_pandas import clean_data, load_data


class DataCleaningTests(unittest.TestCase):
    def setUp(self) -> None:
        self.original = load_data()
        self.cleaned = clean_data(self.original)

    def test_cleaning_does_not_modify_original_data(self) -> None:
        self.assertTrue(self.original['Calories'].isna().any())

    def test_missing_calories_are_filled_with_zero(self) -> None:
        self.assertFalse(self.cleaned['Calories'].isna().any())
        self.assertIn(0, self.cleaned['Calories'].values)

    def test_dates_are_valid_and_missing_dates_are_removed(self) -> None:
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.cleaned['Date']))
        self.assertFalse(self.cleaned['Date'].isna().any())
        self.assertEqual(len(self.cleaned), len(self.original) - 1)


if __name__ == '__main__':
    unittest.main()
