"""Data access layer"""
from .pysus_data import get_all_data


class DataAccess:
    """Data access class"""
    def __init__(self):
        self.number = 1


    def get_all_data(self):
        """Get all data"""
        return get_all_data() + str(self.number)
