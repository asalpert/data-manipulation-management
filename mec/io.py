import requests
import zipfile
import io
import pandas as pd


def fetch_data(url: str) -> None:
    response = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall("data/0-raw")


def csv_paths(dir):
    pass


def read_single_csv(path) -> pd.DataFrame:
    pass


def load_contributions(raw_data_dir) -> pd.DataFrame:
    pass
