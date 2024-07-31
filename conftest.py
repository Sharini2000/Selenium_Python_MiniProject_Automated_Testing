import pytest
import pytest_html

from utils.screenshot import ScreenshotHelper
from pytest_html import extras

screenshot_helper = ScreenshotHelper()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('setup', None)
        if driver:
            screenshot_path = screenshot_helper.take_screenshot(driver[0], f"{item.name}_failure")
            if screenshot_path:
                report.extra = getattr(report, 'extra', [])
                report.extra.append(extras.image(screenshot_path))

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if config.pluginmanager.hasplugin('html'):
        config.option.htmlpath = config.option.htmlpath or "report.html"
        config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title = "Job Search Automation Test Report"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([pytest_html.extras.html("<p>Project: Job Search Automation</p>"), pytest_html.extras.html("<p>Tester: Sharini Rithigaa B S</p>")])
