"""Layer to get data by PySUS"""
from pysus.online_data import SINAN as sinan_online
from pysus.ftp.databases.sinan import SINAN as sinan_database
import pandas as pd

# it'll be use a old year to load faster
YEAR = 2000
DISEASE = 'DENG'
COLUMNS_TO_KEEP = ['CS_SEXO', 'NU_IDADE']


def get_fields_summary():
    """Get fields summary from SINAN metadata"""
    metadata = sinan_online.metadata_df(DISEASE)

    # Get first 100 rows (or all rows if less than 100)
    filtered_data = metadata[["DBF", "Nome do campo", "Categoria"]]

    return filtered_data


def get_all_data(dev_mode=False):
    """Get all data or optional fields summary for development help
    
    Args:
        dev_mode: If True, displays fields summary for developers
    """
    # get summary if in dev mode
    if dev_mode:
        return get_fields_summary()

    # download data
    sinan = sinan_database().load()
    file = sinan.get_files(DISEASE, YEAR)[0]
    download = sinan.download(file).to_dataframe()
    download = download[COLUMNS_TO_KEEP]

    # convert age to int
    download['NU_IDADE'] = pd.to_numeric(
        download['NU_IDADE'].str[1:], errors='coerce'
    ).fillna(0).astype(int)

    return download
