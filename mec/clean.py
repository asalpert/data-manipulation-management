import pandas as pd
import string

def expand_zip(column: pd.Series) -> pd.DataFrame:
    df = column.str.split("-", expand=True)
    df = df.rename(columns={0: "Zip", 1: "+4"})
    return df

def standardize_element(element: str) -> str:
    punctuation = string.punctuation
    for p in range(len(punctuation)):
        standard = element.upper().replace(punctuation[p], "")
    return standard


def strip_punctuation(column: pd.Series) -> pd.Series:
    pass


def combine(path):
    pass
