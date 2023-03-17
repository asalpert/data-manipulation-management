import pandas as pd
import string
import us
import zipcodes
import json

with open('data/street_suffixes.json') as file:
    street_mapping = json.load(file)

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
    last_word = address.split()[-1]

    # [_ for abbr, names in street_mapping if _ in names]
    for a in address:
        for abbr, names in street_mapping.items():
            for n in names:
                if last_word == n:
                    address = address.replace(last_word, abbr)

    return address


def saint_to_st(element: pd.Series) -> pd.Series:
    return element.replace("SAINT", "ST")

def filter_states(address: pd.DataFrame) -> pd.DataFrame:
    real_state = {state.abbr for state in us.states.STATES_AND_TERRITORIES}
    address = address[address['State'].isin(real_state)]

    return address

def filter_zips(address: pd.DataFrame) -> pd.DataFrame:
    address = address.loc[address['Zip'].apply(lambda num: all(z.isnumeric() or z =="-" for z in num))]
    address = address[address['Zip'].apply(lambda num: zipcodes.is_real(num))]

    return address

def clean_addresses(data: pd.DataFrame) -> pd.DataFrame:
    # order of operations: split zipcode, standardize df, filter state/zip, suffixes, saint
    df_clean = data
    df_zip = expand_zip(data['Zip'])
    df_clean[['Zip', '+4']] = df_zip
    df_clean = filter_states(df_clean)
    df_clean = filter_zips(df_clean)
    df_clean = standardize_frame(df_clean)
    df_clean['Address 1'] = df_clean['Address 1'].apply(street_suffixes)
    df_clean['City'] = df_clean["City"].apply(saint_to_st)

    return df_clean

def strip_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns.names = df.columns.str.strip()
    return df


def strip_punctuation(column: pd.Series) -> pd.Series:
    pass


def combine(path):
    pass
