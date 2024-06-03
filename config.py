import os
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from utils import file

context = os.getenv('CONTEXT', 'local_emulator')

load_dotenv(file.abs_path_from_project(f'.env.{context}'))

runs_on_bstack = (context == 'bstack')
if runs_on_bstack:
    load_dotenv(file.abs_path_from_project(f'.env.credentials'))

remote_url = os.getenv('URL_WD_HUB')
appWaitActivity = os.getenv('APP_WAIT_ACTIVITY')

app = os.getenv('APP_STRING')
if app.startswith('./'):
    app = file.abs_path_from_project(app)

hub_timeout = os.getenv('HUB_TIMEOUT', 15.0)


def to_driver_options():
    options = UiAutomator2Options()
    options.set_capability('app', app)
    options.set_capability('appWaitActivity', appWaitActivity)

    if runs_on_bstack:
        bstackUserName = os.getenv('BS_USERNAME')
        bstackAccessKey = os.getenv('BS_ACCESSKEY')
        platformVersion = os.getenv('PLATFORM_VERSION')
        deviceName = os.getenv('DEVICE_NAME')

        options.set_capability('deviceName', deviceName)
        options.set_capability('platformVersion', platformVersion)
        options.set_capability(
            'bstack:options', {
                'projectName': 'homework_19',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',

                'userName': bstackUserName,
                'accessKey': bstackAccessKey,
            },
        )

    return options
