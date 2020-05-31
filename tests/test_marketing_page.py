import scenarios
from pages.marketing_page import MarketingPage


class TestMarketingPage:

    def test_should_change_subsystem(self, browser):
        scenarios.marketing_scenario(browser)
        marketing_page = MarketingPage(browser, browser.current_url)
        marketing_page.open_submenu()
        marketing_page.change_subsystem()

    def test_should_exit_system(self, browser):
        scenarios.marketing_scenario(browser)
        marketing_page = MarketingPage(browser, browser.current_url)
        marketing_page.open_submenu()
        marketing_page.exit_system()
