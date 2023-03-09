import pandas as pd
import string

def expand_zip(column: pd.Series) -> pd.DataFrame:
    df = column.str.split("-", expand=True)
    df = df.rename(columns={0: "Zip", 1: "+4"})
    return df

def standardize_element(column: pd.Series) -> pd.Series:
    punctuation = [x for x in string.punctuation]
    standard = column
    for p in range(len(punctuation)):
        standard = standard.upper().replace(str(punctuation[p]), "")
    return standard

def standardize_frame (df: pd.DataFrame) -> pd.DataFrame:
   return df.applymap(lambda col: standardize_element(col))

def street_types_to_abbr (element: str) -> str:
    
    pass



def strip_punctuation(column: pd.Series) -> pd.Series:
    pass


def combine(path):
    pass
