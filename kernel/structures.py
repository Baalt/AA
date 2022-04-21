class HomeDataStructure:
    def __init__(self):
        # big data home-away
        self.big_data_total_current_home_in_home_away_games = list()
        self.big_data_individual_total_current_home_in_home_away_games = list()
        self.big_data_individual_total_opposing_teams_current_home_in_home_away_games = list()

        # last year home-away
        self.last_year_total_current_home_command_in_home_away_games = list()
        self.last_year_individual_total_current_home_command_in_home_away_games = list()
        self.last_year_individual_total_opposing_teams_current_home_in_home_away_games = list()

        # last20 home-away games
        self.last_20_games_total_current_home_by_year_in_home_away_games = None
        self.last_20_games_individual_total_current_home_by_year_in_home_away_games = None
        self.last_20_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games = None

        # last12 home games
        self.last_12_games_total_current_home_command_by_year_in_home_games = list()
        self.last_12_games_individual_total_current_home_by_year_in_home_games = list()
        self.last_12_games_individual_total_opposing_teams_current_home_by_year_in_away_games = list()

        # last8 home-away games
        self.last_8_games_total_current_home_by_year_in_home_away_games = None
        self.last_8_games_individual_total_current_home_by_year_in_home_away_games = None
        self.last_8_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games = None

        # last4 home-away games
        self.last_4_games_total_current_home_by_year_in_home_away_games = None
        self.last_4_games_individual_total_current_home_by_year_in_home_away_games = None
        self.last_4_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games = None


class AwayDataStructure:
    def __init__(self):
        # big data home-away
        self.big_data_total_current_away_in_home_away_games = list()
        self.big_data_individual_total_current_away_in_home_away_games = list()
        self.big_data_individual_total_opposing_teams_current_away_in_home_away_games = list()

        # last year home-away
        self.last_year_total_current_away_command_in_home_away_games = list()
        self.last_year_individual_total_current_away_command_in_home_away_games = list()
        self.last_year_individual_total_opposing_teams_current_away_command_in_home_away_games = list()

        # last20 home-away games
        self.last_20_games_total_current_away_by_year_in_home_away_games = None
        self.last_20_games_individual_total_current_away_by_year_in_home_away_games = None
        self.last_20_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games = None

        # last12 away games
        self.last_12_games_total_current_away_command_by_year_in_away_games = list()
        self.last_12_games_individual_total_current_away_by_year_in_away_games = list()
        self.last_12_games_individual_total_opposing_teams_current_away_by_year_in_home_games = list()

        # last8 home-away games
        self.last_8_games_total_current_away_by_year_in_home_away_games = None
        self.last_8_games_individual_total_current_away_by_year_in_home_away_games = None
        self.last_8_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games = None

        # last4 home-away games
        self.last_4_games_total_current_away_by_year_in_home_away_games = None
        self.last_4_games_individual_total_current_away_by_year_in_home_away_games = None
        self.last_4_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games = None
