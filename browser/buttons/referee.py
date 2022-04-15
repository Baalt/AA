from selenium.webdriver.common.by import By

from browser.buttons.match import MatchButtons


class RefereeButtons(MatchButtons):
    @property
    def open_referee_button(self):
        REFEREE_BUTTON_XPATH = '//span[contains(text(), "Рефери")]'

        referee_button = self.browser.firefox.find_element(By.XPATH,
                                                           value=REFEREE_BUTTON_XPATH)
        return referee_button

    @property
    def referee_season_button_all(self):
        SEASON_BUTTON_ALL_XPATH = '//div[@id="teamsSeasons"]/button[last()]'

        season_button_all = self.browser.firefox.find_element(By.XPATH,
                                                              value=SEASON_BUTTON_ALL_XPATH)
        return season_button_all

    def current_league_buttons(self, league: str):
        CURRENT_LEAGUE_XPATH = f'//div[@id="refCompetitions"]/button[normalize-space(text())=\'{league}\']'

        current_league_button = self.browser.firefox.find_element(By.XPATH,
                                                                  value=CURRENT_LEAGUE_XPATH)

        return current_league_button