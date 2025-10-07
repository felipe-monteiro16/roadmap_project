"""Layer to get data by PySUS"""
from pysus.online_data import SINAN
import pandas as pd


def get_fields_summary():
    """Get fields summary from SINAN metadata"""
    metadata = SINAN.metadata_df('DENG')

    # set pandas options
    pd.set_option('display.max_rows', 100)
    pd.set_option('display.max_colwidth', 100)

    # Get first 100 rows (or all rows if less than 100)
    filtered_data = metadata[["DBF", "Nome do campo", "Categoria"]].head(100)

    return filtered_data


def get_all_data(dev_mode=False):
    """Get all data with optional fields summary for development help
    
    Args:
        dev_mode: If True, displays fields summary for developers
    """
    if dev_mode:
        return get_fields_summary()

    return "The other data"
