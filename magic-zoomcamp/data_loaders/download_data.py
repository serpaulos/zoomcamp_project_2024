import io
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """

    url = 'https://data.ct.gov/api/views/5mzw-sjtu/rows.csv'

    dtypes = {
        "Serial Number": int,
        "List Year": int,
        "Town": str,
        "Address": str,
        "Assessed Value": float,
        "Sale Amount": float,
        "Sales Ratio": float,
        "Property Type": str,
        "Residential Type": str,
        "Non Use Code": str,
        "Assessor Remarks": str,
        "OPM remarks": str,
        "Location": str
            }

    parse_dates = ['Date Recorded']

    
    return pd.read_csv(url, sep=",", dtype=dtypes, parse_dates=parse_dates)
