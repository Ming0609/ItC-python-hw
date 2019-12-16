import argparse
from datetime import datetime


def get_args():
    # TODO: Add --start-date, --end-date and --output arguments
    #       Convert the two dates to datetime objects
    parser = argparse.ArgumentParser()
    parser.add_argument('--start-date', type = valid_date, help="The Start Date - format YYYY-MM-DD",
                         required = True)
    parser.add_argument('--end-date', type = valid_date, help="The End Date - format YYYY-MM-DD",
                         required = True)
    parser.add_argument('--output', type = str, help="The Start Date - format YYYY-MM-DD",
                         required = True)
    args = parser.parse_args()
    return args

def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = f"Not a valid date: {s}."
        raise argparse.ArgumentTypeError(msg)