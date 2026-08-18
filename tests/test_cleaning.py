import pandas as pd
from src.data_cleaning import standardise_text, cap_outliers_iqr


def test_standardise_text():
    s = pd.Series([" online ", "DIRECT", "partner "])
    result = standardise_text(s).tolist()
    assert result == ["Online", "Direct", "Partner"]


def test_cap_outliers_preserves_length():
    s = pd.Series([1, 2, 3, 4, 1000])
    result = cap_outliers_iqr(s)
    assert len(result) == 5
    assert result.max() < 1000
