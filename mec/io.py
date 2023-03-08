import requests
import zipfile
import io
import pandas as pd
from pathlib import Path


def fetch_data(url: str) -> None:
    response = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall("data/0-raw")


def csv_paths(dir):
    return Path(dir).glob("*csv")


def read_single_csv(path) -> pd.DataFrame:
    df = pd.read_csv(path, index_col=['CD1_A ID'], parse_dates=['Date'])
    return df


def load_contributions(raw_data_dir) -> pd.DataFrame:
    df_main
    paths = csv_paths(raw_data_dir)
    for path in paths:
        df_sub = read_single_csv(path)
        df_main = pd.concat(df_main, df_sub)
    return df_main
