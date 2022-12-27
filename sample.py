from operator import ge
import os
from bkgcheck import BackgroundCheckAPI
from speng import SportsEngineAPI
from speng import FileHelper
import re

def call_backgroundcheck():
    os.environ["BCGCHK_APP_ID"] = ""
    os.environ["BCGCHK_APP_KEY"] = ""
    api = BackgroundCheckAPI()
    api.check_by_name("", first="", state= "", county="")

def call_mapping():
    api = SportsEngineAPI()
    response = api.get_mapping_index()
    print(response)

def replace_names():
    fh = FileHelper("data/coed-2022.csv")
    teams_regex = "(^[\D]*)(\d)"
    df = fh.fix_team_name(22,teams_regex)
    df.to_csv("data/coed-2022-updated.csv")


def main():
    replace_names()
    

if __name__ == "__main__":
    main()