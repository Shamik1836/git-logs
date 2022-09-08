import argparse

args_parser = argparse.ArgumentParser(description="Display information from .git")

args_parser.add_argument("-f", "--frequency", action="store", dest="frequency",
                   type=str, required=False, default="month",
                   choices=["day", "week", "month", "year"])

args_parser.add_argument("-u", "--author", action="store", dest="author",
                   type=str, required=False, default="",
                   help="filter by author's e-mail (substring)")

args_parser.add_argument("-a", "--after", action="store", dest="after",
                   type=str, required=False, default="",
                   help="after date (yyyy-mm-dd hh:mm)")

args_parser.add_argument("-b", "--before", action="store", dest="before",
                   type=str, required=False, default="",
                   help="before date (yyyy-mm-dd hh:mm)")

args_parser.add_argument("-r", "--reverse", action="store", dest="reverse",
                   type=bool, required=False, default=False,
                   help="reverse date order")

args = args_parser.parse_args()