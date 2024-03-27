import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from Utilities import ReadConfigurations


# For taking screenshot on failure
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = ReadConfigurations.read_configuration("basic info", "browser")

    driver = None
    if browser.capitalize() == "Chrome":
        driver = webdriver.Chrome()
    elif browser.capitalize() == "Firefox":
        driver = webdriver.Firefox()
    elif browser.capitalize() == "Edge":
        driver = webdriver.Edge()
    else:
        print("This is not a valid Browser.")
    driver.maximize_window()
    driver.implicitly_wait(5)
    url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()