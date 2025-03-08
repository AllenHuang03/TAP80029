import pandas as pd
from astropy.io import fits

def load_fits(file_path):
    with fits.open(file_path) as hdul:
        return hdul[0].data  # Extract data

def load_csv(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    df = df.dropna()
    df["normalized_flux"] = (df["flux"] - df["flux"].min()) / (df["flux"].max() - df["flux"].min())
    return df
