from selenium.webdriver.common.by import By

from browser.head import Browser


class Button:
    def __init__(self, browser: Browser):
        self.browser = browser

    @property
    def update_button(self):
        UPDATE_BUTTON_XPATH = '//button[@class="btn btn-sm btn-success w-100 my-1 mt-2"]'
        update_button = self.browser.firefox.find_element(By.XPATH, UPDATE_BUTTON_XPATH)

        return update_button

    @property
    def statistic_buttons(self):
        STATISTIC_BUTTONS_XPATH = '//div[@class="btn-group stat-picker-desktop"]' \
                                  '/button[contains(@class, "btn btn-sm btn-light"]'
        statistic_buttons = self.browser.firefox.find_elements(By.XPATH, STATISTIC_BUTTONS_XPATH)

        return statistic_buttons


class LeagueButtons(Button):
    pass


class MatchButtons(Button):
    @property
    def quantity_of_matches_button(self):
        QUANTITY_OF_MATCHES_INPUT_XPATH = '//input[@class="manual-howmuch-input"]'
        QUANTITY_OF_MATCHES_BUTTON_XPATH = '//div[contains(@class, "last_matches_limit-picker")]' \
                                           '/button[last()]'

        quantity_of_matches_input = self.browser.firefox.find_element(By.XPATH,
                                                                      value=QUANTITY_OF_MATCHES_INPUT_XPATH)
        quantity_of_matches_button = self.browser.firefox.find_element(By.XPATH,
                                                                       value=QUANTITY_OF_MATCHES_BUTTON_XPATH)

        return quantity_of_matches_input, quantity_of_matches_button

    @property
    def teams_season_buttons_all(self):
        SEASON_HOME_BUTTON_ALL_XPATH = '(//div[@id="teamsSeasons"])[1]/' \
                                       'button[last()]'
        SEASON_AWAY_BUTTON_ALL_XPATH = '(//div[@id="teamsSeasons"])[2]' \
                                       '/button[last()]'

        season_home_button_all = self.browser.firefox.find_element(By.XPATH,
                                                                   value=SEASON_HOME_BUTTON_ALL_XPATH)
        season_away_button_all = self.browser.firefox.find_element(By.XPATH,
                                                                   value=SEASON_AWAY_BUTTON_ALL_XPATH)

        return season_home_button_all, season_away_button_all

    def current_league_command_buttons(self, league: str):
        CURRENT_HOME_LEAGUE_XPATH = f'(//div[@id="refCompetitions"])[1]' \
                                    f'/button[normalize-space(text())=\'{league}\']'
        CURRENT_AWAY_LEAGUE_XPATH = f'(//div[@id="refCompetitions"])[2]' \
                                    f'/button[normalize-space(text())=\'{league}\']'

        current_league_home_command_button = self.browser.firefox.find_element(By.XPATH,
                                                                               value=CURRENT_HOME_LEAGUE_XPATH)
        current_league_away_command_button = self.browser.firefox.find_element(By.XPATH,
                                                                               value=CURRENT_AWAY_LEAGUE_XPATH)

        return current_league_home_command_button, current_league_away_command_button

    def coefficient_button(self):
        COEFFICIENT_BUTTON_XPATH = '//a[@class="nav-link accent-hvr cursor-pointer"]' \
                                   '/span[normalize-space(text())="Коэффициенты"]'

        coefficient_button = self.browser.firefox.find_element(By.XPATH,
                                                               COEFFICIENT_BUTTON_XPATH)

        return coefficient_button


if __name__ == '__main__':
    pass
