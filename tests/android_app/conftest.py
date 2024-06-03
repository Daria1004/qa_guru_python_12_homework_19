import allure
import config
import pytest
import allure_commons
from selene import browser, support
from appium import webdriver
from utils import utils_allure


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = config.to_driver_options()

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            config.remote_url,
            options=options
        )

    browser.config.timeout = float(config.hub_timeout)

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    utils_allure.attach_screenshot()
    utils_allure.attach_xml_dump()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    if config.runs_on_bstack:
        utils_allure.attach_bstack_videonpm(session_id)
