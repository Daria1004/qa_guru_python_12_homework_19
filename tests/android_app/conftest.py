import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
import os
from dotenv import load_dotenv
from appium import webdriver
from utils import utils_allure


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management(load_env):
    options = UiAutomator2Options().load_capabilities({
        'platformVersion': '11.0',
        'deviceName': 'Oppo A96',
        'app': os.getenv('APP_STRING'),
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',
            'userName': os.getenv('BS_USERNAME'),
            'accessKey': os.getenv('BS_ACCESSKEY'),
        }
    })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            os.getenv('URL_BROWSERSTECK'),
            options=options
        )

    browser.config.timeout = float(os.getenv('timeout', os.getenv('BS_TIMEOUT')))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    utils_allure.attach_bstack_video(session_id)
