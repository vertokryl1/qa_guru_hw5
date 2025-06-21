import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1200
    browser.config.window_height = 1024
    yield
    browser.quit()
