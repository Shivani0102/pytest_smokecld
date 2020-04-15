from appium import webdriver
import subprocess
import os
import pytest
from pathlib import Path
import time
from selenium.webdriver import ActionChains
from testrail import *
from allure_commons.types import AttachmentType
import allure
import test_assaycld
# from robot.libraries.BuiltIn import BuiltIn
# import SeleniumLibrary
import timeit
from selenium.webdriver.common.keys import Keys


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            # print("inside if")
            test_assaycld.case_fields()
            test_assaycld.Time()

            if test_assaycld.update_testrail == True:
                # print("yes true")
                test_assaycld.fail_update()
            else:
                print("not true")

        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))

    if rep.when == 'call' and rep.passed:
        test_assaycld.stop()
        if test_assaycld.update_testrail == True:
            test_assaycld.pass_update()


@pytest.fixture(scope='module', autouse=True)
def teardown_module():
    yield
    test_assaycld.teardwn()


@pytest.fixture(scope="function")
def driver():
    appdata = os.getenv('APPDATA')
    # try:
    #     if os.path.isfile(appdata + "\Assay Analyzer 2.0\D37712\CLD.History.xml"):
    #         os.remove(appdata + "\Assay Analyzer 2.0\D37712\CLD.History.xml")
    # except:
    #     print("history file not found")
    try:
        if os.path.isfile(appdata + "\Assay Analyzer 2.0\D37712\Pens states.dat"):
            os.remove(appdata + "\Assay Analyzer 2.0\D37712\Pen States.dat")
    except:
        print("penstates file not found")

    try:
        if os.path.isfile(appdata + "\Assay Analyzer 2.0\D37712\CustomParameters.dat"):
            os.remove(appdata + "\Assay Analyzer 2.0\D37712\CustomParameters.dat")
    except:
        print("customparam file not found")

    desktop = str(os.path.join(Path.home(), "Desktop\D54823"))
    try:
        if os.path.isfile(desktop + "\Assay Analyzer Version 20191129.2.json"):
            os.remove(desktop + "\Assay Analyzer Version 20191129.2.json")
    except:
        print("json file not found")

    desktop = str(os.path.join(Path.home(), "Desktop\D37712"))
    try:
        if os.path.isfile(desktop + "\workbooktest.workbook"):
            os.remove(desktop + "\workbooktest.workbook")
    except:
        print("workbook file not found")

    path = os.getcwd() + "/open_tejas.bat"
    subprocess.call(path)
    desired_caps = {}
    desired_caps["app"] = "Root"
    global driver
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        desired_capabilities=desired_caps)
    driver.implicitly_wait(60)

    tejasWindow = driver.find_element_by_accessibility_id("AutomationId_MainWindow")
    print(tejasWindow)
    windowHandle = tejasWindow.get_attribute("NativeWindowHandle")
    print(windowHandle)
    int_window = int(windowHandle)
    windowHandle = hex(int_window)
    print(windowHandle)
    new_caps = {}
    new_caps["appTopLevelWindow"] = windowHandle
    new_caps["platformName"] = "Windows"
    new_caps["deviceName"] = "WindowsPC"

    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        desired_capabilities=new_caps)
    driver.implicitly_wait(10)
    yield driver
    # verify = driver.find_element_by_name("ASSAY ANALYZER 2.0").is_displayed()
    # return verify
