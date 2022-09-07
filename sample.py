import os
from bkgcheck import BackgroundCheckAPI 

def main():
    os.environ["BCGCHK_APP_ID"] = "pra-3553c360"
    os.environ["BCGCHK_APP_KEY"] = "281fe817d95aa08bed1a75e05a56b1cd"
    api = BackgroundCheckAPI()
    api.check_by_name("Stanford", first="Neal Anderson", state= "Washington", county="Benton")

if __name__ == "__main__":
    main()