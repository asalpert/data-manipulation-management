import pandas as pd
import string
import us
import zipcodes

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

def street_suffixes (address: pd.Series) -> pd.Series:
    pass

def saint_to_st(element: pd.Series) -> pd.Series:
    return element.replace("SAINT", "ST")

def filter_states(address: pd.Dataframe) -> pd.DataFrame:
    pass

def filter_zips(address: pd.DataFrame) -> pd.DataFrame:
    pass

def clean_addresses(address: pd.DataFrame) -> pd.DataFrame:
    df_clean = standardize_frame(address)

    return df_clean

def strip_punctuation(column: pd.Series) -> pd.Series:
    pass


def combine(path):
    pass
