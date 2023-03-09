import pandas as pd

def expand_zip(column: pd.Series) -> pd.DataFrame:
    df = column.str.split("-", expand=True)
    df = df.rename(columns={0: "Zip", 1: "+4"})
    return df


def strip_punctuation(column: pd.Series) -> pd.Series:
    pass


def combine(path):
    pass
