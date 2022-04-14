from bs4 import BeautifulSoup


class ScraperMethods:
    def scrap_statistic_name(self, soup: BeautifulSoup, tooltip=False) -> str:
        button_class = 'btn btn-sm btn-light active'
        if tooltip:
            button_class = button_class + ' has-tooltip'

        current_statistic_button_name = soup.find(
            'button', attrs={'class': button_class}
        ).get_text(strip=True)

        return current_statistic_button_name


