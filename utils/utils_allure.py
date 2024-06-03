import json
import os
import allure
from selene import browser


def attach_bstack_videonpm(session_id):

    import requests
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(os.getenv('BS_USERNAME'), os.getenv('BS_ACCESSKEY')),
    ).json()

    allure.attach(
        json.dumps(bstack_session),
        name='Session data',
        attachment_type=allure.attachment_type.JSON,
    )

    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )


def attach_screenshot():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )


def attach_xml_dump():
    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )