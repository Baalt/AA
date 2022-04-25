class BetPrinter:
    def __init__(self,
                 big_match_data: dict,
                 big_data_percent: float,
                 last_year_percent: float,
                 similar_percent: float,
                 last_20_percent: float,
                 last_12_percent: float,
                 last_8_percent: float,
                 last_4_percent: float,
                 coeff_total: float,
                 coeff_value: float,
                 rate_direction: str,
                 ord_or_exp):

        self.big_data_percent = big_data_percent
        self.last_year_percent = last_year_percent
        self.similar_percent = similar_percent
        self.last_20_percent = last_20_percent
        self.last_12_home_away_percent = last_12_percent
        self.last_8_percent = last_8_percent
        self.last_4_percent = last_4_percent

        self.big_match_data = big_match_data
        self.coeff_total = coeff_total
        self.coeff_value = coeff_value
        self.rate_direction = rate_direction
        self.ord_or_exp = ord_or_exp

    def print_rate(self):
        print(f"""
        Football match: {self.big_match_data['home_command_name']} - {self.big_match_data['away_command_name']} 
        
        Rate Type:____________________ {'Part for combine rate'  if self.ord_or_exp > 87 else 'Single rate'}
        Bet:__________________________ {self.coeff_total} {self.rate_direction}  
        Coefficient:__________________ {self.coeff_value}

        Big Data:_____________________ {self.big_data_percent}%
        Last Year:____________________ {self.last_year_percent}%
        Similar Games:________________ {self.similar_percent}%
        Last 20 Games:________________ {self.last_20_percent}%
        Last 12 Home-Away Games:______ {self.last_12_home_away_percent}%
        Last 8 Games:_________________ {self.last_8_percent}%
        Last 4 Games:_________________ {self.last_4_percent}%

        {self.big_match_data['home_command_name']} 
        Trainer Name: {self.big_match_data['home_trainer']['trainer_name']}
        Games with current trainer: {self.big_match_data['home_trainer']['count_games_with_command_home_trainer_trainer']}

        {self.big_match_data['away_command_name']} 
        Trainer Name: {self.big_match_data['away_trainer']['trainer_name']}
        Games with current trainer: {self.big_match_data['away_trainer']['count_games_with_command_home_trainer_trainer']}
        """)
