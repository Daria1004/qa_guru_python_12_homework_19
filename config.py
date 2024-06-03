import os
from dotenv import load_dotenv

from utils import file

context = os.getenv('CONTEXT', 'local_emulator')

load_dotenv(file.abs_path_from_project(f'.env.{context}'))

if context == 'bstack':
    load_dotenv(file.abs_path_from_project(f'.env.credentials'))

remote_url = os.getenv('URL_WD_HUB', '')
deviceName = os.getenv('DEVICE_NANE')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
app = os.getenv('APP_STRING', './app-alpha-universal-release.apk')
runs_on_bstack = app.startswith('bs://')
bstackUserName = os.getenv('BS_USERNAME', '')
bstackAccessKey = os.getenv('BS_ACCESSKEY', '')
hub_timeout = os.getenv('HUB_TIMEOUT', 15.0)
platformVersion = os.getenv('PLATFORM_VERSION', '9.0')


def to_driver_options():
    from appium.options.android import UiAutomator2Options
    options = UiAutomator2Options()

    if deviceName:
        options.set_capability('deviceName', deviceName)

    if appWaitActivity:
        options.set_capability('appWaitActivity', appWaitActivity)

    options.set_capability('app', (
        app if (app.startswith('/') or app.startswith('C:') or runs_on_bstack)
        else file.abs_path_from_project(app)
    ))

    if runs_on_bstack:
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
