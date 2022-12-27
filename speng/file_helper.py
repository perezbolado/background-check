from wsgiref.util import request_uri
import pandas as pd
import re

class FileHelper():
    def __init__(self, path):
        self.load_file(path)

    def load_file(self, file_path):
        self.df = pd.read_csv(file_path)
    
    def get_teams(self):
        col1_Teams = self.df['Team1_ID'].tolist()
        col2_Teams = self.df['Team2_ID'].tolist()
        teams = list(set(col1_Teams + col2_Teams))
        teams = [ x for x in teams if isinstance(x, str)]
        return teams

    def get_naming_convention_mapping(self, year, team_regex):
        teams = self.get_teams()
        prog = re.compile(team_regex)
        map = {}
        for team in teams:
            result = prog.match(team)
            assert len(result.regs) == 3
            map[team] = "{}-{:0>2}-{}".format(result[1],result[2], year)
        return map

    def fix_team_name(self, year, team_regex):
        map = self.get_naming_convention_mapping(year, team_regex)
        games_df = self.df[self.df.Event_Type == "Game" ]
        games_df["Team1_ID"] = games_df ["Team1_ID"].apply(lambda x: map[x] )
        games_df["Team2_ID"] = games_df ["Team2_ID"].apply(lambda x: map[x] )
        events_df = self.df[self.df.Event_Type == "Event" ]
        events_df["Tags"] = events_df["Tags"].apply(lambda x: map[x] )
        concat = pd.concat([games_df, events_df], axis=0)
        return concat


    
        

