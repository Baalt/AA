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


class KushPrinter(BetPrinter):
    def __init__(self, statistic_name: str, league_name: str, big_match_data: dict,
                 big_data_percent: float, last_year_percent: float, similar_percent: float,
                 last_20_percent: float, last_12_percent: float, last_8_percent: float, last_4_percent: float,
                 coeff_total: float, coeff_value: float, rate_direction: str, category: str,
                 big_data_kush_by_rate: float, last_year_kush_by_rate, similar_kush_by_rate: float,
                 last_20_kush_by_rate: float, last_12_kush_by_rate,
                 last_8_kush_by_rate: float, last_4_kush_by_rate: float):
        super().__init__(statistic_name, league_name, big_match_data, big_data_percent, last_year_percent,
                         similar_percent, last_20_percent, last_12_percent, last_8_percent, last_4_percent, coeff_total,
                         coeff_value, rate_direction, category)

        self.big_data_kush_by_rate = big_data_kush_by_rate
        self.last_year_kush_by_rate = last_year_kush_by_rate
        self.similar_kush_by_rate = similar_kush_by_rate
        self.last_20_kush_by_rate = last_20_kush_by_rate
        self.last_12_kush_by_rate = last_12_kush_by_rate
        self.last_8_kush_by_rate = last_8_kush_by_rate
        self.last_4_kush_by_rate = last_4_kush_by_rate

    def print_rate(self):
        print(f"""
         ###############################################################################################################
         League:_______________________ {self.league_name}
         Football match:_______________ {self.big_match_data['home_command_name']} - {self.big_match_data['away_command_name']}
         Category:_____________________ {self.category}

         Statistic Name:_______________ {self.statistic_name}
         Rate Type:____________________ {'Part for combine rate' if float(self.coeff_value) < 1.683 else 'Single rate'}
         Bet:__________________________ {self.coeff_total} {self.rate_direction}  
         Coefficient:__________________ {self.coeff_value}
         
         Big Data K_by_R:______________ {self.big_data_kush_by_rate} $kush$
         Last Year K_by_R:_____________ {self.last_year_kush_by_rate} $kush$
         Similar Games K_by_R:_________ {self.similar_kush_by_rate} $kush$
         Last 20 Games K_by_R:_________ {self.last_20_kush_by_rate} $kush$
         Last 12 Home-Away K_by_R:_____ {self.last_12_kush_by_rate} $kush$
         Last 8 Games K_by_R:__________ {self.last_8_kush_by_rate} $kush$
         Last 4 Games K_by_R:__________ {self.last_4_kush_by_rate} $kush$               


         Big Data:_____________________ {self.big_data_percent} %
         Last Year:____________________ {self.last_year_percent} %
         Similar Games:________________ {self.similar_percent} %
         Last 20 Games:________________ {self.last_20_percent} %
         Last 12 Home-Away Games:______ {self.last_12_home_away_percent} %
         Last 8 Games:_________________ {self.last_8_percent} %
         Last 4 Games:_________________ {self.last_4_percent} %               
             """)


class TrainerPrinter:
    def __init__(self, big_match_data: dict):
        self.big_match_data = big_match_data

    def print_trainer_info(self):
        try:
            print(f"""
        Home command:________________ {self.big_match_data['home_command_name']}
        Home command trainer:________ {self.big_match_data['home_trainer']['trainer_name']}
        Count of games with command:_ {self.big_match_data['home_trainer']['count_games_with_command_home_trainer']}
            """)

        except Exception:
            try:
                print(f"""
        Home command:________________ {self.big_match_data['home_command_name']}
        Home command trainer:________ {self.big_match_data['home_trainer']['trainer_name']}
        Count of games with command:_ {self.big_match_data['home_trainer']['count_games_with_command']}
                    """)

            except Exception as err:
                print('HOME TRAINER INFO ERROR: ', err)

        try:
            print(f"""
        Away command:________________ {self.big_match_data['away_command_name']}
        Away command trainer:________ {self.big_match_data['away_trainer']['trainer_name']}
        Count of games with command:_ {self.big_match_data['away_trainer']['count_games_with_command_away_trainer']}
            """)

        except Exception:
            try:
                print(f"""
        Away command:________________ {self.big_match_data['away_command_name']}
        Away command trainer:________ {self.big_match_data['away_trainer']['trainer_name']}
        Count of games with command:_ {self.big_match_data['away_trainer']['count_games_with_command']}
                    """)
            except Exception as err:
                print('AWAY TRAINER INFO ERROR: ', err)


class LeaderBoardPrinter:
    def __init__(self, all_league_data: dict):
        self.all_league_data = all_league_data

    def show_league_table(self):
        print('GOALS')
        print('№_', 'Command Name                  ', 'games count', 'points', 'total|individual|opposing')
        try:
            for command_name in self.all_league_data['Голы']:
                try:
                    points = self.all_league_data['Голы'][command_name]['points']
                    position = self.all_league_data['Голы'][command_name]['position']
                    games_count = self.all_league_data['Голы'][command_name]['games_count']
                    total = self.all_league_data['Голы'][command_name]['total']

                    print('{:>2}'.format(position),
                          '{:<30}'.format(command_name),
                          '{:>11}'.format(games_count),
                          '{:>6}'.format(points),
                          '{:>29}'.format(total))

                except KeyError as err:
                    print(err)
                    print('Error address -- LeaderBoardPrinter.show_league_table')
        except KeyError as err:
            print(err)
            print('Error address -- LeaderBoardPrinter.show_league_table')
            print('all_league_data["Голы"] is empty')

    def show_current_static_table(self, statistic_name):
        print(statistic_name)
        print('№_', 'Command Name        ', 'games count', 'total|individual|opposing')
        try:
            for command_name in self.all_league_data[statistic_name]:
                try:
                    position = self.all_league_data[statistic_name][command_name]['position']
                    games_count = self.all_league_data[statistic_name][command_name]['games_count']
                    total = self.all_league_data[statistic_name][command_name]['total']

                    print('{:>2}'.format(position),
                          '{:<20}'.format(command_name),
                          '{:>11}'.format(games_count),
                          '{:>29}'.format(total))

                except KeyError as err:
                    print(err)
                    print('Error address -- LeaderBoardPrinter.show_current_static_table')
        except KeyError as err:
            print(err)
            print('Error address -- LeaderBoardPrinter.show_current_static_table')
            print(print(f'all_league_data[{statistic_name}] is empty'))
