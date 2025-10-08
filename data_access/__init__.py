"""Data access layer"""
from .pysus_data import get_all_data, get_fields_summary, download_data


class DataAccess:
    """Data access class"""
    def __init__(self):
        pass


    def get_fields_summary(self):
        """Get fields summary"""
        return get_fields_summary()


    def download_data(self):
        """Download data from SINAN"""
        return download_data()


    def get_all_data(self, dev_mode=False):
        """Get all data"""
        return get_all_data(dev_mode=dev_mode)
