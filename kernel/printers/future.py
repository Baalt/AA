class BetPrinter:
    def __init__(self,
                 statistic_name: str,
                 league_name: str,
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
                 category: str):
        self.statistic_name = statistic_name
        self.league_name = league_name
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
        self.category = category

    def print_rate(self):
        print(f"""
        League:_______________________ {self.league_name}
        Football match:_______________ {self.big_match_data['home_command_name']} - {self.big_match_data['away_command_name']}
        Category:_____________________ {self.category}
        
        Statistic Name:_______________ {self.statistic_name}
        Rate Type:____________________ {'Part for combine rate' if float(self.coeff_value) < 1.683 else 'Single rate'}
        Bet:__________________________ {self.coeff_total} {self.rate_direction}  
        Coefficient:__________________ {self.coeff_value}

        Big Data:_____________________ {self.big_data_percent}%
        Last Year:____________________ {self.last_year_percent}%
        Similar Games:________________ {self.similar_percent}%
        Last 20 Games:________________ {self.last_20_percent}%
        Last 12 Home-Away Games:______ {self.last_12_home_away_percent}%
        Last 8 Games:_________________ {self.last_8_percent}%
        Last 4 Games:_________________ {self.last_4_percent}%               
        """)


class TrainerPrinter:
    def __init__(self, big_match_data: dict):
        self.big_match_data = big_match_data

    def print_trainer_info(self):
        try:
            print(f"""
            'Home command:________________ {self.big_match_data['home_command_name']}
            'Home command trainer:________ {self.big_match_data['home_trainer']['trainer_name']}
            'Count of games with command:_ {self.big_match_data['home_trainer']['count_games_with_command_home_trainer']}
            """)

        except Exception as err:
            print('HOME TRAINER INFO ERROR: ', err)

        try:
            print(f"""
            'Away command:________________ {self.big_match_data['away_command_name']}
            'Away command trainer:________ {self.big_match_data['away_trainer']['trainer_name']}
            'Count of games with command:_ {self.big_match_data['away_trainer']['count_games_with_command_away_trainer']}
            """)

        except Exception as err:
            print('AWAY TRAINER INFO ERROR: ', err)
