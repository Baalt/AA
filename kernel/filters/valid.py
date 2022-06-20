from kernel.errors import ValidStructureError
from kernel.structures import HomeDataStructure, AwayDataStructure


class ValidStructureFilter:
    def __init__(self, home_structure: HomeDataStructure, away_structure: AwayDataStructure):
        self.home_structure = home_structure
        self.away_structure = away_structure

    def valid_and_create(self):
        if self.is_home_structure_valid() and self.is_away_structure_valid():
            self.adding_home_structures_for_the_latest_games()
            self.adding_away_structures_for_the_latest_games()
            # test mode
            # self.home_valid_structure_print()
            # self.away_valid_structure_print()

    def adding_home_structures_for_the_latest_games(self):
        # last20 home-away games
        self.home_structure.last_20_games_total_current_home_by_year_in_home_away_games = \
            self.home_structure.last_year_total_current_home_command_in_home_away_games[:20]

        self.home_structure.last_20_games_individual_total_current_home_by_year_in_home_away_games = \
            self.home_structure.last_year_individual_total_current_home_command_in_home_away_games[:20]

        self.home_structure.last_20_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games = \
            self.home_structure.last_year_individual_total_opposing_teams_current_home_in_home_away_games[
            :20]
        # last8 home-away games
        self.home_structure.last_8_games_total_current_home_by_year_in_home_away_games = \
            self.home_structure.last_year_total_current_home_command_in_home_away_games[:8]

        self.home_structure.last_8_games_individual_total_current_home_by_year_in_home_away_games = \
            self.home_structure.last_year_individual_total_current_home_command_in_home_away_games[:8]

        self.home_structure.last_8_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games = \
            self.home_structure.last_year_individual_total_current_home_command_in_home_away_games[:8]
        # last4 home-away games
        self.home_structure.last_4_games_total_current_home_by_year_in_home_away_games = \
            self.home_structure.last_year_total_current_home_command_in_home_away_games[:4]

        self.home_structure.last_4_games_individual_total_current_home_by_year_in_home_away_games = \
            self.home_structure.last_year_individual_total_current_home_command_in_home_away_games[:4]

        self.home_structure.last_4_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games = \
            self.home_structure.last_year_individual_total_opposing_teams_current_home_in_home_away_games[:4]

    def adding_away_structures_for_the_latest_games(self):
        # last20 home-away games
        self.away_structure.last_20_games_total_current_away_by_year_in_home_away_games = \
            self.away_structure.last_year_total_current_away_command_in_home_away_games[:20]

        self.away_structure.last_20_games_individual_total_current_away_by_year_in_home_away_games = \
            self.away_structure.last_year_individual_total_current_away_command_in_home_away_games[:20]

        self.away_structure.last_20_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games = \
            self.away_structure.last_year_individual_total_opposing_teams_current_away_in_home_away_games[
            :20]
        # last8 home-away games
        self.away_structure.last_8_games_total_current_away_by_year_in_home_away_games = \
            self.away_structure.last_year_total_current_away_command_in_home_away_games[:8]

        self.away_structure.last_8_games_individual_total_current_away_by_year_in_home_away_games = \
            self.away_structure.last_year_individual_total_current_away_command_in_home_away_games[:8]

        self.away_structure.last_8_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games = \
            self.away_structure.last_year_individual_total_opposing_teams_current_away_in_home_away_games[:8]
        # last4 home-away games
        self.away_structure.last_4_games_total_current_away_by_year_in_home_away_games = \
            self.away_structure.last_year_total_current_away_command_in_home_away_games[:4]

        self.away_structure.last_4_games_individual_total_current_away_by_year_in_home_away_games = \
            self.away_structure.last_year_individual_total_current_away_command_in_home_away_games[:4]

        self.away_structure.last_4_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games = \
            self.away_structure.last_year_individual_total_opposing_teams_current_away_in_home_away_games[:4]

    def home_valid_structure_print(self):
        print('home big data')
        print(self.home_structure.big_data_total_current_home_in_home_away_games)
        print(self.home_structure.big_data_individual_total_current_home_in_home_away_games)
        print(
            self.home_structure.big_data_individual_total_opposing_teams_current_home_in_home_away_games)
        print('home by year')
        print(self.home_structure.last_year_total_current_home_command_in_home_away_games)
        print(self.home_structure.last_year_individual_total_current_home_command_in_home_away_games)
        print(
            self.home_structure.last_year_individual_total_opposing_teams_current_home_in_home_away_games)
        print('home similar')
        print(self.home_structure.similar_command_total_current_home_big_data_home_away_games)
        print(self.home_structure.similar_command_individual_total_current_home_command_in_home_away_games)
        print(self.home_structure.similar_command_individual_total_opposing_teams_current_home_in_home_away_games)
        print('home last 20')
        print(self.home_structure.last_20_games_total_current_home_by_year_in_home_away_games)
        print(
            self.home_structure.last_20_games_individual_total_current_home_by_year_in_home_away_games)
        print(
            self.home_structure.last_20_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games)
        print('last home games by year')
        print(self.home_structure.last_12_games_total_current_home_command_by_year_in_home_games)
        print(self.home_structure.last_12_games_individual_total_current_home_by_year_in_home_games)
        print(
            self.home_structure.last_12_games_individual_total_opposing_teams_current_home_by_year_in_away_games)
        print('home last8')
        print(self.home_structure.last_8_games_total_current_home_by_year_in_home_away_games)
        print(self.home_structure.last_8_games_individual_total_current_home_by_year_in_home_away_games)
        print(self.home_structure.last_8_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games)
        print('home last4')
        print(self.home_structure.last_4_games_total_current_home_by_year_in_home_away_games)
        print(self.home_structure.last_4_games_individual_total_current_home_by_year_in_home_away_games)
        print(
            self.home_structure.last_4_games_individual_total_opposing_teams_current_home_by_year_in_home_away_games)

    def away_valid_structure_print(self):
        print('away big data')
        print(self.away_structure.big_data_total_current_away_in_home_away_games)
        print(self.away_structure.big_data_individual_total_current_away_in_home_away_games)
        print(
            self.away_structure.big_data_individual_total_opposing_teams_current_away_in_home_away_games)
        print('away by year')
        print(self.away_structure.last_year_total_current_away_command_in_home_away_games)
        print(self.away_structure.last_year_individual_total_current_away_command_in_home_away_games)
        print(
            self.away_structure.last_year_individual_total_opposing_teams_current_away_in_home_away_games)
        print('away similar')
        print(self.away_structure.similar_command_total_current_away_big_data_home_away_games)
        print(self.away_structure.similar_command_individual_total_current_away_command_in_home_away_games)
        print(self.away_structure.similar_command_individual_total_opposing_teams_current_away_in_home_away_games)
        print('away last 20')
        print(self.away_structure.last_20_games_total_current_away_by_year_in_home_away_games)
        print(
            self.away_structure.last_20_games_individual_total_current_away_by_year_in_home_away_games)
        print(
            self.away_structure.last_20_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games)
        print('last away games by year')
        print(self.away_structure.last_12_games_total_current_away_command_by_year_in_away_games)
        print(self.away_structure.last_12_games_individual_total_current_away_by_year_in_away_games)
        print(
            self.away_structure.last_12_games_individual_total_opposing_teams_current_away_by_year_in_home_games)
        print('away last8')
        print(self.away_structure.last_8_games_total_current_away_by_year_in_home_away_games)
        print(self.away_structure.last_8_games_individual_total_current_away_by_year_in_home_away_games)
        print(self.away_structure.last_8_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games)
        print('away last4')
        print(self.away_structure.last_4_games_total_current_away_by_year_in_home_away_games)
        print(self.away_structure.last_4_games_individual_total_current_away_by_year_in_home_away_games)
        print(self.away_structure.last_4_games_individual_total_opposing_teams_current_away_by_year_in_home_away_games)

    def is_home_structure_valid(self):
        if self.home_structure:
            if len(self.home_structure.last_year_total_current_home_command_in_home_away_games) == len(
                    self.home_structure.last_year_individual_total_current_home_command_in_home_away_games) == len(
                self.home_structure.last_year_individual_total_opposing_teams_current_home_in_home_away_games):

                if len(self.home_structure.last_12_games_total_current_home_command_by_year_in_home_games) == len(
                        self.home_structure.last_12_games_individual_total_current_home_by_year_in_home_games) == len(
                    self.home_structure.last_12_games_individual_total_opposing_teams_current_home_by_year_in_away_games):

                    if len(self.home_structure.last_year_total_current_home_command_in_home_away_games) >= 20 and len(
                            self.home_structure.last_12_games_total_current_home_command_by_year_in_home_games) >= 12 and \
                            len(self.home_structure.similar_command_total_current_home_big_data_home_away_games) > 8:
                        return True

                    raise ValidStructureError(
                        f"""ValidStructureError address -- kernel/filters/valid/ValidStructureFilter.is_home_structure_valid(
                            Insufficient number of matches in HOME structures to start analysis
                            length last year of games must be >= 20 -- {len(self.home_structure.last_year_total_current_home_command_in_home_away_games)}
                            length last 12 of games must be >= 12 -- {len(self.home_structure.last_12_games_total_current_home_command_by_year_in_home_games)}
                            length similar games must be >= 8 -- {len(self.home_structure.similar_command_total_current_home_big_data_home_away_games)}""")

                raise ValidStructureError(
                    f"""Mismatch of last 12 home structures, must be the same length
                        len of last 12 home structure -- {len(self.home_structure.last_12_games_total_current_home_command_by_year_in_home_games)}
                        len of last 12 ind home structure -- {len(self.home_structure.last_12_games_individual_total_current_home_by_year_in_home_games)}
                        len of last 12 opposing home structure -- {len(self.home_structure.last_12_games_individual_total_opposing_teams_current_home_by_year_in_away_games)}""")

            raise ValidStructureError(
                f"""Mismatch of last year home structures, must be the same length
                    len of last year home structure -- {len(self.home_structure.last_year_total_current_home_command_in_home_away_games)}
                    len of last year ind home structure -- {len(self.home_structure.last_year_individual_total_current_home_command_in_home_away_games)}
                    len of last year opposing home structure -- {len(self.home_structure.last_year_individual_total_opposing_teams_current_home_in_home_away_games)}""")
        raise ValidStructureError(f'Home structure error -- {self.home_structure}')

    def is_away_structure_valid(self):
        if self.away_structure:
            if len(self.away_structure.last_year_total_current_away_command_in_home_away_games) == len(
                    self.away_structure.last_year_individual_total_current_away_command_in_home_away_games) == len(
                self.away_structure.last_year_individual_total_opposing_teams_current_away_in_home_away_games):

                if len(self.away_structure.last_12_games_total_current_away_command_by_year_in_away_games) == len(
                        self.away_structure.last_12_games_individual_total_current_away_by_year_in_away_games) == len(
                    self.away_structure.last_12_games_individual_total_opposing_teams_current_away_by_year_in_home_games):

                    if len(self.away_structure.last_year_total_current_away_command_in_home_away_games) >= 20 and len(
                            self.away_structure.last_12_games_total_current_away_command_by_year_in_away_games) >= 12 and \
                            len(self.away_structure.similar_command_total_current_away_big_data_home_away_games) > 8:
                        return True

                    raise ValidStructureError(
                        f"""ValidStructureError address - kernel/filters/valid/ValidStructureFilter.is_away_structure_valid()
                            Insufficient number of matches in AWAY structures to start analysis
                            length last year of games must be >= 20 -- {len(self.away_structure.last_year_total_current_away_command_in_home_away_games)}
                            length last 12 of games must be >= 12 -- {len(self.away_structure.last_12_games_total_current_away_command_by_year_in_away_games)}
                            length similar games must be >= 8 -- {len(self.away_structure.similar_command_total_current_away_big_data_home_away_games)}""")

                raise ValidStructureError(
                    f"""Mismatch of last 12 away structures, must be the same length
                        len of last 12 away structure -- {len(self.away_structure.last_12_games_total_current_away_command_by_year_in_away_games)}
                        len of last 12 ind away structure -- {len(self.away_structure.last_12_games_individual_total_current_away_by_year_in_away_games)}
                        len of last 12 opposing away structure -- {len(self.away_structure.last_12_games_individual_total_opposing_teams_current_away_by_year_in_home_games)}""")
            raise ValidStructureError(
                f"""Mismatch of away structures, must be the same length
                    len of last year away structure -- {len(self.away_structure.last_year_total_current_away_command_in_home_away_games)}
                    len of last year ind away structure -- {len(self.away_structure.last_year_individual_total_current_away_command_in_home_away_games)}
                    len of last year opposing away structure -- {len(self.away_structure.last_year_individual_total_opposing_teams_current_away_in_home_away_games)}""")
        raise ValidStructureError(f'Home structure error -- {self.away_structure}')
