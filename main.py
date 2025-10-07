"""Main"""
from data_access import DataAccess
from cli import show_all_data


def main():
    """Main function to tests"""
    data_access = DataAccess
    data = data_access.get_all_data(None)
    show_all_data(data)


main()
