import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path
import random
fake = Faker()

def generate():
    fake_data = [[fake.first_name(), fake.last_name(), fake.date_of_birth(), fake.email(), fake.phone_number()] for n in range(1000)]
    fake_df = pd.DataFrame(fake_data, columns=['First Name', 'Last Name', 'Birthday', 'Email', 'Phone Number'])
    return fake_df

def save(df):
    # fake_records = generate()
    df.to_csv("data/fake_records.csv")
    return

def load(path):
    df = pd.read_csv(path, index_col = "Email")
    df['Birthday'] = pd.to_datetime(df['Birthday'])
    return df

def assign_salaries(df):
    salaries = [random.randint(20000, 100000) for i in range(len(df))]
    df_salaries = df.assign(Salary = salaries)
    return df_salaries

def over_50k(df):
    return df[df['Salary']>50000]

def normalize(series):
    mean = np.mean(series)
    st_dev = np.std(series)
    normalized = (series - mean)/st_dev
    return normalized

def assign_normalized_salaries(df):
    df_salaries = assign_salaries(df)
    salaries = df_salaries['Salary']
    normalized_salaries = normalize(salaries)
    df_salaries['Normalized Salary'] = normalized_salaries
    #df_normalized_salaries = df_salaries.assign(NormalizedSalaries = normalized_salaries)
    return df_salaries
