"""Main"""
import argparse
from data_access import DataAccess
from cli import show_all_data


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='SINAN Data Access Tool')

    parser.add_argument(
        '-d', '--dev',
        action='store_true',
        help='Enable development mode (shows field summary)'
    )

    return parser.parse_args()


def get_fields_summary():
    """Get fields summary from SINAN metadata"""
    data_access = DataAccess()
    data = data_access.get_fields_summary()
    show_all_data(data)


def get_all_data(dev_mode=False):
    """Main function to tests"""
    data_access = DataAccess()
    data = data_access.get_all_data(dev_mode=dev_mode)
    show_all_data(data)


if __name__ == "__main__":
    args = parse_arguments()
    get_all_data(dev_mode=args.dev)
