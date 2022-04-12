from datetime import datetime


class MatchDataNormalize:
    def __init__(self, season: str, day_month: str):
        self.season = season
        self.day_month = day_month

    def convert_season_to_dmY(self):
        season_and_year = self.season.split()
        if len(season_and_year) == 2:
            year_or_years = self.strip_year(season_and_year[-1])
            if len(year_or_years) == 2:
                first_half_season_year, second_half_season_year = year_or_years
                second_half_season_year = '20' + second_half_season_year

                return self.determine_the_year_by_the_month_of_the_season(first_half_season_year=first_half_season_year,
                                                                          second_half_season_year=second_half_season_year)
            elif isinstance(year_or_years, str):
                return f'{self.day_month}.{year_or_years}'

    def strip_year(self, year: str) -> str:
        return year.strip('()') if '/' not in year else year.strip('()').split('/')

    def determine_the_year_by_the_month_of_the_season(self,
                                                      first_half_season_year: str,
                                                      second_half_season_year: str):
        match_date = datetime.strptime(self.day_month, "%d.%m")
        if match_date.month in range(1, 7):
            return f'{self.day_month}.{second_half_season_year}'
        if match_date.month in range(7, 13):
            return f'{self.day_month}.{first_half_season_year}'


if __name__ == '__main__':
    print(MatchDataNormalize(season='ITA1\n                (2021)', day_month='13.08').convert_season_to_dmY())
