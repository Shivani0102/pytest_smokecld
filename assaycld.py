import unittest
import zipfile
from pathlib import Path

import keyboard
from appium import webdriver
import subprocess, sys
from subprocess import Popen, PIPE
import os
import time
from os import path
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from testrail import *
from allure_commons.types import AttachmentType
import json
import allure
from lxml import etree
from robot.libraries.BuiltIn import BuiltIn
import timeit
from selenium.webdriver.common.keys import Keys


# sys.path.append(r'C:\Users\Fleek\PycharmProjects\tejastest\venv\testrail.py')


# addImagePath(common.cfgImageLibrary)

# s = Screen()
# timeout = 2

# ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
class assaycld():
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    global client
    global run_id
    run_id = None
    client = APIClient('https://berkeleylights.testrail.io/')
    client.user = 'ashish.rawat@berkeleylights.com'
    client.password = 'Fleek@2016'

    def __init__(self, driver):
        self.driver = driver

    def createTestRun(self, test_ids=[], name="Assay Analyzer 2.0 Automated Smoke Test CLD"):
        response = client.send_post(
            'add_run/2',
            {'name': name,
             'include_all': False,
             'case_ids': test_ids
             }
        )
        global run_id
        run_id = str(response["id"])

    def closeTestRun(self):
        global run_id
        response = client.send_post(
            'close_run/' + run_id,
            {}
        )

    def updateTestCase(self, testCaseId, result):
        global run_id
        if result == "pass":
            status = 1
        elif result == "fail":
            status = 5
        # else:
        # self.log.failed("Unknows Status ID for TestRail test update. Please use 'pass' or 'fail' for the tests.")
        print(testCaseId)
        print(run_id)
        response = client.send_post(
            'add_result_for_case/' + run_id + '/' + testCaseId,
            {
                'status_id': status,
                'comment': 'Test Executed - Status updated from Automated Smoke Test Suite'
            }
        )

    def capture_page_screenshot(self):
        # ul = BuiltIn().get_library_instance('SeleniumLibrary')
        # path = ul.capture_page_screenshot()
        # allure.attach.file(path, name="screenshot", attachment_type=allure.attachment_type.JPG)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        # return path

    def case_fields(self, testid):
        global run_id
        response = client.send_get(
            'get_case/' + testid
        )
        print("printing response.")
        # print json.dumps(response, sort_keys=True, indent=4)
        print("Title")
        print
        response["title"]
        print("Steps:-")
        print
        response["custom_steps"]
        print("Expected Output:")
        print
        response["custom_expected"]

    '''Testcase T35911'''

    def start_tejas(self):
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
        verify = driver.find_element_by_name("ASSAY ANALYZER 2.0").is_displayed()
        return verify

    def close(self):
        self.driver.find_element_by_accessibility_id("PART_Close").click()
        self.driver.find_element_by_accessibility_id("DiscardButton").click()
        self.driver.quit()

    '''Testcase T35912'''

    def maximize(self):
        self.driver.find_element_by_accessibility_id("PART_Max").click()
        # allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    '''Testcase T35913'''

    def logo_verify(self):
        verify = self.driver.find_element_by_accessibility_id("PART_WindowTitleThumb").is_displayed()
        return verify

    '''TestCase T35885'''

    def workbook_explorer_save(self):
        save = self.driver.find_element_by_accessibility_id("AutomationId_WorkbookExplorer_Save").is_displayed()
        return save

    def workbook_explorer_openworkbook(self):
        openworkbook = self.driver.find_element_by_accessibility_id("AutomationId_WorkbookExplorer_Open").is_displayed()
        return openworkbook

    def workbook_explorer_addchip(self):
        addchip = self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddChipFolder(s)").is_displayed()
        return addchip

    def workbook_explorer_addfilter(self):
        addfilter = self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddNewFilter").is_displayed()
        return addfilter

    def workbook_explorer_addgraph(self):
        addgraph = self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddNewGraph").is_displayed()
        return addgraph

    '''TestCase T35916

    def create_workbook_type(self):
        driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_File").click()
        driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_Settings").click()
        driver.find_element_by_name("Workbook Types").click()
        driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Add").click()
        driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_ManageWorkflowView_WorkflowName").send_keys("CLD")
        driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_ManageWorkflowView_Apply").click()
        cld = driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Item_CLD").is_displayed()
        driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Apply").click()
        return cld

    def remove_workbook_type(self):
        #driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_File").click()
        driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_File").click()
        driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_Settings").click()
        driver.find_element_by_name("Workbook Types").click()
        driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Item_CLD").click()
        driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Remove").click()
        driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Apply").click()
        time.sleep(5)'''

    '''TestCase T35917'''

    def open_workbook_type(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_File").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_NewWorkbook").click()
        self.driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_CLD").click()
        # driver.find_element_by_accessibility_id("CancelButton").click()
        verify = self.driver.find_element_by_name("CLD.").is_displayed()
        return verify

    '''TestCase T35886'''

    def add_chip(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddChipFolder(s)").click()
        time.sleep(2)
        self.driver.find_element_by_name("Desktop (pinned)").click()
        time.sleep(3)
        self.driver.find_element_by_name("D37712").click()
        time.sleep(2)
        # driver.find_element_by_accessibility_id("0").click()
        self.driver.find_element_by_accessibility_id("1").click()
        chip = self.driver.find_element_by_name("D37712").is_displayed()
        return chip

    def time_start(self):
        global start
        start = timeit.default_timer()

    def time_stop(self):
        stop = timeit.default_timer()
        execution_time = str(stop - start) + " sec"
        # print("Program Executed in " + str(execution_time))
        return execution_time

    '''TestCase T35887'''

    def verify_option_chip(self):
        global actionchains
        actionchains = ActionChains(self.driver)
        chip = self.driver.find_element_by_name("D37712")
        actionchains.context_click(chip).perform()

    def verify_timeline(self):
        timeline = self.driver.find_element_by_name("Open in Timeline").is_displayed()
        return timeline

    def verify_gallery(self):
        gallery = self.driver.find_element_by_name("Open in Gallery").is_displayed()
        return gallery

    def verify_rawdata(self):
        rawdata = self.driver.find_element_by_name("Open in Raw Data").is_displayed()
        return rawdata

    def verify_remove(self):
        remove = self.driver.find_element_by_name("Remove chip(s)").is_displayed()
        return remove

    def verify_reload(self):
        reload = self.driver.find_element_by_name("Reload chip(s)").is_displayed()
        return reload

    def verify_containing_folder(self):
        containingFolder = self.driver.find_element_by_name("Open Containing Folder").is_displayed()
        return containingFolder

    '''TestCase 750'''

    def click_filter(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddNewFilter").click()
        filter = self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder")
        verify = filter.get_attribute("Name")
        return verify

    '''TestCase 751'''

    def hide_chips(self):
        self.driver.find_element_by_accessibility_id("Expander").click()
        hide = self.driver.find_element_by_name("D50238").is_displayed()
        self.driver.find_element_by_accessibility_id("Expander").click()
        return hide

    '''TestCase T35888'''

    def open_timeline(self):
        chip = self.driver.find_element_by_name("D37712")
        actionchains = ActionChains(self.driver)
        actionchains.context_click(chip).perform()
        self.driver.find_element_by_name("Open in Timeline").click()
        time.sleep(5)
        timeline = self.driver.find_element_by_accessibility_id("AutomationId_TimeLine")
        verify = timeline.get_attribute("Name")

        return verify

    def close_timeline(self):
        actionchains = ActionChains(self.driver)
        timeline = self.driver.find_element_by_accessibility_id("AutomationId_TimeLine")
        actionchains.context_click(timeline).perform()
        self.driver.find_element_by_name("Hide").click()

    '''TestCase T35889'''

    def open_gallery(self):
        actionchains = ActionChains(self.driver)
        chip = self.driver.find_element_by_name("D37712")
        actionchains.context_click(chip).perform()
        self.driver.find_element_by_name("Open in Gallery").click()
        time.sleep(8)
        gallery = self.driver.find_element_by_accessibility_id("AutomationId_Gallery")
        verify = gallery.get_attribute("Name")
        # time.sleep(150)
        # actionchains.context_click(gallery).perform()
        # driver.find_element_by_name("Hide").click()
        return verify

    def close_gallfil(self):
        actionchains = ActionChains(self.driver)
        time.sleep(4)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery").click()
        gallery = self.driver.find_element_by_accessibility_id("AutomationId_Gallery")
        actionchains.context_click(gallery).perform()
        time.sleep(2)
        self.driver.find_element_by_name("Hide").click()

    def close_gallery(self):
        actionchains = ActionChains(self.driver)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery").click()
        gallery = self.driver.find_element_by_accessibility_id("AutomationId_Gallery")
        actionchains.context_click(gallery).perform()
        time.sleep(2)
        self.driver.find_element_by_name("Hide").click()

    '''TestCase T35890'''

    def open_raw_data(self):
        chip = self.driver.find_element_by_name("D37712")
        actionchains = ActionChains(self.driver)
        actionchains.context_click(chip).perform()
        self.driver.find_element_by_name("Open in Raw Data").click()
        time.sleep(2)
        raw = self.driver.find_element_by_accessibility_id("AutomationId_RawData")
        verify = raw.get_attribute("Name")
        # time.sleep(180)
        # actionchains.context_click(raw).perform()
        # driver.find_element_by_name("Hide").click()
        return verify

    def close_raw_data(self):
        actionchains = ActionChains(self.driver)
        raw = self.driver.find_element_by_accessibility_id("AutomationId_RawData")
        actionchains.context_click(raw).perform()
        self.driver.find_element_by_name("Hide").click()

    '''TestCase 755'''

    def remove_chip(self):
        actionchains = ActionChains(self.driver)
        chip = self.driver.find_element_by_name("D50238")
        actionchains.context_click(chip).perform()
        self.driver.find_element_by_name("Remove chip(s)").click()
        self.driver.find_element_by_accessibility_id("OKButton").click()
        try:
            a = self.driver.find_element_by_name("D50238").is_displayed()
            return a
        except:
            b = False
            return b

    '''TestCase 756'''

    def verify_save_workbook(self):
        self.driver.find_element_by_accessibility_id("AutomationId_WorkbookExplorer_Save").click()
        save = self.driver.find_element_by_accessibility_id("1")
        verify = save.get_attribute("Name")
        self.driver.find_element_by_accessibility_id("2").click()
        return verify

    '''TestCase 757'''

    def save_workbook(self):
        self.driver.find_element_by_accessibility_id("AutomationId_WorkbookExplorer_Save").click()
        self.driver.find_element_by_accessibility_id("1001").send_keys("shivam")
        self.driver.find_element_by_accessibility_id("1").click()

    '''TestCase 758'''

    def open_workbook(self):
        self.driver.find_element_by_accessibility_id("AutomationId_WorkbookExplorer_Open").click()
        self.driver.find_element_by_name("shivam.workbook").click()
        self.driver.find_element_by_accessibility_id("1").click()
        time.sleep(3)

    '''TestCase 126332'''

    def new_graph(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddNewGraph").click()
        time.sleep(2)
        graph = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder")
        verify = graph.get_attribute("Name")
        return verify

    '''Chip Timeline TestCases'''

    '''TestCase 761 '''

    def verify_chiptimeline_timeline_view(self):
        view = self.driver.find_element_by_accessibility_id("AutomationId_TimeLine_ChipTimeline").is_displayed()
        return view

    def verify_chiptimeline_matching_grid(self):
        grid = self.driver.find_element_by_accessibility_id("AutomationId_TimeLine_ChipColumns").is_displayed()
        return grid

    '''TestCase T35914'''

    def verify_data_import_templates_element(self):
        self.driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_File").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_Settings").click()
        self.driver.find_element_by_name("Data Import Template").click()

    def verify_data_import_templates_element_cld(self):
        cld = self.driver.find_element_by_name("CLD").is_displayed()
        return cld

    def verify_data_import_templates_element_add(self):
        add = self.driver.find_element_by_name("Add").is_displayed()
        return add

    def verify_data_import_templates_element_edit(self):
        edit = self.driver.find_element_by_name("Edit").is_displayed()
        return edit

    def verify_data_import_templates_element_copy(self):
        copy = self.driver.find_element_by_name("Copy").is_displayed()
        return copy

    def verify_data_import_templates_element_remove(self):
        remove = self.driver.find_element_by_name("Remove").is_displayed()
        return remove

    def verify_data_import_templates_element_import(self):
        imp = self.driver.find_element_by_name("Import").is_displayed()
        return imp

    def verify_data_import_templates_element_export(self):
        export = self.driver.find_element_by_name("Export").is_displayed()
        self.driver.find_element_by_name("Cancel").click()
        return export

    '''TestCase T35915'''

    def verify_workbook_type_element(self):
        self.driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_File").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_Settings").click()
        self.driver.find_element_by_name("Workbook Types").click()

    def verify_workbook_type_element_custom(self):
        custom = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Item_Custom").is_displayed()
        return custom

    def verify_workbook_type_element_add(self):
        add = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Add").is_displayed()
        return add

    def verify_workbook_type_element_edit(self):
        edit = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Edit").is_displayed()
        return edit

    def verify_workbook_type_element_copy(self):
        copy = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Copy").is_displayed()
        return copy

    def verify_workbook_type_element_remove(self):
        remove = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Remove").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Cancel").click()
        return remove

    '''TestCase T35918'''

    def cld_workbook(self):
        self.driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_File").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_NewWorkbook").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_CLDWorkbook").click()

    '''TestCase T35904'''

    def raw_data_column_sorting(self):
        self.driver.find_element_by_accessibility_id("PenId").click()
        time.sleep(3)
        sort = self.driver.find_element_by_accessibility_id("CellElement_0_1")
        element = sort.get_attribute("Name")
        return element

    def raw_data_column_sorting1(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("PenId").click()
        time.sleep(6)
        sort = self.driver.find_element_by_accessibility_id("CellElement_0_1")
        abc = sort.get_attribute("Name")
        self.driver.find_element_by_accessibility_id("PenId").click()
        time.sleep(1)
        return abc

    '''TestCase T35905'''

    def raw_data_unselect_parameter(self):
        self.driver.find_element_by_name("Empty : parameter").click()
        actionchains = ActionChains(self.driver)
        for x in range(0, 12):
            actionchains.send_keys(Keys.ARROW_UP).perform()

        self.driver.find_element_by_accessibility_id("AutomationId_RawData_AllHeadersVisible").click()
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_HeaderVisibility").click()
        verify = self.driver.find_element_by_accessibility_id("ChipId").is_displayed()
        return verify

    '''TestCase T35906'''

    def raw_data_new_parameter(self):
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_NewParameter").click()
        verify = self.driver.find_element_by_name("NEW PARAMETER").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_ParameterEditor_Close").click()
        return verify

    '''TestCase T35907'''

    def raw_data_add_new_parameter(self):
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_NewParameter").click()
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_ParameterEditor_Entries").click()
        time.sleep(3)

        actionchains = ActionChains(self.driver)
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actionchains.send_keys(Keys.ARROW_UP).perform()
        actionchains.send_keys(Keys.RETURN).perform()

        time.sleep(5)

        self.driver.find_element_by_accessibility_id("AutomationId_RawData_ParameterEditor_ParameterInput").send_keys(
            "parameter")
        self.driver.find_element_by_name("Fields").click()
        element = self.driver.find_element_by_name("[Empty : CellCount]")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element).perform()

        self.driver.find_element_by_accessibility_id("Multiply").click()

    def penid_attribute(self):
        actionchains = ActionChains(self.driver)
        penid = self.driver.find_element_by_name("[Empty : PenId]")
        actionchains.double_click(penid).perform()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_ParameterEditor_Apply").click()

    def raw_data_verify_parameter(self):
        self.driver.find_element_by_name("ChipId").click()
        actionchains = ActionChains(self.driver)
        for x in range(0, 10):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(5)
        parameter = self.driver.find_element_by_name("Empty : parameter").is_displayed()
        return parameter

    def raw_data_verify_parameter_in_grid(self):
        for x in range(0, 18):
            self.driver.find_element_by_accessibility_id("HorizontalLargeIncrease").click()
        grid = self.driver.find_element_by_accessibility_id("Empty : parameter").is_displayed()
        return grid

    '''TestCase T35907'''

    '''def raw_data_add_new_parameter(self):
        driver.find_element_by_accessibility_id("AutomationId_RawData_NewParameter").click()
        driver.find_element_by_accessibility_id("AutomationId_RawData_ParameterEditor_Entries").click()
        time.sleep(3)
        driver.find_element_by_accessibility_id("AutomationId_RawData_ParameterEditor_Entries_Item_Empty").click()
        driver.find_element_by_accessibility_id("RichTextBox").send_keys("shivam")
        driver.find_element_by_name("Fields").click()
        element = driver.find_element_by_name("[Load-3 : CellCount]")
        actionchains = ActionChains(driver)
        actionchains.double_click(element).perform()
        driver.find_element_by_name("Operators").click()
        mul = driver.find_element_by_name(" * ")
        actionchains.double_click(mul).perform()
        driver.find_element_by_accessibility_id("PART_ExpressionNodeEditor").click()
        time.sleep(3)
        driver.find_element_by_accessibility_id("PART_ExpressionNodeEditor").send_keys("2")
        driver.find_element_by_accessibility_id("AutomationId_RawData_ParameterEditor_Apply").click()
        time.sleep(5)'''

    def raw_data(self):
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_NewParameter").click()
        driver.find_element_by_accessibility_id("RichTextBox").send_keys("shivam")

    '''TestCase T35644'''

    def raw_data_drag_drop(self):
        time.sleep(3)
        actionchains = ActionChains(self.driver)
        drag = self.driver.find_element_by_accessibility_id("Load-3 : CellCountVerified")
        drop = self.driver.find_element_by_name("GridViewGroupPanel")
        actionchains.drag_and_drop(drag, drop).perform()
        time.sleep(3)
        verify = self.driver.find_element_by_accessibility_id("GroupRow_0_1").is_displayed()
        return verify

    '''TestCase T35645'''

    def raw_data_drag_drop_items(self):
        actionchains = ActionChains(self.driver)
        drag = self.driver.find_element_by_accessibility_id("ChipId")
        drop = self.driver.find_element_by_name("GridViewGroupPanel")
        actionchains.drag_and_drop(drag, drop).perform()
        # time.sleep(2)
        # driver.find_element_by_accessibility_id("ExpanderButton").click()
        # verify = driver.find_element_by_accessibility_id("GroupRow_D50238_2").is_displayed()
        # return verify

    '''TestCase T35654'''

    def raw_data_remove_grouping(self):
        self.driver.find_element_by_accessibility_id("PART_CloseButton").click()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("PART_CloseButton").click()

    '''TestCase T35669'''

    def raw_data_reordering_column(self):
        actionchains = ActionChains(self.driver)
        drag = self.driver.find_element_by_accessibility_id("ChipId")
        drop = self.driver.find_element_by_accessibility_id("Load-3 : CellCountVerified")
        actionchains.drag_and_drop(drag, drop).perform()

    '''TestCase T35679'''

    def raw_data_column_drag(self):
        actionchains = ActionChains(self.driver)
        drag = self.driver.find_element_by_name("Load-3 : CellCountVerified")
        drop = self.driver.find_element_by_name("ChipId")
        actionchains.drag_and_drop(drag, drop).perform()

    '''TestCase T35703'''

    def raw_data_uncheck_all(self):
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_AllHeadersVisible").click()
        # verify = driver.find_element_by_accessibility_id("Cell_0_0").is_displayed()
        # return verify

    '''TestCase T35600'''

    def chip_timeline_open_from_window(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_Window").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_Windows").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_ChipTimeline").click()
        verify = self.driver.find_element_by_accessibility_id("AutomationId_TimeLine_ChipTimeline").is_displayed()
        return verify

    '''TestCase T35899'''

    def add_chip_in_filter(self):
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_Chips").click()
        self.driver.find_element_by_name("D37712").click()
        time.sleep(2)

    '''comment'''
    '''TestCase T35900'''

    def filter_name(self, name):
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_FilterName").send_keys(name)
        self.driver.find_element_by_accessibility_id("HeaderCloseButton").click()
        self.driver.find_element_by_accessibility_id("HeaderDropDownMenu").click()
        self.driver.find_element_by_name("Tabbed document").click()

        # driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_Filte").send_keys("shivam")

    def close_filter(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder").click()
        close = self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder")
        actionchains = ActionChains(self.driver)
        actionchains.context_click(close).perform()
        self.driver.find_element_by_name("Hide").click()

    '''TestCase T35901'''

    def add_condition_filter(self):
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_AddCondition").click()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_DimensionSelector").click()
        # driver.find_element_by_name("PenId").click()
        time.sleep(2)

    def abc(self):
        # driver.find_element_by_name("PenId").click()
        self.driver.find_element_by_name("Empty:Cell_Count").click()

    def penid(self):
        pen = self.driver.find_element_by_name("PenId").is_displayed()
        return pen

    def pen_state(self):
        state = self.driver.find_element_by_name("PenState").is_displayed()
        # state = driver.find_element_by_name("PenState1").is_displayed()
        return state

    def load_pen_filter(self):
        penid = self.driver.find_element_by_name("Empty:Pen_Id").is_displayed()
        return penid

    def load_device_id(self):
        deviceid = self.driver.find_element_by_name("Empty:Device_Id").is_displayed()
        return deviceid

    def load_cell_count_verified(self):
        cellcount = self.driver.find_element_by_name("Empty:Cell_Count_Verified").is_displayed()
        return cellcount

    def load_cell_count(self):
        loadcellcount = self.driver.find_element_by_name("Empty:Cell_Count").is_displayed()
        return loadcellcount

    def load_celltype(self):
        celltype = self.driver.find_element_by_name("Empty:Cell_Type").is_displayed()
        return celltype

    def load_pen_id(self):
        loadpenid = self.driver.find_element_by_name("Load-3:PenId").is_displayed()
        return loadpenid

    def cell_count_verified(self):
        cellcountverified = self.driver.find_element_by_name("Load-3:CellCountVerified").is_displayed()
        return cellcountverified

    def cell_count(self):
        cellcounts = self.driver.find_element_by_name("Load-3:CellCount").is_displayed()
        return cellcounts

    def cell_type(self):
        celltypes = self.driver.find_element_by_name("Load-3:CellType").is_displayed()
        return celltypes

    '''TestCase T35903'''

    def filter_close(self):
        actionchains = ActionChains(self.driver)
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_SaveFilter").click()
        time.sleep(2)
        close = self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder")
        actionchains.context_click(close).perform()
        self.driver.find_element_by_name("Hide").click()

    def filter_save_button_oned(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_Window").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_New").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_WorkbookExplorer").click()
        time.sleep(5)
        verify = self.driver.find_element_by_name("fil").is_displayed()
        return verify

    '''TestCase T35984'''

    def verify_savefilter(self):
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_SaveFilter").click()
        time.sleep(4)

    def filter_save_button_twod(self):
        time.sleep(2)
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_ContextMenu_ElementsTree_Element_Filter2").is_displayed()
        return verify

    '''Testcase T35983'''

    def filter_twod_condition(self):
        # actionchains = ActionChains(driver)
        '''driver.find_element_by_accessibility_id("HeaderCloseButton").click()
        driver.find_element_by_accessibility_id("HeaderDropDownMenu").click()
        driver.find_element_by_name("Tabbed document").click()'''
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_FilterDimension").click()
        self.driver.find_element_by_name("2-D").click()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_AddCondition").click()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_AggregationMode").click()
        time.sleep(3)
        self.driver.find_element_by_name("Max").click()

    def filter_twod_xaxis(self):
        time.sleep(4)
        xaxis = self.driver.find_element_by_accessibility_id(
            "AutomationId_FilterBuilder_2DFilter_XAxis_Values").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_2DFilter_XAxis_Values").click()
        self.driver.find_element_by_name("Empty:Cell_Count_Verified").click()
        return xaxis

    def filter_twod_yaxis(self):
        time.sleep(3)
        yaxis = self.driver.find_element_by_accessibility_id(
            "AutomationId_FilterBuilder_2DFilter_YAxis_Values").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_2DFilter_YAxis_Values").click()
        self.driver.find_element_by_name("Empty:Cell_Count_Verified").click()
        return yaxis

    def filter_verify_chart(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_FilterBuilder_2DFilter_Chart").is_displayed()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_Window").click()
        self.driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_New").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_WorkbookExplorer").click()
        return verify

    '''TestCase T35627'''

    def filter_select_string_parameter(self):
        self.driver.find_element_by_name("Load-3:Device_Id").click()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_StringFilter_Items").click()
        self.driver.find_element_by_name("D50238").click()
        verify = self.driver.find_element_by_name("1535").is_displayed()
        return verify

    '''TestCase T35893'''

    def gallery_setting(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()

    def visible(self):
        visible = self.driver.find_element_by_accessibility_id("Visible").is_displayed()
        return visible

    def show_rank(self):
        rank = self.driver.find_element_by_accessibility_id("Show Rank").is_displayed()
        return rank

    def column_name(self):
        column = self.driver.find_element_by_accessibility_id("Column Name").is_displayed()
        return column

    def column_footer(self):
        footer = self.driver.find_element_by_accessibility_id("Column Footer").is_displayed()
        return footer

    def row_height(self):
        height = self.driver.find_element_by_name("Row Height :").is_displayed()
        return height

    def digits_after_comma(self):
        digits = self.driver.find_element_by_name("Digits after comma :").is_displayed()
        return digits

    def pen_reject_approval(self):
        pen = self.driver.find_element_by_accessibility_id(
            "AutomationId_GallerySettings_PenRejectApproval").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_GallerySettings_Close").click()
        return pen

    '''TestCase 35895'''

    def gallery_sort_element(self):
        self.driver.find_element_by_accessibility_id("Id").click()
        time.sleep(1)
        sort = self.driver.find_element_by_name("Pen_1").is_displayed()
        return sort

    def gallery_sort_element1(self):
        self.driver.find_element_by_accessibility_id("Id").click()
        time.sleep(1)
        sort = self.driver.find_element_by_name("Pen_1758").is_displayed()
        self.driver.find_element_by_accessibility_id("Id").click()
        return sort

    def attribute_showup_under_each_image_sequence(self):
        self.driver.find_element_by_accessibility_id()

    '''TestCase T35609'''

    def gallery_image_sequence_load3(self):
        load3 = self.driver.find_element_by_accessibility_id("Load-3").is_displayed()
        return load3

    def gallery_image_sequence_load5(self):
        load5 = self.driver.find_element_by_accessibility_id("Load-5").is_displayed()
        return load5

    def gallery_image_sequence_pe(self):
        pe = self.driver.find_element_by_accessibility_id("TPS-PE").is_displayed()
        return pe

    def gallery_image_sequence_fitc(self):
        fitc = self.driver.find_element_by_accessibility_id("TPS-FITC").is_displayed()
        return fitc

    '''TestCase T35610'''

    def gallery_show_rank(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        self.driver.find_element_by_accessibility_id("CellElement_0_1").click()
        self.driver.find_element_by_accessibility_id("CellElement_1_1").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GallerySettings_Apply").click()
        verify = self.driver.find_element_by_name("1535").is_displayed()
        return verify

    '''TestCase T35612'''

    def gallery_increase_row_height(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        self.driver.find_element_by_accessibility_id("increase").click()
        self.driver.find_element_by_accessibility_id("increase").click()
        self.driver.find_element_by_accessibility_id("increase").click()
        self.driver.find_element_by_accessibility_id("increase").click()
        self.driver.find_element_by_accessibility_id("increase").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GallerySettings_Apply").click()

    '''TestCase T35670'''

    def gallery_reorder_column(self):
        actionchains = ActionChains(self.driver)
        drag = self.driver.find_element_by_accessibility_id("Load-3")
        drop = self.driver.find_element_by_accessibility_id("TPS-PE")
        actionchains.drag_and_drop(drag, drop).perform()

    '''TestCase T35667'''

    def gallery_change_brightness_contrast(self):
        actionchains = ActionChains(self.driver)
        load = self.driver.find_element_by_accessibility_id("Load-3")
        actionchains.context_click(load).perform()
        self.driver.find_element_by_accessibility_id("IncreaseButton").click()
        self.driver.find_element_by_accessibility_id("IncreaseButton").click()
        self.driver.find_element_by_accessibility_id("IncreaseButton").click()
        self.driver.find_element_by_accessibility_id("IncreaseButton").click()
        self.driver.find_element_by_accessibility_id("IncreaseButton").click()
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery").click()

    '''TestCase T35615'''

    def gallery_visible_pens(self):
        visible = self.driver.find_element_by_name(" Visible 1535 of 1535 pens").is_displayed()
        return visible

    '''TestCase T35896'''

    def gallery_attribute_list(self):
        self.driver.find_element_by_accessibility_id("CellElement_0_0").click()

    def verify_attribute_penid(self):
        penid = self.driver.find_element_by_name("PenId: ").is_displayed()
        return penid

    def verify_attribute_deviceid(self):
        deviceid = self.driver.find_element_by_name("Device_Id: ").is_displayed()
        return deviceid

    def verify_attribute_cellcountverified(self):
        cell = self.driver.find_element_by_name("CellCountVerified: ").is_displayed()
        return cell

    def verify_attribute_cellcount(self):
        cellcount = self.driver.find_element_by_name("CellCount: ").is_displayed()
        return cellcount

    '''TestCases T35897'''

    def gallery_select_pens(self):
        pens = []
        pens = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Selected")
        for x in range(1, 4):
            pens[x].click()

    '''TestCase T35975'''

    def gallery_export_csv(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_ExportMenu_ExportToCSV").click()
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_ExportToCSV_Export").click()
        verify = self.driver.find_element_by_name("Selected pens have been successfully exported.").is_displayed()
        self.driver.find_element_by_accessibility_id("OKButton").click()
        return verify

    '''TestCase T35974'''

    def gallery_select_data_attribute(self):
        element = []
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        self.driver.find_element_by_accessibility_id("VerticalLargeIncrease").click()
        element = self.driver.find_elements_by_accessibility_id("AutomationId_GallerySettings_ColumnFooters")
        actionchains = ActionChains(self.driver)
        actionchains.move_to_element_with_offset(element[6], 50, 1)
        actionchains.click()
        actionchains.perform()
        for x in range(0, 3):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
            actionchains.send_keys(Keys.RETURN).perform()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("CellElement_6_0").click()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_GallerySettings_Apply").click()
        return len(element)
        # time.sleep(5)

    def verify_attribute1(self):
        verify1 = self.driver.find_element_by_name("Empty: PenId: ").is_displayed()
        return verify1

    def verify_attribute2(self):
        verify2 = self.driver.find_element_by_name("Empty: CellCountVerified: ").is_displayed()
        return verify2

    def verify_attribute3(self):
        verify3 = self.driver.find_element_by_name("Empty: CellCount: ").is_displayed()
        return verify3

    def verify_attribute4(self):
        verify4 = self.driver.find_element_by_name("Load: PenId: ").is_displayed()
        return verify4

    def verify_attribute5(self):
        verify5 = self.driver.find_element_by_name("Empty: parameter: ").is_displayed()
        return verify5

    def gallery_export_pdf(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_ExportMenu_ExportToPDF").click()
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_ExportToPDF_Export").click()
        actionchains = ActionChains(self.driver)
        try:
            time.sleep(3)
            data = self.driver.find_element_by_name("data.pdf")
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            data.click()
            actionchains.send_keys(Keys.DELETE).perform()

        self.driver.find_element_by_accessibility_id("1001").send_keys("data")
        self.driver.find_element_by_accessibility_id("1").click()
        time.sleep(5)
        self.driver.find_element_by_accessibility_id("CancelButton").click()

    '''TestCase T35910'''

    def raw_data_parameter_in_gallery(self):
        verify = self.driver.find_element_by_name("parameter: ").is_displayed()
        return verify

    '''TestCase T35894'''

    def gallery_select_attribute(self):
        actionchains = ActionChains(self.driver)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GallerySettings_ColumnFooters").click()
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actionchains.send_keys(Keys.RETURN).perform()
        time.sleep(10)
        # driver.find_element_by_accessibility_id("AutomationId_GallerySettings_ColumnFooters_Item_CellCount").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GallerySettings_Apply").click()
        cell = self.driver.find_element_by_name("CellCount: ").is_displayed()
        return cell

    '''TestCase T35969'''

    def gallery_image_sequence_empty(self):
        empty = self.driver.find_element_by_accessibility_id("Empty").is_displayed()
        return empty

    def gallery_image_sequence_load(self):
        load = self.driver.find_element_by_accessibility_id("Load").is_displayed()
        return load

    def gallery_image_sequence_culture(self):
        culture = self.driver.find_element_by_accessibility_id("Culture").is_displayed()
        return culture

    def gallery_image_sequence_assay(self):
        assay = self.driver.find_element_by_accessibility_id("Assay").is_displayed()
        return assay

    def gallery_image_sequence_culture2(self):
        culture2 = self.driver.find_element_by_accessibility_id("Assay").is_displayed()
        return culture2

    def gallery_image_sequence_assay2(self):
        assay2 = self.driver.find_element_by_accessibility_id("Assay").is_displayed()
        return assay2

    '''TestCase T35621'''

    def gallery_custom_parameter_attribute(self):
        abc = self.driver.find_element_by_name("abc: ").is_displayed()
        return abc

    '''TestCase T35663


    def gallery_enlarge_image():
        actionchains = ActionChains(driver)
        image = driver.find_element_by_accessibility_id("PART_ImageHost")
        actionchains.double_click(image).perform()
        enlarged = driver.find_element_by_name("Enlarged Image").is_displayed()
        driver.find_element_by_accessibility_id("PART_Close").click()
        return enlarged '''

    '''TestCase T35970'''

    def add_graph_button(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddNewGraph").click()
        graph = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder")
        verify = graph.get_attribute("Name")
        return verify

    def add_graph(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_GraphType").click()
        self.driver.find_element_by_name("Scatter Plot").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Chip").click()
        self.driver.find_element_by_name("D37712").click()
        verify = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot").is_displayed()
        return verify

    '''TestCase T35971'''

    def graph_builder_graph_type(self):
        graph = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_GraphType").is_displayed()
        return graph

    def graph_builder_chip(self):
        chip = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Chip").is_displayed()
        return chip

    def graph_builder_save_button(self):
        save = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Save")
        verify = save.get_attribute("Name")
        return verify

    def graph_builder_export(self):
        export = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Export").is_displayed()
        return export

    def graph_builder_setting(self):
        setting = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Settings").is_displayed()
        return setting

    def graph_builder_linktogallery(self):
        gallery = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_LinkToGallery")
        verify = gallery.get_attribute("Name")
        return verify

    def graph_builder_linktorawdata(self):
        raw = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_LinkToRawData")
        verify = raw.get_attribute("Name")
        return verify

    def graph_builder_select(self):
        select = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_SelectOrZoom")
        verify = select.get_attribute("Name")
        return verify

    def graph_builder_xaxis(self):
        xaxis = self.driver.find_element_by_accessibility_id(
            "AutomationId_GraphBuilder_ScatterPlot_XAxis_Values").is_displayed()
        return xaxis

    def graph_builder_yaxis(self):
        yaxis = self.driver.find_element_by_accessibility_id(
            "AutomationId_GraphBuilder_ScatterPlot_YAxis_Values").is_displayed()
        return yaxis

    def graph_builder_groupby(self):
        color = self.driver.find_element_by_accessibility_id(
            "AutomationId_GraphBuilder_ScatterPlot_Color").is_displayed()
        return color

    '''TestCase T35972'''

    def graph_builder_axis_attribute(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_XAxis_Values").click()
        self.driver.find_element_by_name("Empty:Pen_Id").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_YAxis_Values").click()
        self.driver.find_element_by_name("Empty:Cell_Count_Verified").click()
        time.sleep(2)
        graph = self.driver.find_element_by_accessibility_id(
            "AutomationId_GraphBuilder_ScatterPlot_Chart_Legend").is_displayed()
        return graph

    '''TestCase T35973'''

    def verify_legend(self):
        verify = self.driver.find_element_by_name("Undecided").is_displayed()
        return verify

    def graph_builder_change_groupby(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_Color").click()
        self.driver.find_element_by_name("Empty:Cell_Type").click()
        time.sleep(5)
        verify = self.driver.find_element_by_name("Line 1").is_displayed()
        return verify

    '''TestCase T35976'''

    def graph_builder_save(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Save").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_SaveGraph_Name").send_keys("graph")
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_SaveGraph_Apply").click()
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_ContextMenu_ElementsTree_Element_Graph").is_displayed()
        return verify

    def close_graph(self):
        actionchains = ActionChains(self.driver)
        hide = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder")
        actionchains.context_click(hide).perform()
        self.driver.find_element_by_name("Hide").click()

    '''TestCase T35977'''

    def graph_builder_open_saved_graph(self):
        open = self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_ContextMenu_ElementsTree_Element_Graph")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(open).perform()
        time.sleep(5)

    def verify_xaxis(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_XAxis_Values").click()
        xaxis = self.driver.find_element_by_name("Empty:Pen_Id").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_XAxis_Values").click()
        return xaxis

    def verify_yaxis(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_YAxis_Values").click()
        yaxis = self.driver.find_element_by_name("Empty:Cell_Count_Verified").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_YAxis_Values").click()
        return yaxis

    def verify_color_dropdown(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_Color").click()
        color = self.driver.find_element_by_name("Empty:Cell_Type").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_Color").click()
        return color

    '''TestCase T35978'''

    def add_graph_histogram(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddNewGraph").click()

    def histogram_select_attribute(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_GraphType").click()
        self.driver.find_element_by_name("Histogram").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Chip").click()
        self.driver.find_element_by_name("D37712").click()
        verify = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Histogram").is_displayed()
        return verify

    def histogram_xaxis(self):
        xaxis = self.driver.find_element_by_accessibility_id(
            "AutomationId_GraphBuilder_Histogram_XAxis_Values").is_displayed()
        return xaxis

    def histogram_bin_value(self):
        bin = self.driver.find_element_by_accessibility_id(
            "AutomationId_GraphBuilder_Histogram_BinCounts").is_displayed()
        return bin

    def histogram_null_value_checkbox(self):
        null = self.driver.find_element_by_accessibility_id(
            "AutomationId_GraphBuilder_Histogram_ShowNullableValues").is_displayed()
        return null

    '''TestCase T35979'''

    def histogram_select_xaxis(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Histogram_XAxis_Values").click()
        self.driver.find_element_by_name("Empty:Cell_Count_Verified").click()
        time.sleep(3)
        histogram = self.driver.find_element_by_accessibility_id(
            "AutomationId_GraphBuilder_Histogram_Chart").is_displayed()
        return histogram

    '''TestCase 35981'''

    def histogram_save(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Save").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_SaveGraph_Name").send_keys("graph1")
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_SaveGraph_Apply").click()
        save = self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_ContextMenu_ElementsTree_Element_Graph1").is_displayed()
        return save

    '''TestCase T35982'''

    def open_histogram(self):
        actionchains = ActionChains(self.driver)
        open = self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_ContextMenu_ElementsTree_Element_Graph1")
        actionchains.double_click(open).perform()

    def verify_axis(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Histogram_XAxis_Values").click()
        axis = self.driver.find_element_by_name("Empty:Cell_Count_Verified").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Histogram_XAxis_Values").click()
        return axis

    def verify_bin(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Histogram_BinCounts").click()
        bin = self.driver.find_element_by_name("5").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Histogram_BinCounts").click()
        return bin

    def filter(self):
        self.driver.find_element_by_accessibility_id("abcd").click()
        # allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def gallery(self):
        self.driver.find_element_by_name("demo").click()

    '''TestCase T35980'''

    def change_bin_quantity(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Chip").click()
        self.driver.find_element_by_name("D37712").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Histogram_BinCounts").click()
        self.driver.find_element_by_name("6").click()
        bin = self.driver.find_element_by_name("0..0.5").is_displayed()
        return bin

    '''TestCase T35902'''

    def filter_builder_set_min(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_FilterBuilder_SliderFilter_SelectedMin").is_displayed()
        return verify

    def filter_builder_set_max(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_FilterBuilder_SliderFilter_SelectedMax").is_displayed()
        return verify

    def filter_builder_increase(self):
        inc = []
        inc = self.driver.find_elements_by_accessibility_id("increase")
        inc[1].click()
        inc[1].click()
        time.sleep(3)
        pen = self.driver.find_element_by_name("1756").is_displayed()
        return pen

    '''Timeline T42209'''

    def timeline_image_sequence_expander(self):
        actionchains = ActionChains(self.driver)
        chip = []
        time.sleep(2)
        chip = self.driver.find_elements_by_name("D37712")
        actionchains.move_to_element_with_offset(chip[2], 10, 10).click().perform()
        time.sleep(5)

    def timeline_image_sequence1(self):
        time.sleep(2)
        sequence1 = self.driver.find_element_by_accessibility_id(
            "AutomationId_TimeLine_TimeLineItem_AutoPenQA_postOET").is_displayed()
        return sequence1

    def timeline_image_sequence2(self):
        sequence2 = self.driver.find_element_by_accessibility_id(
            "AutomationId_TimeLine_TimeLineItem_Sequence_2018-05-04_13-00-47.552_Cellsinchannelafterimport").is_displayed()
        return sequence2

    def timeline_image_sequence3(self):
        sequence3 = self.driver.find_element_by_accessibility_id(
            "AutomationId_TimeLine_TimeLineItem_Sequence_2018-05-07_16-17-02.131_Test").is_displayed()
        return sequence3

    def timeline_image_sequence4(self):
        sequence4 = self.driver.find_element_by_accessibility_id(
            "AutomationId_TimeLine_TimeLineItem_Sequence_2018-05-09_09-03-20.370_Spotlight_Hu3_AfterCulture_Day_4").is_displayed()
        return sequence4

    '''Remove raw data parameter'''

    def remove_new_parameter(self):
        self.driver.find_element_by_name("ChipId").click()
        actionchains = ActionChains(self.driver)
        for x in range(0, 10):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        parameter = []
        parameter = self.driver.find_elements_by_accessibility_id("AutomationId_RawData_RemoveParameter")
        customparam = len(parameter)
        parameter[customparam - 1].click()
        self.driver.find_element_by_accessibility_id("OKButton").click()
        return len(parameter)

    """testcase T42264"""

    def verify_version_number(self):
        versionnumber = self.driver.find_element_by_name("ASSAY ANALYZER 2.0").is_displayed()
        return versionnumber

    """testcase T42442"""

    def verify_shortinformation(self):
        self.driver.find_element_by_name("Help").click()
        self.driver.find_element_by_name("About").click()
        self.driver.find_element_by_name("Version 20191129.2").is_displayed()
        desc = self.driver.find_element_by_name(
            "Powerful software that is designed to work with gigabytes of data obtained from Optoﬂuidic platforms developed by Berkeley Lights. The main usage of the app is to help biologists easily find, check and export data to pdf files in minutes.").is_displayed()
        pr = self.driver.find_elements_by_accessibility_id("PART_Close")
        print(pr)
        pr[1].click()
        return desc

    """testcase T42195"""

    def verify_filterbuilder(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddNewFilter").click()
        time.sleep(5)
        filterwind = self.driver.find_element_by_accessibility_id("HeaderElement").is_displayed()  # "Rad Pane Group"
        time.sleep(3)
        pr = self.driver.find_elements_by_accessibility_id("HeaderDropDownMenu")
        # print(pr)
        pr[1].click()
        self.driver.find_element_by_name("Hide").click()
        return filterwind

    """testcase T42196"""

    def verify_expander(self):
        self.driver.find_element_by_accessibility_id("Expander").click()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("Expander").click()
        time.sleep(2)
        chiptext = self.driver.find_element_by_name("D37712").is_displayed()
        return chiptext

    """testcase T42200"""

    def verify_removechip(self):
        global actionchains
        actionchains = ActionChains(self.driver)
        chip = self.driver.find_element_by_name("D37712")
        actionchains.context_click(chip).perform()
        time.sleep(3)
        self.driver.find_element_by_name("Remove chip(s)").click()
        self.driver.find_element_by_accessibility_id("OKButton").click()
        try:
            a = self.driver.find_element_by_name("D37712").is_displayed()
            return a
        except:
            b = False
            return b

    """testcase T42201"""

    def verify_saveworkbookbutton(self):
        self.driver.find_element_by_accessibility_id("AutomationId_WorkbookExplorer_Save").click()
        explorerwin = self.driver.find_element_by_name("Save As").is_displayed()
        actionchains = ActionChains(self.driver)
        scrolldown = self.driver.find_elements_by_accessibility_id("DownButton")
        print(scrolldown)
        actionchains.double_click(scrolldown[2]).perform()
        try:
            data = self.driver.find_element_by_name("workbooktest.workbook")
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            data.click()
            actionchains.send_keys(Keys.DELETE).perform()
        self.driver.find_element_by_accessibility_id("1001").send_keys("workbooktest")
        time.sleep(3)
        return explorerwin

    """testcase T42202"""

    def verify_usersaveworkbook(self):
        # save = self.driver.find_element_by_accessibility_id("1").is_displayed()
        self.driver.find_element_by_accessibility_id("1").click()
        # return save

    """testcase 42203"""

    def verify_useropenworkbook(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_WorkbookExplorer_Save").click()
        self.driver.find_element_by_name("Save As").is_displayed()
        actionchains = ActionChains(self.driver)
        scrolldown = self.driver.find_elements_by_accessibility_id("DownButton")
        actionchains.double_click(scrolldown[2]).perform()
        workbook = self.driver.find_element_by_name("workbooktest.workbook").is_displayed()
        self.driver.find_element_by_name("workbooktest.workbook").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("2").click()
        # self.driver.find_element_by_accessibility_id("CancelButton").click()
        try:
            time.sleep(3)
            data = self.driver.find_element_by_name("CONFIRMATION")
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            self.driver.find_element_by_accessibility_id("CancelButton").click()

        return workbook

    # def verify_useropenworkbook(self):
    #     time.sleep(2)
    #     self.driver.find_element_by_accessibility_id("AutomationId_WorkbookExplorer_Open").click()
    #     workbook = self.driver.find_element_by_name("workbooktest.workbook").is_displayed()
    #     self.driver.find_element_by_name("workbooktest.workbook").click()
    #     self.driver.find_element_by_accessibility_id("1").click()
    #     time.sleep(3)
    #     self.driver.find_element_by_name("Cancel").click()
    #     return workbook

    """testcase T42304"""

    def verify_graphbutton(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddNewGraph").click()
        graphbutton = self.driver.find_element_by_name("Graph Builder").is_displayed()
        time.sleep(3)
        actionchains = ActionChains(self.driver)
        chip = self.driver.find_element_by_name("Graph Builder")
        actionchains.context_click(chip).perform()
        self.driver.find_element_by_name("Hide").click()
        return graphbutton

    """testcase T42383"""

    def verify_changeworkbook(self):
        self.driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_File").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_NewWorkbook").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_CLD").click()
        try:
            time.sleep(3)
            data = self.driver.find_element_by_name("CONFIRMATION")
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            self.driver.find_element_by_name("Cancel").click()

    def verify_reloadchips(self):
        global actionchains
        actionchains = ActionChains(self.driver)
        chip1 = self.driver.find_element_by_name("D37712")
        actionchains.context_click(chip1).perform()
        time.sleep(3)
        self.driver.find_element_by_name("Open in Raw Data").click()
        chip2 = self.driver.find_element_by_name("D37712")
        actionchains.context_click(chip2).perform()
        time.sleep(3)
        self.driver.find_element_by_name("Reload chip(s)").click()
        time.sleep(3)
        raw = self.driver.find_element_by_accessibility_id("AutomationId_RawData")
        actionchains.context_click(raw).perform()
        self.driver.find_element_by_name("Hide").click()

    """testcase T42384"""

    def verify_containingfolder(self):
        global actionchains
        actionchains = ActionChains(self.driver)
        chip = self.driver.find_element_by_name("D37712")
        actionchains.context_click(chip).perform()
        self.driver.find_element_by_name("Open Containing Folder").click()
        time.sleep(3)
        self.driver.find_element_by_name("workbooktest.workbook").click()
        self.driver.find_element_by_accessibility_id("Close").click()
        # return workbook

    """testcase T42453"""

    def verify_chipconfirmation(self):
        global actionchains
        actionchains = ActionChains(self.driver)
        time.sleep(2)
        chip = self.driver.find_element_by_name("D37712")
        actionchains.context_click(chip).perform()
        time.sleep(3)
        self.driver.find_element_by_name("Remove chip(s)").click()
        close = self.driver.find_elements_by_accessibility_id("PART_Close")
        close[1].click()
        chipvisible = self.driver.find_element_by_name("D37712").is_displayed()
        return chipvisible

    """testcase T42454"""

    def verify_draganddropui(self):
        global actionchains
        actionchains = ActionChains(self.driver)
        source = self.driver.find_element_by_name("D37712")
        destination = self.driver.find_element_by_accessibility_id("AutomationId_WorkbookExplorer")
        time.sleep(2)
        actionchains.drag_and_drop(source, destination).perform()
        time.sleep(3)
        checkui = source.is_displayed()
        return checkui

    """testcase T42205"""

    def verify_opentimeline(self):
        chip = self.driver.find_element_by_name("D37712")
        actionchains = ActionChains(self.driver)
        actionchains.context_click(chip).perform()
        self.driver.find_element_by_name("Open in Timeline").click()
        time.sleep(5)
        timeline = self.driver.find_element_by_accessibility_id("AutomationId_TimeLine")
        verify = timeline.get_attribute("Name")

        return verify

    """testcase T42204"""

    def verify_switchtimeline(self):
        global actionchains
        actionchains = ActionChains(self.driver)
        chip1 = self.driver.find_elements_by_name("D37712")
        print(chip1)
        actionchains.context_click(chip1[3]).perform()
        time.sleep(3)
        self.driver.find_element_by_name("Open in Raw Data").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_Window").click()
        time.sleep(2)
        self.driver.find_element_by_name("Windows").click()
        self.driver.find_element_by_name("Chip Timeline").click()
        time.sleep(4)
        verifychiptimeline = self.driver.find_elements_by_name("D37712")
        checktimeline = verifychiptimeline[1].is_displayed()
        raw = self.driver.find_element_by_accessibility_id("AutomationId_RawData")
        actionchains.context_click(raw).perform()
        self.driver.find_element_by_name("Hide").click()
        return checktimeline

    """testcase T42208"""

    def verify_timelinegridview(self):
        actionchains = ActionChains(self.driver)
        chip = []
        chip = self.driver.find_elements_by_name("D37712")
        actionchains.move_to_element_with_offset(chip[2], 10, 10).click().perform()
        time.sleep(5)
        sequence1 = self.driver.find_element_by_accessibility_id(
            "AutomationId_TimeLine_ChipColumns_Item_Empty").is_displayed()
        return sequence1

    """testcase T42259"""

    def verify_removechipfromtimeline(self):
        self.driver.find_element_by_accessibility_id("AutomationId_TimeLine_Chips_ChipSelection").click()
        try:
            verify = self.driver.find_element_by_accessibility_id(
                "AutomationId_TimeLine_ChipColumns_Item_Empty").is_displayed()
            return verify
        except:
            b = False
            return b

    """testcase 42386"""

    def verify_selectedchipdata(self):
        self.driver.find_element_by_accessibility_id("AutomationId_TimeLine_SelectFolder").click()
        time.sleep(4)
        chipdata = self.driver.find_element_by_name("Export_2018-05-09_20-46-53_D37712").is_displayed()
        # time.sleep(3)
        close = self.driver.find_elements_by_name("Close")
        close[1].click()
        return chipdata

    """testcase T42300"""

    def verify_timelinehistoryfile(self):
        global actionchains
        actionchains = ActionChains(self.driver)
        timeline = self.driver.find_element_by_accessibility_id("AutomationId_TimeLine")
        actionchains.context_click(timeline).perform()
        self.driver.find_element_by_name("Hide").click()
        time.sleep(3)
        appdata = os.getenv('APPDATA')
        os.remove(appdata + "\Assay Analyzer 2.0\D37712\History.xml")
        chip = self.driver.find_element_by_name("D37712")
        actionchains.context_click(chip).perform()
        self.driver.find_element_by_name("Open in Timeline").click()
        time.sleep(3)
        verifyfile = path.exists(appdata + "\Assay Analyzer 2.0\D37712\History.xml")
        return verifyfile

    """testcase T42301"""

    def verify_openhistoryxml(self):

        appdata = os.getenv('APPDATA')
        verifydata = " <CsvPath>Processed Data\D50238_2019-01-29_14-34-13_2019-01-29_11-19-56.549_TNFa_FITC_0_TNFa_FITC.csv</CsvPath>"
        verifyfile = path.exists(appdata + "\Assay Analyzer 2.0\D50238\CustomParameters.dat")
        if verifyfile == True:
            with open(appdata + "\Assay Analyzer 2.0\D50238\History.xml", 'r') as file:
                if verifydata in file.read():
                    print("data verified")
                    return True
                else:
                    return False

    """testcase T42302"""

    def verify_imageseqxmlforempty(self):
        appdata = os.getenv('APPDATA')
        verifydata = "<Type>Empty</Type>"
        verifyfile = path.exists(appdata + "\Assay Analyzer 2.0\D50238\CustomParameters.dat")
        if verifyfile == True:
            with open(appdata + "\Assay Analyzer 2.0\D37712\History.xml", 'r') as file:
                if verifydata in file.read():
                    return True
                else:
                    return False

    def verify_imageseqxmlforload(self):
        appdata = os.getenv('APPDATA')
        verifydata = "<Type>Load</Type>"
        verifyfile = path.exists(appdata + "\Assay Analyzer 2.0\D50238\CustomParameters.dat")
        if verifyfile == True:
            with open(appdata + "\Assay Analyzer 2.0\D37712\History.xml", 'r') as file:
                if verifydata in file.read():
                    return True
                else:
                    return False

    def verify_imageseqxmlforassay(self):
        appdata = os.getenv('APPDATA')
        verifydata = "<Type>Assay</Type>"
        verifyfile = path.exists(appdata + "\Assay Analyzer 2.0\D50238\CustomParameters.dat")
        if verifyfile == True:
            with open(appdata + "\Assay Analyzer 2.0\D37712\History.xml", 'r') as file:
                if verifydata in file.read():
                    return True
                else:
                    return False

    def verify_imageseqxmlforculture(self):
        appdata = os.getenv('APPDATA')
        verifydata = "<Type>Culture</Type>"
        verifyfile = path.exists(appdata + "\Assay Analyzer 2.0\D50238\CustomParameters.dat")
        if verifyfile == True:
            with open(appdata + "\Assay Analyzer 2.0\D37712\History.xml", 'r') as file:
                if verifydata in file.read():
                    return True
                else:
                    return False

    """testcase T42248"""

    def verify_selectparamter(self):
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_AllHeadersVisible").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_AllHeadersVisible").click()

    def verify_groupbyfeature(self):
        global actionchains
        actionchains = ActionChains(self.driver)
        source = self.driver.find_element_by_accessibility_id("PenId")
        destination = self.driver.find_element_by_accessibility_id("PART_GroupPanel")
        time.sleep(2)
        actionchains.drag_and_drop(source, destination).perform()

    def verify_groupbypenid1(self):
        time.sleep(5)
        verify = self.driver.find_element_by_accessibility_id("GroupRow_1_1").is_displayed()
        return verify

    def verify_groupbypenid2(self):
        verify = self.driver.find_element_by_accessibility_id("GroupRow_2_1").is_displayed()
        return verify

    def verify_groupbypenid3(self):
        verify = self.driver.find_element_by_accessibility_id("GroupRow_3_1").is_displayed()
        return verify

    """testcase T42249"""

    def verify_hierarichalgrouping(self):
        global actionchains
        actionchains = ActionChains(self.driver)
        source = self.driver.find_element_by_accessibility_id("Empty : PenId")
        destination = self.driver.find_element_by_accessibility_id("PART_GroupPanel")
        time.sleep(2)
        actionchains.drag_and_drop(source, destination).perform()

    def verify_groupbyemptypenid1(self):
        self.driver.find_element_by_accessibility_id("GroupRow_1_1").click()
        filter = self.driver.find_element_by_accessibility_id("GroupRow_1_2")
        verify = filter.get_attribute("Name")
        return verify

    def verify_groupbyemptypenid2(self):
        expandclick = self.driver.find_elements_by_name("1")
        expandclick[3].click()
        global actionchains
        actionchains = ActionChains(self.driver)
        source = self.driver.find_element_by_accessibility_id("Empty : Device_Id")
        destination = self.driver.find_element_by_accessibility_id("PART_GroupPanel")
        actionchains.drag_and_drop(source, destination).perform()
        time.sleep(4)
        filter = self.driver.find_element_by_accessibility_id("GroupRow_D37712_3")
        verify = filter.get_attribute("Name")
        closeheader = self.driver.find_elements_by_accessibility_id("PART_CloseButton")
        print(closeheader)
        closeheader[0].click()
        closeheader[1].click()
        closeheader[2].click()
        return verify

    """testcase T42252"""

    def verify_addparameterusingcompoperator(self):
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_NewParameter").click()
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_ParameterEditor_Entries").click()
        time.sleep(3)

        actionchains = ActionChains(self.driver)
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actionchains.send_keys(Keys.RETURN).perform()

        time.sleep(5)

        self.driver.find_element_by_accessibility_id(
            "AutomationId_RawData_ParameterEditor_ParameterInput").send_keys(
            "Cparameter1")
        self.driver.find_element_by_name("Fields").click()
        time.sleep(3)
        self.driver.find_element_by_name("[Empty : CellCount]").click()
        for x in range(0, 3):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()

        element1 = self.driver.find_element_by_name("[Load : CellCount]")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element1).perform()
        time.sleep(3)
        operator = self.driver.find_element_by_accessibility_id("GreaterThan")
        operator.click()

    def verify_otherattribute(self):
        actionchains = ActionChains(self.driver)
        for x in range(0, 3):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        # actionchains.send_keys(Keys.ARROW_DOWN).perform()
        element2 = self.driver.find_element_by_name("[Culture : CellCount]")
        actionchains.double_click(element2).perform()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_ParameterEditor_Apply").click()

    def raw_data_verify_parameter1(self):
        self.driver.find_element_by_name("ChipId").click()
        actionchains = ActionChains(self.driver)
        for x in range(0, 10):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(5)
        parameter = self.driver.find_element_by_name("Load : Cparameter1").is_displayed()
        return parameter

    """testcase T42253"""

    def verify_addparamLoperator(self):
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_NewParameter").click()
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_ParameterEditor_Entries").click()
        time.sleep(3)

        actionchains = ActionChains(self.driver)
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actionchains.send_keys(Keys.RETURN).perform()

        time.sleep(5)

        self.driver.find_element_by_accessibility_id(
            "AutomationId_RawData_ParameterEditor_ParameterInput").send_keys(
            "Lparameter1")
        self.driver.find_element_by_name("Fields").click()
        time.sleep(3)
        self.driver.find_element_by_name("[Empty : CellCount]").click()
        for x in range(0, 3):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()

        element1 = self.driver.find_element_by_name("[Load : CellCount]")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element1).perform()
        time.sleep(3)
        operator = self.driver.find_element_by_accessibility_id("GreaterThan")
        operator.click()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("PART_ExpressionNodeEditor").click()
        keyboard.press('1')
        self.driver.find_element_by_accessibility_id("And").click()

    def verify_otherLattribute(self):
        actionchains = ActionChains(self.driver)
        for x in range(0, 3):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        # actionchains.send_keys(Keys.ARROW_DOWN).perform()
        element2 = self.driver.find_element_by_name("[Culture : CellCount]")
        actionchains.double_click(element2).perform()
        time.sleep(3)
        operator = self.driver.find_element_by_accessibility_id("GreaterThan")
        operator.click()
        time.sleep(3)
        element = self.driver.find_element_by_accessibility_id("PART_ExpressionNodeEditor")
        element.click()

    def verify_attriint(self):
        actionchains = ActionChains(self.driver)
        for x in range(0, 3):
            actionchains.send_keys(Keys.ARROW_RIGHT).perform()
            time.sleep(4)
        keyboard.press('5')
        time.sleep(3)
        self.driver.find_element_by_name("OK").click()

    def raw_data_verify_Lparameter(self):
        self.driver.find_element_by_name("ChipId").click()
        actionchains = ActionChains(self.driver)
        for x in range(0, 10):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(5)
        parameter = self.driver.find_element_by_name("Load : Lparameter1").is_displayed()
        return parameter

    def verify_Lparameter1ingrid(self):
        for x in range(0, 18):
            self.driver.find_element_by_accessibility_id("HorizontalLargeIncrease").click()
        grid = self.driver.find_element_by_accessibility_id("Load : Lparameter1").is_displayed()
        return grid

    """testcase T42254"""

    def verify_Cparameteringrid(self):
        for x in range(0, 18):
            self.driver.find_element_by_accessibility_id("HorizontalLargeIncrease").click()
        grid = self.driver.find_element_by_accessibility_id("Load : Cparameter1").is_displayed()
        return grid

    """testcase T42255"""

    def verify_parameteringallery(self):
        self.driver.find_element_by_accessibility_id("CellElement_0_0").click()
        time.sleep(3)
        verify = self.driver.find_element_by_name("Cparameter1: ").is_displayed()
        return verify

    """testcase T42284"""

    def verify_logparameter(self):
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_NewParameter").click()
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_ParameterEditor_Entries").click()
        time.sleep(3)

        actionchains = ActionChains(self.driver)
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actionchains.send_keys(Keys.ARROW_UP).perform()
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actionchains.send_keys(Keys.RETURN).perform()

        time.sleep(5)

        self.driver.find_element_by_accessibility_id(
            "AutomationId_RawData_ParameterEditor_ParameterInput").send_keys(
            "Logparameter1")
        self.driver.find_element_by_name("Functions").click()
        time.sleep(4)
        atanclick = self.driver.find_element_by_name("Atan")
        atanclick.click()
        time.sleep(3)
        for x in range(0, 3):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()

    def verify_logselect(self):
        time.sleep(4)
        actionchains = ActionChains(self.driver)
        logclick = self.driver.find_element_by_name("Log")  # Log()
        actionchains.double_click(logclick).perform()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("PART_ExpressionNodeEditor").click()
        time.sleep(2)
        keyboard.press('left')

    def verify_movetoright(self):
        keyboard.press('left')
        actionchains = ActionChains(self.driver)
        fieldclick = self.driver.find_element_by_name("Fields")
        actionchains.double_click(fieldclick).perform()

    def verify_selectattribute(self):
        time.sleep(3)
        actionchains = ActionChains(self.driver)
        self.driver.find_element_by_name("Load : PenId").click()
        for x in range(0, 6):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(4)
        scndattr = self.driver.find_element_by_name("Assay : Score").click()
        actionchains.double_click(scndattr).perform()
        time.sleep(2)
        self.driver.find_element_by_name("OK").click()

    def raw_data_verify_Logparameter(self):
        self.driver.find_element_by_name("ChipId").click()
        actionchains = ActionChains(self.driver)
        for x in range(0, 10):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(5)
        parameter = self.driver.find_element_by_name("Assay_2 : Logparameter1").is_displayed()
        return parameter

    """testcase T42451"""

    def verify_attrinexpressioneditor(self):
        actionchains = ActionChains(self.driver)
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_NewParameter").click()
        time.sleep(3)
        fieldclick = self.driver.find_element_by_name("Fields")
        actionchains.double_click(fieldclick).perform()
        # fields = self.driver.find_elements_by_accessibility_id("Expander")
        # print(fields)
        assaycheck = self.driver.find_element_by_name("Assays").is_displayed()
        return assaycheck

    def verify_cultureattr(self):
        culturecheck = self.driver.find_element_by_name("Cultures").is_displayed()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_RawData_ParameterEditor_Close").click()
        return culturecheck

    """testcase T42452"""

    def verify_editnumericvalue(self):
        actionchains = ActionChains(self.driver)
        numeric = self.driver.find_elements_by_name("1")
        # print(numeric)
        actionchains.double_click(numeric[2]).perform()
        time.sleep(3)
        keyboard.press('2')
        click1 = self.driver.find_element_by_accessibility_id("PART_ExpressionNodeEditor")
        click1.click()
        time.sleep(4)
        verifynumeric = self.driver.find_element_by_accessibility_id("CellElement_0_4")
        changednumeric = verifynumeric.get_attribute("Name")
        return changednumeric

    def verify_changetodefault(self):
        actionchains = ActionChains(self.driver)
        time.sleep(4)
        numeric = self.driver.find_element_by_name("21")
        print(numeric)
        actionchains.double_click(numeric).perform()
        time.sleep(3)
        keyboard.press('1')
        click1 = self.driver.find_element_by_accessibility_id("PART_ExpressionNodeEditor")
        click1.click()
        time.sleep(4)
        verifynumeric = self.driver.find_element_by_accessibility_id("CellElement_0_4")
        changednumeric = verifynumeric.get_attribute("Name")
        return changednumeric

    """testcase T42214"""

    def verify_emptyrankforselection(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        time.sleep(4)
        columnempty = self.driver.find_element_by_accessibility_id("CellElement_0_1").is_selected()
        return columnempty

    def verify_loadrankforselection(self):
        columnempty = self.driver.find_element_by_accessibility_id("CellElement_1_1").is_selected()
        return columnempty

    def verify_removecheckbxselection(self):
        time.sleep(4)
        self.driver.find_element_by_accessibility_id("CellElement_0_1").click()
        self.driver.find_element_by_accessibility_id("CellElement_1_1").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GallerySettings_Apply").click()

    def verify_emptyrankfornonselection(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        time.sleep(4)
        columnempty = self.driver.find_element_by_accessibility_id("CellElement_0_1").is_selected()
        return columnempty

    def verify_loadrankfornonselection(self):
        columnempty = self.driver.find_element_by_accessibility_id("CellElement_1_1").is_selected()
        return columnempty

    def verify_defaultcheckbxselection(self):
        time.sleep(4)
        self.driver.find_element_by_accessibility_id("CellElement_0_1").click()
        self.driver.find_element_by_accessibility_id("CellElement_1_1").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GallerySettings_Apply").click()

    """testcase T42216"""

    def verify_rowheightvalue(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        verifyingraph = self.driver.find_elements_by_accessibility_id("textbox")
        print(verifyingraph)
        dropdown = verifyingraph[0].get_attribute("Value.Value")
        return dropdown

    def verify_rowheightincrease(self):
        heightincrease = self.driver.find_elements_by_accessibility_id("increase")
        heightincrease[0].click()
        self.driver.find_element_by_accessibility_id("AutomationId_GallerySettings_Apply").click()

    def verify_rowheightincreasedvalue(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        verifyingraph = self.driver.find_elements_by_accessibility_id("textbox")
        print(verifyingraph)
        dropdown = verifyingraph[0].get_attribute("Value.Value")
        time.sleep(4)
        heightincrease = self.driver.find_elements_by_accessibility_id("decrease")
        heightincrease[0].click()
        self.driver.find_element_by_accessibility_id("AutomationId_GallerySettings_Apply").click()
        return dropdown

    """testcase T42273"""

    def verify_reorderingofcolumns(self):
        columnattr = self.driver.find_elements_by_class_name("GridViewHeaderCell")
        # print(columnattr)
        time.sleep(3)
        column = columnattr[3].get_attribute("Name")
        print(column)
        return column

    def verify_columnchange(self):
        time.sleep(3)
        actionchains = ActionChains(self.driver)
        drag = self.driver.find_element_by_accessibility_id("Empty")
        drop = self.driver.find_element_by_accessibility_id("Culture")
        actionchains.drag_and_drop(drag, drop).perform()
        time.sleep(3)

    def verify_reorderingofchangedcolumns(self):
        time.sleep(4)
        columnattr = self.driver.find_elements_by_class_name("GridViewHeaderCell")
        # print(columnattr)
        time.sleep(3)
        column = columnattr[3].get_attribute("Name")
        print(column)
        return column

    """testcase T42270"""

    def verify_brightnesswindow(self):
        actionchains = ActionChains(self.driver)
        empty = self.driver.find_element_by_accessibility_id("Empty")
        actionchains.context_click(empty).perform()
        time.sleep(4)
        verify = self.driver.find_element_by_accessibility_id("root").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery").click()
        return verify

    """testcase T42219"""

    def verify_totalpencount(self):
        self.driver.find_element_by_accessibility_id("Empty").click()
        self.driver.find_element_by_accessibility_id("Empty").click()
        time.sleep(4)
        columnattr = self.driver.find_element_by_name("1758")
        time.sleep(3)
        column = columnattr.get_attribute("Name")
        self.driver.find_element_by_accessibility_id("Empty").click()
        return column

    """testcase T42223"""

    def verify_beforerejectedpens(self):
        columnattr = self.driver.find_element_by_name("Pen_2")
        time.sleep(3)
        column = columnattr.get_attribute("Name")
        return column

    def verify_afterrejectedpens(self):
        rejectclick = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Rejected")
        rejectclick[1].click()
        self.driver.find_element_by_accessibility_id("OKButton").click()
        time.sleep(5)

        try:
            columnattr = self.driver.find_element_by_name("Pen_2").is_displayed()
            return columnattr
        except:
            b = False
            return b

    """fuilter builder"""

    """testcase T42231"""

    def verify_stringtypeparameter(self):
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_DimensionSelector").click()
        time.sleep(3)
        for x in range(0, 2):
            keyboard.press('down')
        self.driver.find_element_by_name("Empty:Cell_Count").click()
        increase = self.driver.find_elements_by_accessibility_id("increase")
        increase[1].click()
        time.sleep(2)
        increase[1].click()
        time.sleep(2)
        celltypedata1 = self.driver.find_element_by_name("Pens: ").is_displayed()
        return celltypedata1

    def verify_stringtypeparameter1(self):
        celltypedata1 = self.driver.find_element_by_name("Total: ").is_displayed()
        # self.driver.find_element_by_name("Line 1").click()
        return celltypedata1

    """testcase T42233"""

    def verify_addmultiplecondition(self):
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_AddCondition").click()

        scndcond = self.driver.find_elements_by_accessibility_id("AutomationId_FilterBuilder_DimensionSelector")
        scndcond[1].click()

    def verify_scndcond(self):
        actionchains = ActionChains(self.driver)
        time.sleep(3)
        for x in range(0, 4):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()

        # time.sleep(3)
        self.driver.find_element_by_name("Load:Cell_Count_Verified").click()
        time.sleep(3)
        time.sleep(2)
        increase = self.driver.find_elements_by_accessibility_id("increase")
        increase[3].click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("VerticalLargeIncrease").click()
        time.sleep(2)
        celltypedata1 = self.driver.find_element_by_name("Pens: ").is_displayed()
        return celltypedata1

    def verify_gettotalpencount(self):
        totalcount = self.driver.find_element_by_name("1687")
        getcount = totalcount.get_attribute("Name")
        print(getcount)
        self.driver.find_element_by_accessibility_id("VerticalLargeDecrease").click()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_SaveFilter").click()
        return getcount

    def verify_openexplorer(self):
        time.sleep(3)
        self.driver.find_element_by_name("Window").click()
        time.sleep(3)
        self.driver.find_element_by_name("New").click()
        time.sleep(2)
        self.driver.find_element_by_name("Workbook Explorer").click()

    def verify_selectgalleryfilter(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_Filters").click()
        time.sleep(2)
        self.driver.find_element_by_name("filter1").click()
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery").click()
        getcount = self.driver.find_element_by_name("Visible 1687 of 1758 pens")
        verifycount = getcount.get_attribute("Name")
        return verifycount

    """testcase T42235"""

    def verify_booleancondition(self):
        actionchains = ActionChains(self.driver)
        time.sleep(3)
        for x in range(0, 5):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        self.driver.find_element_by_name("Load:Cparameter1").click()
        toggle = self.driver.find_element_by_accessibility_id(
            "AutomationId_FilterBuilder_BoolFilter_Selected").is_displayed()
        return toggle

    def verify_toggle(self):
        defaultpens = self.driver.find_element_by_name("1716")
        getdefault = defaultpens.get_attribute("Name")
        return getdefault

    def verify_toggleclick(self):
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_BoolFilter_Selected").click()
        time.sleep(4)
        changedtpens = self.driver.find_element_by_name("42")
        getcount = changedtpens.get_attribute("Name")
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_BoolFilter_Selected").click()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_SaveFilter").click()
        return getcount

    """testcase T42236"""

    def verify_savedfilter(self):
        savedfilter = self.driver.find_element_by_name("filter1").is_displayed()
        return savedfilter

    def verify_openfilterwindow(self):
        savedfilter = self.driver.find_element_by_name("filter1")
        actionchains = ActionChains(self.driver)
        actionchains.context_click(savedfilter).perform()
        time.sleep(2)
        self.driver.find_element_by_name("Edit").click()
        time.sleep(4)
        editfilter = self.driver.find_element_by_class_name("RadBusyIndicator").is_displayed()
        return editfilter

    """testcase T42385"""

    def verify_openchipfromfilter(self):
        time.sleep(3)
        actionchains = ActionChains(self.driver)
        savedfilter = self.driver.find_element_by_name("fil")
        actionchains.double_click(savedfilter).perform()

        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_Chips").click()
        time.sleep(2)
        chip = self.driver.find_elements_by_name("D37712")
        chip[1].click()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder").click()
        time.sleep(2)
        pencount = self.driver.find_element_by_name("1758")
        getsavedcount = pencount.get_attribute("Name")
        return getsavedcount

    """testcase T42237"""

    def verify_disableenablefilter(self):
        savedfilter = self.driver.find_element_by_name("filter1")
        actionchains = ActionChains(self.driver)
        actionchains.context_click(savedfilter).perform()
        time.sleep(2)
        self.driver.find_element_by_name("Edit").click()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_Chips").click()
        time.sleep(2)
        chip = self.driver.find_elements_by_name("D37712")
        chip[1].click()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder").click()
        self.driver.find_element_by_accessibility_id("HeaderCloseButton").click()
        self.driver.find_element_by_accessibility_id("HeaderDropDownMenu").click()
        self.driver.find_element_by_name("Tabbed document").click()

    def disabletoggle(self):
        toggle = self.driver.find_elements_by_accessibility_id("AutomationId_FilterBuilder_Filter_EnableDisable")
        # print(toggle)
        toggle[0].click()
        time.sleep(5)
        disablecheck = self.driver.find_elements_by_accessibility_id("AutomationId_FilterBuilder_DimensionSelector")
        check = disablecheck[0].is_enabled()
        # check = self.driver.find_elements_by_name("1756")
        # print(check)
        return check

    def verify_secondtoggledisable(self):
        toggle = self.driver.find_elements_by_accessibility_id("AutomationId_FilterBuilder_Filter_EnableDisable")
        print(toggle)
        toggle[0].click()
        time.sleep(3)
        toggle[1].click()
        time.sleep(5)
        disablecheck = self.driver.find_elements_by_accessibility_id("AutomationId_FilterBuilder_DimensionSelector")
        verify = disablecheck[1].is_enabled()
        time.sleep(3)
        toggle[1].click()
        return verify

    """testcase T42238"""

    def verify_deletefiltercond(self):
        delete = self.driver.find_elements_by_accessibility_id("AutomationId_FilterBuilder_Filter_Remove")
        delete[0].click()
        time.sleep(4)
        try:
            verify = self.driver.find_element_by_name("1756").is_displayed()
            return verify
        except:
            b = False
            return b

    def verify_getpencountafterdeletion(self):
        time.sleep(3)
        verify = self.driver.find_element_by_name("1687").is_displayed()
        return verify

    """testcase T42239"""

    def verify_editfiltername(self):
        savedfilter = self.driver.find_element_by_name("filter1")
        actionchains = ActionChains(self.driver)
        actionchains.context_click(savedfilter).perform()
        time.sleep(2)
        self.driver.find_element_by_name("Edit").click()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_FilterName").click()

    def verify_removename(self):
        actionchains = ActionChains(self.driver)
        for x in range(0, 4):
            actionchains.send_keys(Keys.BACK_SPACE).perform()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_FilterName").send_keys("editedfilter")
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_SaveFilter").click()
        close = self.driver.find_elements_by_accessibility_id("HeaderDropDownMenu")
        close[1].click()
        time.sleep(3)
        self.driver.find_element_by_name("Hide").click()

    def verify_changedname(self):
        time.sleep(3)
        getname = self.driver.find_element_by_name("editedfilter").is_displayed()
        return getname

    """testcase T42240"""

    def verify_filterclick(self):
        actionchains = ActionChains(self.driver)
        getname = self.driver.find_element_by_name("editedfilter")
        actionchains.double_click(getname).perform()
        time.sleep(4)
        filterwindow = self.driver.find_element_by_accessibility_id("scrollView").is_displayed()
        close = self.driver.find_elements_by_accessibility_id("HeaderDropDownMenu")
        close[1].click()
        time.sleep(3)
        self.driver.find_element_by_name("Hide").click()
        return filterwindow

    """testcase T42241"""

    def verify_removefilter(self):
        actionchains = ActionChains(self.driver)
        getname = self.driver.find_element_by_name("editedfilter")
        actionchains.context_click(getname).perform()
        time.sleep(3)
        self.driver.find_element_by_name("Remove").click()
        time.sleep(2)
        self.driver.find_element_by_name("OK").click()
        time.sleep(3)
        try:
            verify = self.driver.find_element_by_name("editedfilter").is_displayed()
            return verify
        except:
            a = False
            return a

    """testcase T42242"""

    def verify_customparaminfilter(self):
        actionchains = ActionChains(self.driver)
        time.sleep(3)
        for x in range(0, 10):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        verify = self.driver.find_element_by_name("Assay_2:Logparameter1").is_displayed()
        return verify

    """testcase T42243"""

    def verify_filterconditionusingparam(self):
        self.driver.find_element_by_name("Assay_2:Logparameter1").click()
        time.sleep(3)
        increase = self.driver.find_elements_by_accessibility_id("increase")
        increase[1].click()
        increase[1].click()

        changedpen = self.driver.find_element_by_name("829")
        getcount = changedpen.get_attribute("Name")
        return getcount

    """testcase T42244"""

    def verify_filterpen(self):
        rejectclick = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Rejected")
        rejectclick[1].click()
        self.driver.find_element_by_accessibility_id("OKButton").click()
        time.sleep(3)

    def verify_selectfilter(self):
        self.driver.find_element_by_name("PenState").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("ThreeStateSwitcher_Rejected").click()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_SaveFilter").click()

    def verif_filteringallery(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_Filters").click()
        time.sleep(3)
        self.driver.find_element_by_name("filterpen").click()
        time.sleep(5)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery").click()
        try:
            getcount = self.driver.find_element_by_name("Visible 1 of 1758 pens").is_displayed()
            return getcount
        except:
            b = False
            return b

    """testcase T42245"""

    def verify_validationmessage(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddNewFilter").click()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_SaveFilter").click()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_FilterName").click()
        time.sleep(2)
        verify = self.driver.find_element_by_name("Name cannot be empty").is_displayed()
        pr = self.driver.find_elements_by_accessibility_id("HeaderDropDownMenu")
        # print(pr)
        pr[1].click()
        self.driver.find_element_by_name("Hide").click()
        return verify

    """testcase T42370"""

    def verify_changegraph(self):
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_2DFilter_XAxis_Values").click()
        time.sleep(2)
        self.driver.find_element_by_name("Empty:Pen_Id").click()
        time.sleep(2)
        try:
            verify = self.driver.find_element_by_name("1000").is_displayed()
            return verify
        except:
            b = False
            return b

    """testcase T42371"""

    # def verify_zoominggraph(self):
    #     actionchains = ActionChains(self.driver)
    #     self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_2DFilter_Chart").click()
    #     time.sleep(2)
    #     for x in range(0, 4):
    #         actionchains.send_keys(Keys.CONTROL, Keys.ADD).perform()
    #         # self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_2DFilter_Chart").send_keys(
    #         #     Keys.CONTROL, Keys.ADD)

    """testcase T42372"""

    def verify_expand2dfilter(self):
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_2DFilter_Expand").click()
        time.sleep(3)
        verify = self.driver.find_element_by_class_name("ExpandTwoDFilterControl").is_displayed()
        closeexpand = self.driver.find_elements_by_accessibility_id("PART_Close")
        print(closeexpand)
        closeexpand[1].click()
        return verify

    """testcase T42374"""

    def verify_2Dconditiontogallery(self):
        pens = self.driver.find_elements_by_name("0")
        a = pens[3].get_attribute("Name")
        print(a)
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_SaveFilter").click()
        time.sleep(2)
        return a

    def verify_filteringallery(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_Filters").click()
        time.sleep(3)
        self.driver.find_element_by_name("filter2").click()
        time.sleep(5)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery").click()
        try:
            getcount = self.driver.find_element_by_name("Visible 0 of 1758 pens").is_displayed()
            return getcount
        except:
            b = False
            return b

    """testcase T42396"""

    def verify_dragtofilter(self):
        global actionchains
        actionchains = ActionChains(self.driver)
        source = self.driver.find_element_by_name("D37712")
        destination = self.driver.find_element_by_name("Filters")
        time.sleep(2)
        actionchains.drag_and_drop(source, destination).perform()
        time.sleep(3)
        filterwindow = self.driver.find_element_by_accessibility_id("scrollView").is_displayed()
        return filterwindow

    def verify_drggedchip(self):
        verifychip = self.driver.find_element_by_name("D37712").is_displayed()
        close = self.driver.find_elements_by_accessibility_id("HeaderDropDownMenu")
        close[1].click()
        time.sleep(3)
        self.driver.find_element_by_name("Hide").click()
        return verifychip
        # select = Select(self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_Chips"))
        # select.first_selected_option.get_attribute("value")
        # return verify

    """testcase T42437"""

    def verify_changesin1D(self):
        self.driver.find_element_by_name("PenState").click()
        getcount = self.driver.find_element_by_name("1757")
        pen = getcount.get_attribute("Name")
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_DimensionSelector").click()
        self.driver.find_element_by_name("Empty:Cell_Count_Verified").click()
        time.sleep(2)
        inc = self.driver.find_elements_by_accessibility_id("increase")
        inc[1].click()
        inc[1].click()
        time.sleep(4)
        getcount1 = self.driver.find_element_by_name("1756")
        pen1 = getcount1.get_attribute("Name")

        if pen == pen1:
            return False
        else:
            return True

    """testcase T42246"""

    def verify_decreasinginmultiplecond(self):
        # self.driver.find_element_by_name("Line 1").click()
        getcount = self.driver.find_element_by_name("1756")
        pen = getcount.get_attribute("Name")
        print(pen)
        getcount1 = self.driver.find_element_by_name("1687")
        pen1 = getcount1.get_attribute("Name")
        print(pen1)
        if int(pen1) < int(pen):
            return True
        else:
            return False

    """testcase 42450"""

    def verify_removefiltergallery(self):
        actionchains = ActionChains(self.driver)
        getname = self.driver.find_element_by_name("filterpen")
        actionchains.context_click(getname).perform()
        time.sleep(3)
        self.driver.find_element_by_name("Remove").click()
        time.sleep(2)
        self.driver.find_element_by_name("OK").click()

    def verify_removedfilter(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_Filters").click()
        time.sleep(3)
        try:
            verify = self.driver.find_element_by_name("filterpen").is_displayed()
            return verify
        except:
            b = False
            return b

    """testcase T42456"""

    def click(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery").click()

    def verify_filterdroprefresh(self):
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_Chips").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddChipFolder(s)").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddChipFolder(s)").click()
        self.driver.find_element_by_name("Desktop (pinned)").click()
        self.driver.find_element_by_name("D50238").click()
        # driver.find_element_by_accessibility_id("0").click()
        self.driver.find_element_by_accessibility_id("1").click()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_Chips").click()
        value = self.driver.find_elements_by_name(
            "Tejas.Infrastructure.Behaviors.SelectableObject`1[Tejas.Services.Entities.IChip]")
        # value.select_by_index(1)
        verify = value[1].is_displayed()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder").click()
        return verify

    def verify_closefilter(self):
        time.sleep(2)
        close = self.driver.find_elements_by_accessibility_id("HeaderDropDownMenu")
        close[1].click()
        time.sleep(2)
        # actionchains = ActionChains(self.driver)
        # actionchains.context_click(close[1]).perform()
        self.driver.find_element_by_name("Hide").click()

    def remove_2ndchip(self):
        time.sleep(3)
        actionchains = ActionChains(self.driver)
        chip = self.driver.find_element_by_name("D50238")
        actionchains.context_click(chip).perform()
        self.driver.find_element_by_name("Remove chip(s)").click()
        self.driver.find_element_by_accessibility_id("OKButton").click()
        try:
            a = self.driver.find_element_by_name("D50238").is_displayed()
            return a
        except:
            b = False
            return b

    """testcase T42458"""

    def verify_filterstuck(self):
        time.sleep(5)
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_Chips").click()
        self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder").click()
        verify = self.driver.find_element_by_accessibility_id("AutomationId_FilterBuilder_Chips").is_enabled()
        return verify

    """testcase T42256"""

    def remove_custom_parameter(self):
        self.driver.find_element_by_name("ChipId").click()
        time.sleep(1)
        self.driver.find_element_by_name("PenId").click()
        actionchains = ActionChains(self.driver)
        for x in range(0, 10):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        parameter = []
        parameter = self.driver.find_elements_by_accessibility_id("AutomationId_RawData_RemoveParameter")
        customparam = len(parameter)
        parameter[customparam - 1].click()
        self.driver.find_element_by_accessibility_id("OKButton").click()
        return len(parameter)

    """testcase 42412"""

    def verify_Addedfilterforexlorer(self):
        time.sleep(3)
        firststfilter = self.driver.find_element_by_name("fil").is_displayed()
        return firststfilter

    def verify_Addedfilter1forexplorer(self):
        firststfilter = self.driver.find_element_by_name("filter2").is_displayed()
        return firststfilter

    def verify_Addedfilterforgallery(self):
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_Filters").click()
        firststfilter = self.driver.find_element_by_name("fil").is_displayed()
        return firststfilter

    def verify_Addedfilter1forgallery(self):
        firstfilter = self.driver.find_element_by_name("filter2").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery").click()
        return firstfilter

    """testcase 42224"""

    def verify_filterredcount(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_Filters").click()
        time.sleep(3)
        self.driver.find_element_by_name("fil").click()
        time.sleep(5)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery").click()
        try:
            getcount = self.driver.find_element_by_name("Visible 1756 of 1758 pens").is_displayed()
            return getcount
        except:
            b = False
            return b

    """testcase 42266"""

    def verify_removegalleryfilter(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_Filters").click()
        time.sleep(3)
        self.driver.find_element_by_name("fil").click()
        time.sleep(5)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery").click()
        try:
            getcount = self.driver.find_element_by_name("Visible 1756 of 1758 pens").is_displayed()
            return getcount
        except:
            b = False
            return b

    """testcase T42268"""

    def verify_changepenstate(self):
        selectpen = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Selected")
        selectpen[0].click()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_ExportMenu_ExportToCSV").click()
        time.sleep(3)
        verify = self.driver.find_element_by_name("Export to CSV").is_displayed()
        time.sleep(2)
        close = self.driver.find_elements_by_accessibility_id("PART_Close")
        print(close)
        close[1].click()
        undecided = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Undecided")
        undecided[0].click()
        return verify

    """testcase T42269"""

    def verify_savedpenstate(self):
        pens = []
        pens = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Selected")
        for x in range(1, 3):
            pens[x].click()
        time.sleep(3)

    def verify_selectedpen(self):
        penstate = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Selected")
        flag = penstate[1].is_selected()
        time.sleep(2)
        # undecided = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Undecided")
        # undecided[1].click()
        # undecided[2].click()
        return flag

    """testcase T42292"""

    def verify_validationattrmessage(self):
        element = []
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        self.driver.find_element_by_accessibility_id("VerticalLargeIncrease").click()
        element = self.driver.find_elements_by_accessibility_id("AutomationId_GallerySettings_ColumnFooters")
        actionchains = ActionChains(self.driver)
        actionchains.move_to_element_with_offset(element[6], 50, 1)
        actionchains.click()
        actionchains.perform()
        for x in range(0, 4):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(3)

    def verify_displayedmessage(self):
        actionchains = ActionChains(self.driver)
        ele = self.driver.find_element_by_name("Culture: CellCountVerified")
        hover = actionchains.move_to_element(ele)
        hover.perform()
        time.sleep(3)
        verify = self.driver.find_element_by_name("You can not select more than 5 items").is_displayed()
        return verify

    """----------------------------------------------------------------------------"""

    def deleteworkbook(self):
        desktop = str(os.path.join(Path.home(), "Desktop\D37712"))
        try:
            if os.path.isfile(desktop + "\workbooktest.workbook"):
                os.remove(desktop + "\workbooktest.workbook")
        except:
            print("workbook file not found")

    """----------------------------------------------------------------------------"""
    """testcase T42387"""

    def verify_exporttoarchive(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("CellElement_6_1").click()
        self.driver.find_element_by_name("Cancel").click()
        time.sleep(2)
        archive = self.driver.find_element_by_accessibility_id("AutomationId_Gallery_ExportMenu").is_displayed()
        return archive

    def verify_exporttoarchiveclick(self):
        archive = self.driver.find_element_by_accessibility_id("AutomationId_Gallery_ExportMenu")
        archive.click()
        verifyitem = self.driver.find_element_by_name("Images only").is_displayed()
        return verifyitem

    def verify_archiveitem1(self):
        verifyitem1 = self.driver.find_element_by_name("Images Per Pen").is_displayed()
        return verifyitem1

    def verify_archiveitem2(self):
        verifyitem2 = self.driver.find_element_by_name("Images Per Image Sequence").is_displayed()
        return verifyitem2

    def verify_archiveitem3(self):
        verifyitem3 = self.driver.find_element_by_name("Images and CSVs").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_ExportMenu").click()
        return verifyitem3

    """testcase T42309"""

    def verify_exportselectedthumb(self):
        actionchains = ActionChains(self.driver)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_ExportMenu").click()
        time.sleep(2)
        self.driver.find_element_by_name("Images only").click()
        saveas = self.driver.find_element_by_name("Save As").is_displayed()
        return saveas

    def verify_exportdefaultfilename(self):
        # actionchains = ActionChains(self.driver)
        time.sleep(3)
        self.driver.find_element_by_class_name("Edit").click()
        for x in range(0, 40):
            keyboard.press('backspace')
        self.driver.find_element_by_class_name("Edit").send_keys("ExportThumbnails")
        self.driver.find_element_by_name("Save").click()
        time.sleep(2)
        try:
            time.sleep(3)
            data = self.driver.find_element_by_name("Save As")
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            self.driver.find_element_by_name("Yes").click()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_ExportMenu").click()
        self.driver.find_element_by_name("Images only").click()
        time.sleep(3)
        verify = self.driver.find_element_by_name("ExportThumbnails.zip").is_displayed()
        time.sleep(3)
        self.driver.find_element_by_name("Cancel").click()
        return verify

    def verify_datainzip(self):
        desktop = str(os.path.join(Path.home(), "Desktop\D50238"))
        print(desktop)
        verifyfile = path.exists(desktop)
        print(verifyfile)
        if verifyfile == True:
            print("yes")
            dir = "D37712_Pen_4_Assay_2_0.jpeg"

            z = zipfile.ZipFile(desktop + "\ExportThumbnails.zip")
            if dir in z.namelist():
                return True
            else:
                return False

    """testcase T42388"""

    def verify_penidforexporting(self):
        undecided = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Undecided")
        undecided[1].click()
        undecided[2].click()
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_ExportMenu").click()
        time.sleep(2)
        self.driver.find_element_by_name("Images only").click()
        time.sleep(3)
        penidwindow = self.driver.find_element_by_name("Enter Pen Ids").is_displayed()
        return penidwindow

    def verify_rangeforpenid(self):
        self.driver.find_element_by_class_name("TextBox").click()
        time.sleep(2)
        self.driver.find_element_by_class_name("TextBox").send_keys("3")
        self.driver.find_element_by_name("OK").click()
        self.driver.find_element_by_class_name("Edit").click()

    def verify_saverangefile(self):
        for x in range(0, 39):
            keyboard.press('backspace')

        self.driver.find_element_by_class_name("Edit").send_keys("ExportThumbnailrange")
        self.driver.find_element_by_name("Save").click()
        time.sleep(2)
        try:
            time.sleep(3)
            data = self.driver.find_element_by_name("Save As")
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            self.driver.find_element_by_name("Yes").click()

        time.sleep(3)

    def verify_rangeinzip(self):
        desktop = str(os.path.join(Path.home(), "Desktop\D50238"))
        print(desktop)
        verifyfile = path.exists(desktop)
        print(verifyfile)
        if verifyfile == True:
            print("yes")
            dir = "D37712_Pen_3_Assay_0.jpeg"

            z = zipfile.ZipFile(desktop + "\ExportThumbnailrange.zip")
            if dir in z.namelist():
                return True
            else:
                return False

    def verify_onlyrangeinzip(self):
        desktop = str(os.path.join(Path.home(), "Desktop\D50238"))
        print(desktop)
        verifyfile = path.exists(desktop)
        print(verifyfile)
        if verifyfile == True:
            print("yes")
            dir = "D37712_Pen_2_Assay_0.jpeg"

            z = zipfile.ZipFile(desktop + "\ExportThumbnailrange.zip")
            if dir in z.namelist():
                return False
            else:
                return True

    """testcase T42310"""

    def verify_selectedcolumn1(self):
        verify = self.driver.find_element_by_name("Empty").is_displayed()
        return verify

    def verify_selectedcolumn2(self):
        verify = self.driver.find_element_by_name("Load").is_displayed()
        return verify

    def verify_unselectcolumn(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("CellElement_0_0").click()
        self.driver.find_element_by_accessibility_id("CellElement_1_0").click()
        time.sleep(2)
        self.driver.find_element_by_name("Apply").click()

    def verify_unselectedcolumn1(self):
        try:
            verify = self.driver.find_element_by_name("Empty").is_displayed()
            return verify
        except:
            b = False
            return b

    def verify_unselectedcolumn2(self):
        try:
            verify = self.driver.find_element_by_name("Load").is_displayed()
            return verify
        except:
            b = False
            return b

    def verify_changecoltodefault(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("CellElement_0_0").click()
        self.driver.find_element_by_accessibility_id("CellElement_1_0").click()
        time.sleep(2)
        self.driver.find_element_by_name("Apply").click()

    """testcase T42311"""

    def verify_penrejectiondisabled(self):
        rejectclick = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Rejected")
        rejectclick[1].click()
        self.driver.find_element_by_name("Cancel").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GallerySettings_PenRejectApproval").click()
        self.driver.find_element_by_name("Apply").click()
        rejectclick = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Rejected")
        rejectclick[1].click()
        time.sleep(2)
        try:
            verify = self.driver.find_element_by_name("CONFIRMATION").is_displayed()
            return verify
        except:
            b = False
            return b

    def verify_rejectedpen(self):
        time.sleep(2)
        try:
            sort = self.driver.find_element_by_name("Pen_3").is_displayed()
            return sort
        except:
            b = False
            return b

    """testcase T42312"""

    def verify_rejectionmessage(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GallerySettings_PenRejectApproval").click()
        self.driver.find_element_by_name("Apply").click()
        rejectclick = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Rejected")
        rejectclick[1].click()
        time.sleep(3)
        verify = self.driver.find_element_by_name("CONFIRMATION").is_displayed()
        self.driver.find_element_by_name("OK").click()
        return verify

    """testcase T42313"""

    def verify_rejectallpens(self):
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        rejection = self.driver.find_element_by_accessibility_id(
            "AutomationId_GallerySettings_PenRejectApproval").is_selected()
        self.driver.find_element_by_name("Apply").click()
        return rejection

    def verify_clickrejectpen(self):
        rejectclick = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Rejected")
        rejectclick[0].click()
        time.sleep(3)
        verify = self.driver.find_element_by_name("CONFIRMATION").is_displayed()
        self.driver.find_element_by_name("OK").click()
        return verify

    def verify_rejectedpen1(self):
        time.sleep(2)
        try:
            sort = self.driver.find_element_by_name("Pen_4").is_displayed()
            return sort
        except:
            b = False
            return b

    def verify_rejectedpen2(self):
        time.sleep(2)
        try:
            sort = self.driver.find_element_by_name("Pen_5").is_displayed()
            return sort
        except:
            b = False
            return b

    """testcase T42314"""

    def verify_cancelpenreject(self):
        rejectclick = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Rejected")
        rejectclick[1].click()
        time.sleep(3)
        verify = self.driver.find_element_by_name("Cancel").is_displayed()
        self.driver.find_element_by_name("Cancel").click()
        return verify

    def verify_cancelrejectedpen(self):
        time.sleep(2)
        try:
            sort = self.driver.find_element_by_name("Pen_5").is_displayed()
            return sort
        except:
            b = False
            return b

    """testcase T42415"""

    def verify_archive1000(self):
        undecided = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Selected")
        undecided[0].click()
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_ExportMenu").click()
        self.driver.find_element_by_name("Images only").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("Edit").click()
        for x in range(0, 39):
            keyboard.press('backspace')

        self.driver.find_element_by_class_name("Edit").send_keys("ExportThumbnail1000")
        self.driver.find_element_by_name("Save").click()
        time.sleep(2)
        try:
            time.sleep(3)
            data = self.driver.find_element_by_name("Save As")
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            self.driver.find_element_by_name("Yes").click()

        time.sleep(3)

    def verify_range1000inzip(self):
        desktop = str(os.path.join(Path.home(), "Desktop\D50238"))
        print(desktop)
        verifyfile = path.exists(desktop)
        print(verifyfile)
        if verifyfile == True:
            print("yes")
            # dir = "D37712_Pen_2_Assay_0.jpeg"

            z = zipfile.ZipFile(desktop + "\ExportThumbnail1000.zip")

            if len(z.namelist()) > 1000:
                return True
            else:
                return False

    """testcase T42455"""

    def verify_unselectpenarchive(self):
        undecided = self.driver.find_elements_by_accessibility_id("ThreeStateSwitcher_Undecided")
        undecided[0].click()
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_ExportMenu").click()
        self.driver.find_element_by_name("Images only").click()
        self.driver.find_element_by_class_name("TextBox").click()
        time.sleep(2)
        self.driver.find_element_by_class_name("TextBox").send_keys("3")
        self.driver.find_element_by_name("OK").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("Edit").click()
        for x in range(0, 39):
            keyboard.press('backspace')

        self.driver.find_element_by_class_name("Edit").send_keys("ExportThumbnailrejectpen")
        self.driver.find_element_by_name("Save").click()
        time.sleep(2)
        try:
            time.sleep(3)
            data = self.driver.find_element_by_name("Save As")
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            self.driver.find_element_by_name("Yes").click()

        time.sleep(3)

    def verify_unselectinzip(self):
        desktop = str(os.path.join(Path.home(), "Desktop\D50238"))
        print(desktop)
        verifyfile = path.exists(desktop)
        print(verifyfile)
        if verifyfile == True:
            print("yes")
            dir = "D37712_Pen_3_Assay_0.jpeg"

            z = zipfile.ZipFile(desktop + "\ExportThumbnailrejectpen.zip")

            if dir in z.namelist():
                return True
            else:
                return False

    """testcase T42457"""

    def verify_headersortingpersist(self):
        actionchains = ActionChains(self.driver)
        self.driver.find_element_by_accessibility_id("AutomationId_Gallery_OpenSettings").click()
        time.sleep(2)
        combo = self.driver.find_elements_by_accessibility_id("AutomationId_GallerySettings_ColumnFooters")
        combo[1].click()
        time.sleep(2)
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actionchains.send_keys(Keys.RETURN).perform()
        # self.driver.find_element_by_name("CellCountVerified").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GallerySettings_Apply").click()

    def verify_defaultcolumnsorting(self):
        time.sleep(4)
        defaultcol = self.driver.find_element_by_name("3").is_displayed()
        return defaultcol

    def verify_changedcolumnsorting(self):
        self.driver.find_element_by_name("Load").click()
        time.sleep(4)
        self.driver.find_element_by_name("Load").click()
        defaultcol = self.driver.find_element_by_name("1").is_displayed()
        return defaultcol

    """testcase T42277"""

    def verify_xaxislabels(self):
        verify = self.driver.find_element_by_name("X:").is_displayed()
        return verify

    def verify_yaxislabels(self):
        verify = self.driver.find_element_by_name("Y:").is_displayed()
        return verify

    """testcase T42278"""

    def verify_xaxisdropdown(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_XAxis_Values").click()
        verify = self.driver.find_element_by_name("Empty:Pen_Id").is_displayed()
        return verify

    def verify_xaxisdropdown1(self):
        verify = self.driver.find_element_by_name("Empty:Device_Id").is_displayed()
        return verify

    def verify_xaxisdropdown2(self):
        verify = self.driver.find_element_by_name("Empty:Cell_Count_Verified").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_XAxis_Values").click()
        return verify

    def verify_yaxisdropdown(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_YAxis_Values").click()
        verify = self.driver.find_element_by_name("Empty:Pen_Id").is_displayed()
        return verify

    def verify_yaxisdropdown1(self):
        verify = self.driver.find_element_by_name("Empty:Device_Id").is_displayed()
        return verify

    def verify_yaxisdropdown2(self):
        verify = self.driver.find_element_by_name("Empty:Cell_Count_Verified").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_XAxis_Values").click()
        return verify

    """testcase T42279"""

    def verify_groupbyoption(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_Color").click()
        verify = self.driver.find_element_by_name("Pen State").is_displayed()
        return verify

    def verify_groupbyoption1(self):
        verify = self.driver.find_element_by_name("Empty:Device_Id").is_displayed()
        return verify

    def verify_groupbyoption2(self):
        verify = self.driver.find_element_by_name("Empty:Cell_Count_Verified").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_XAxis_Values").click()
        return verify

    """testcase T42280"""

    def verify_changegroupby(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_Color").click()
        self.driver.find_element_by_name("Empty:Device_Id").click()
        time.sleep(4)
        legend = self.driver.find_element_by_name(
            "Telerik.Windows.Controls.Legend.LegendItem").is_displayed()
        return legend

    """testcase T42288"""

    def verify_penplotlegends(self):
        legend = self.driver.find_elements_by_name("D37712")
        print(legend)
        beforelegend = self.driver.find_element_by_name("1000").is_displayed()
        time.sleep(3)
        legend[2].click()
        return beforelegend

    def verify_penplotlegends1(self):
        try:
            beforelegend = self.driver.find_element_by_name("1000").is_displayed()
            return beforelegend
        except:
            v = False
            return v

    def verify_gettodefault(self):
        legend = self.driver.find_elements_by_name("D37712")
        legend[2].click()

    """testcase T42317"""

    def verify_linktogallery(self):
        gallerylink = self.driver.find_element_by_name("Link-To-Gallery").is_displayed()
        return gallerylink

    def verify_galleryredirecting(self):
        self.driver.find_element_by_name("Link-To-Gallery").click()
        verifygallery = self.driver.find_element_by_name("Gallery").is_displayed()
        return verifygallery

    def close_link(self):
        self.driver.find_element_by_name("Link-To-Gallery").click()

    """testcase T42319"""

    def verify_linktorawdata(self):
        rawdatalink = self.driver.find_element_by_name("Link-To-Raw-Data").is_displayed()
        return rawdatalink

    def verify_rawdataredirecting(self):
        self.driver.find_element_by_name("Link-To-Raw-Data").click()
        verifyrawdata = self.driver.find_element_by_name("Raw Data").is_displayed()
        return verifyrawdata

    def close_rawlink(self):
        self.driver.find_element_by_name("Link-To-Raw-Data").click()

    """testcase T42322"""

    def verify_exportgraph(self):
        verify = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Export").is_displayed()
        return verify

    def verify_savedialog(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Export").click()
        verify = self.driver.find_element_by_name("Save As").is_displayed()
        return verify

    def verify_savefile(self):
        self.driver.find_element_by_name("Save").click()
        time.sleep(2)
        try:
            time.sleep(3)
            data = self.driver.find_element_by_name("Save As")
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            self.driver.find_element_by_name("Yes").click()
        verify = self.driver.find_element_by_name("CONFIRMATION").is_displayed()
        self.driver.find_element_by_name("Cancel").click()
        return verify

    def verify_savedimage(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Export").click()
        verify = self.driver.find_element_by_name("X_Empty_Pen_Id-Y_Empty_Cell_Count_Verified.png").is_displayed()
        time.sleep(3)
        self.driver.find_element_by_name("Cancel").click()
        return verify

    """testcase 42323"""

    def verify_graphsetting(self):
        verify = self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Settings").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Settings").click()
        return verify

    def verify_settingelement1(self):
        verify = self.driver.find_element_by_name("Shape: ").is_displayed()
        return verify

    def verify_settingelement2(self):
        verify = self.driver.find_element_by_name("Fill: ").is_displayed()
        return verify

    def verify_settingelement3(self):
        verify = self.driver.find_element_by_name("Height: ").is_displayed()
        return verify

    def verify_settingelement4(self):
        verify = self.driver.find_element_by_name("Width: ").is_displayed()
        return verify

    def verify_settingelement5(self):
        verify = self.driver.find_element_by_name("Stroke: ").is_displayed()
        return verify

    def verify_settingelement6(self):
        verify = self.driver.find_element_by_name("Stroke Thickness: ").is_displayed()
        return verify

    def verify_settingelement7(self):
        verify = self.driver.find_element_by_name("Palette: ").is_displayed()
        return verify

    def verify_settingelement8(self):
        verify = self.driver.find_element_by_name("Selection Color: ").is_displayed()
        return verify

    def verify_attributes(self):
        verify = self.driver.find_element_by_name("Tooltip Attributes").is_displayed()
        return verify

    def verify_preview(self):
        verify = self.driver.find_element_by_name("Preview").is_displayed()
        return verify

    def verify_okbutton(self):
        verify = self.driver.find_element_by_name("OK").is_displayed()
        self.driver.find_element_by_name("OK").click()
        return verify

    """testcase T42324"""

    def verify_selecttooltipattr(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Settings").click()
        self.driver.find_element_by_name("Empty:Pen_Id").click()
        time.sleep(3)
        verify = self.driver.find_element_by_name("Empty:Pen_Id").is_selected()
        return verify

    def verify_selecttooltipattr1(self):
        self.driver.find_element_by_name("Empty:Device_Id").click()
        time.sleep(3)
        verify = self.driver.find_element_by_name("Empty:Pen_Id").is_selected()
        return verify

    def verify_selecttooltipattr2(self):
        self.driver.find_element_by_name("Empty:Cell_Count_Verified").click()
        time.sleep(3)
        verify = self.driver.find_element_by_name("Empty:Cell_Count_Verified").is_selected()
        return verify

    def verify_selecttooltipattr3(self):
        self.driver.find_element_by_name("Empty:Cell_Count").click()
        time.sleep(3)
        verify = self.driver.find_element_by_name("Empty:Cell_Count").is_selected()
        return verify

    def verify_selecttooltipattr4(self):
        self.driver.find_element_by_name("Empty:Time_Stamp").click()
        time.sleep(3)
        verify = self.driver.find_element_by_name("Empty:Time_Stamp").is_selected()
        return verify

    def verify_selecttooltipattr5(self):
        actionchains = ActionChains(self.driver)
        ele = self.driver.find_element_by_name("Load:Pen_Id")
        actionchains.move_to_element(ele).perform()
        verify = self.driver.find_element_by_name("You can not select more than 5 items").is_displayed()
        self.driver.find_element_by_name("OK").click()
        return verify

    def verify_scatterpoints(self):
        actionchains = ActionChains(self.driver)
        point = self.driver.find_elements_by_class_name("ContentPresenter")
        time.sleep(2)
        point[28].click()
        actionchains.move_to_element(point[30]).perform()
        time.sleep(3)
        verify = self.driver.find_element_by_name("Empty:Time_Stamp").is_displayed()
        return verify

    """testcase T42328"""

    def verify_savegraphname(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Save").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_SaveGraph_Name").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_SaveGraph_Name").send_keys(
            "graphbuilder")
        verify = self.driver.find_element_by_name("Save Graph").is_displayed()
        return verify

    def verify_savegaph(self):
        self.driver.find_element_by_name("Apply").click()
        time.sleep(2)

    """testcase T42329"""

    def verify_emptygraphname(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Save").click()
        verify = self.driver.find_element_by_name("Save Graph").is_displayed()
        return verify

    def verify_savegaphwindow(self):
        self.driver.find_element_by_name("Apply").click()
        time.sleep(2)
        verify = self.driver.find_element_by_name("Name can not be empty.").is_displayed()
        time.sleep(2)
        self.driver.find_element_by_name("Cancel").click()
        return verify

    """testcase T42330"""

    def verify_graphinworkbook(self):
        verify = self.driver.find_element_by_name("graphbuilder").is_displayed()
        return verify

    def verify_opensavedgraph(self):
        actionchains = ActionChains(self.driver)
        graph = self.driver.find_element_by_name("graphbuilder")
        actionchains.double_click(graph).perform()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder").click()
        frstattr = self.driver.find_element_by_name("Empty:Pen_Id").is_displayed()
        return frstattr

    def verify_attr(self):
        frstattr = self.driver.find_element_by_name("Empty:Cell_Count_Verified").is_displayed()
        return frstattr

    """testcase T42331"""

    def verify_changesavedgraph(self):
        actionchains = ActionChains(self.driver)
        graph = self.driver.find_element_by_name("graphbuilder")
        actionchains.context_click(graph).perform()
        self.driver.find_element_by_name("Edit").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_Color").click()
        self.driver.find_element_by_name("Pen State").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Save").click()

    def verify_openchangedgraph(self):
        actionchains = ActionChains(self.driver)
        graph = self.driver.find_element_by_name("graphbuilder")
        actionchains.double_click(graph).perform()
        try:
            frstattr = self.driver.find_element_by_name("Empty:Device_Id").is_displayed()
            # self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_Color").click()
            return frstattr
        except:
            b = False
            return b

    """testcase T42333"""

    def verify_removegraphconf(self):
        actionchains = ActionChains(self.driver)
        graph = self.driver.find_element_by_name("graphbuilder")
        actionchains.context_click(graph).perform()
        self.driver.find_element_by_name("Remove").click()
        time.sleep(2)
        verify = self.driver.find_element_by_name("CONFIRMATION").is_displayed()
        self.driver.find_element_by_name("OK").click()
        return verify

    def verify_removedgraph(self):
        try:
            graph = self.driver.find_element_by_name("graphbuilder").is_displayed()
            return graph
        except:
            b = False
            return b

    """testcase T42334"""

    def verify_stringtypevalidation(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_XAxis_Values").click()
        self.driver.find_element_by_name("Empty:Device_Id").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_ScatterPlot_YAxis_Values").click()
        self.driver.find_element_by_name("Empty:Cell_Count").click()
        time.sleep(1)
        # verifymsg=self.driver.find_element_by_name("Both X and Y cannot be string type").is_displayed()
        # return verifymsg

    """testcase T42337"""

    def verify_changebinquantity(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Histogram_BinCounts").click()

    def verify_bincount(self):
        actionchains = ActionChains(self.driver)
        for x in range(0, 4):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        verify = self.driver.find_element_by_name("10").is_displayed()
        self.driver.find_element_by_name("10").click()
        return verify

    def verify_changedbinvalue(self):
        verify = self.driver.find_element_by_name("0..0.3").is_displayed()
        return verify

    """testcase T42338"""

    def verify_nullablevalues(self):
        verify = self.driver.find_element_by_name("Show nullable values").is_displayed()
        self.driver.find_element_by_name("Show nullable values").click()
        return verify

    def verify_changedtonull(self):
        verify = self.driver.find_element_by_name("Null").is_displayed()
        return verify

    """testcase T42339"""

    def verify_exporthistogram(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Export").click()
        verify = self.driver.find_element_by_name("Save As").is_displayed()
        return verify

    def verify_savegraph(self):
        self.driver.find_element_by_name("Save").click()
        time.sleep(2)
        try:
            time.sleep(3)
            data = self.driver.find_element_by_name("Save As")
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            self.driver.find_element_by_name("Yes").click()
        verify = self.driver.find_element_by_name("CONFIRMATION").is_displayed()
        self.driver.find_element_by_name("Cancel").click()
        return verify

    """testcase 42342"""

    def verify_edithistogram(self):
        actionchains = ActionChains(self.driver)
        open = self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_ContextMenu_ElementsTree_Element_Graph1")
        actionchains.context_click(open).perform()
        self.driver.find_element_by_name("Edit").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Histogram_BinCounts").click()
        self.driver.find_element_by_name("6").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Save").click()

    def verify_changedhistogram(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Histogram_BinCounts").click()
        time.sleep(2)
        verify = self.driver.find_element_by_name("6").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder").click()
        return verify

    """testcase T42343"""

    def verify_removehistogram(self):
        actionchains = ActionChains(self.driver)
        open = self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_ContextMenu_ElementsTree_Element_Graph1")
        actionchains.context_click(open).perform()
        self.driver.find_element_by_name("Remove").click()
        self.driver.find_element_by_name("OK").click()

    def verify_removedhistogram(self):
        try:
            verify = self.driver.find_element_by_name("Graph1").is_displayed()
            return verify

        except:
            b = False
            return b

    """testcase T42345"""

    def verify_linkgallery(self):
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Histogram_XAxis_Values").click()
        self.driver.find_element_by_name("Empty:Cell_Count_Verified").click()
        self.driver.find_element_by_accessibility_id("AutomationId_GraphBuilder_Histogram_BinCounts").click()
        self.driver.find_element_by_name("6").click()

    """Settings"""
    """testcase T42294"""

    def verify_opensettings(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_File").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_Settings").click()
        time.sleep(2)

    def verify_colortheme(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_Theme_PrimaryColorSchemes").click()
        verify = self.driver.find_element_by_name("Dark").is_displayed()
        return verify

    def verify_primaryoption(self):
        verify = self.driver.find_element_by_name("Light").is_displayed()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_Theme_PrimaryColorSchemes").click()
        return verify

    def verify_scndrycolortheme(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_Theme_SecondaryColorSchemes").click()
        verify = self.driver.find_element_by_name("Blue").is_displayed()
        return verify

    def verify_secondaryoption(self):
        verify = self.driver.find_element_by_name("Orange").is_displayed()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_Theme_SecondaryColorSchemes").click()
        # self.driver.find_element_by_name("Apply").click()
        return verify

    """testcase T42379"""

    def verify_exportsettings(self):
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_AppLevel_Export").click()
        saveas = self.driver.find_element_by_name("Save As").is_displayed()
        return saveas

    def verify_saveexportsetting(self):
        actionchains = ActionChains(self.driver)
        time.sleep(3)
        self.driver.find_element_by_class_name("Edit").click()
        for x in range(0, 6):
            actionchains.send_keys(Keys.ARROW_RIGHT).perform()

        for x in range(0, 69):
            keyboard.press('backspace')
        time.sleep(2)
        self.driver.find_element_by_class_name("Edit").send_keys("Assay Analyzer Version 20191129.2")
        time.sleep(2)
        self.driver.find_element_by_name("Save").click()
        time.sleep(2)
        try:
            time.sleep(3)
            data = self.driver.find_element_by_name("Save As")
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            self.driver.find_element_by_name("Yes").click()

    def verify_exportconfirmation(self):
        verify = self.driver.find_element_by_name(
            "Assay Analyzer settings have been successfully exported").is_displayed()
        self.driver.find_element_by_name("OK").click()
        return verify

    """testcase T42378"""

    def verify_importsettings(self):
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_AppLevel_Import").click()
        saveas = self.driver.find_element_by_name("Open").is_displayed()
        return saveas

    def verify_savedfile(self):
        verify = self.driver.find_element_by_name("Assay Analyzer Version 20191129.2.json").is_displayed()
        self.driver.find_element_by_name("Assay Analyzer Version 20191129.2.json").click()
        return verify

    def verify_importconfirmation(self):
        self.driver.find_element_by_accessibility_id("1").click()
        verify = self.driver.find_element_by_name(
            "Assay Analyzer settings have been successfully imported.").is_displayed()
        self.driver.find_element_by_name("OK").click()
        return verify

    def verify_applychanges(self):
        self.driver.find_element_by_name("Apply").click()

    """testcase 42380"""

    def verify_resetsettings(self):
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_AppLevel_Reset").click()
        verify = self.driver.find_element_by_name(
            "Are you sure you want to reset application settings to default values?").is_displayed()
        self.driver.find_element_by_name("OK").click()
        self.driver.find_element_by_name("Apply").click()
        return verify

    """testcase T42295"""

    def verify_columncsv(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_ColumnsByCSVType").click()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_ColumnsByCSVTypeView_ColumnsListBySelectedType_ColumnName_Target_Index").click()
        self.driver.find_element_by_name("Apply").click()

    def verify_savedcsvcol(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_ColumnsByCSVType").click()

        verify = self.driver.find_element_by_name("Target_Index").is_selected()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_ColumnsByCSVTypeView_ColumnsListBySelectedType_ColumnName_Target_Index").click()
        self.driver.find_element_by_name("Apply").click()
        return verify

    """testcase T42376"""

    def verify_thumbnail(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_Thumbnails").click()
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_ThumbnailsView_ImageQualityLevel_Low").is_displayed()
        return verify

    def verify_thumbnail1(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_ThumbnailsView_ImageQualityLevel_Medium").is_displayed()
        return verify

    def verify_thumbnail2(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_ThumbnailsView_ImageQualityLevel_High").is_displayed()
        return verify

    def verify_thumbnail3(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_ThumbnailsView_ImageQualityLevel_Original").is_displayed()
        self.driver.find_element_by_name(
            "Pen and Channel area").click()
        self.driver.find_element_by_name("Apply").click()
        return verify

    def verify_changedthumbnail(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_Thumbnails").click()
        verify = self.driver.find_element_by_name(
            "Pen and Channel area").is_selected()
        # self.driver.find_element_by_name("Pen area").click()
        # self.driver.find_element_by_name("Apply").click()
        return verify

    """testcase T42377"""

    def verify_thumbnailalert(self):
        for x in range(0, 3):
            self.driver.find_element_by_accessibility_id("IncreaseButton").click()
        time.sleep(2)
        verify = self.driver.find_element_by_name("Original quality will consume more memory then usual").is_displayed()
        self.driver.find_element_by_name("OK").click()
        return verify

    def verify_default(self):
        for x in range(0, 3):
            self.driver.find_element_by_accessibility_id("DecreaseButton").click()
        self.driver.find_element_by_name("Apply").click()

    """testcase T42296"""

    def verify_thumbnaildisplay(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_Thumbnails").click()
        time.sleep(2)
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_ThumbnailsView_ThumbnailInfos_Assay").is_displayed()

        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_ThumbnailsView_ThumbnailInfos_Assay").click()
        self.driver.find_element_by_name("Apply").click()
        return verify

    """testcase T42297"""

    def verify_workbookcolumn(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_DefaultColumns").click()

        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnsView_DefaultColumns_Add").click()

        verify = self.driver.find_element_by_name("ADD NEW DEFAULT COLUMN").is_displayed()
        return verify

    def verify_addcolumn(self):
        actionchains = ActionChains(self.driver)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_ColumnName").click()

        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_ColumnName").send_keys("demo")

        time.sleep(2)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_ColumnTypes").click()
        time.sleep(3)
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actionchains.send_keys(Keys.RETURN).perform()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_Alternates_Add").click()

        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_Apply").click()

    def verify_addedcolumn(self):
        actionchains = ActionChains(self.driver)
        time.sleep(2)
        self.driver.find_element_by_name("PenId").click()
        for x in range(0, 18):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()

        newcol = self.driver.find_element_by_name("demo").is_displayed()
        # self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Apply").click()
        return newcol

    """testcase T42299"""

    def verify_updatecol(self):
        actionchains = ActionChains(self.driver)
        self.driver.find_element_by_name("demo").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnsView_DefaultColumns_Edit").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_ColumnTypes").click()
        time.sleep(3)
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actionchains.send_keys(Keys.RETURN).perform()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_Apply").click()

    def verify_editwin(self):
        self.driver.find_element_by_name("demo").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnsView_DefaultColumns_Edit").click()
        time.sleep(3)
        editwin = self.driver.find_element_by_name("EDIT 'DEMO' COLUMN").is_displayed()
        return editwin

    def verify_changedcol(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_ColumnTypes").click()
        verify = self.driver.find_element_by_name("Boolean").is_displayed()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_Close").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_Cancel").click()
        return verify

    """testcase T42381"""

    def verify_reloadpaneoption(self):
        self.driver.find_element_by_name("Workbook").click()
        verify = self.driver.find_element_by_name("Reload panes with chips").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Cancel").click()
        return verify

    def verify_selectreloadpane(self):
        actionchains = ActionChains(self.driver)

        # self.driver.find_element_by_name("Reload panes with chips").click()
        check = self.driver.find_elements_by_class_name("CheckBox")
        actionchains.move_to_element(check[1]).perform()
        # check[0].click()
        time.sleep(2)
        # verify = self.driver.find_element_by_name("Reload panes with chips").is_selected()
        # return verify

    """testcase T42393"""

    def verify_defaultparam(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_WorkbookTypes"
        ).click()
        chipcheck = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Item_CLD").is_displayed()

        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Item_CLD").click()

        return chipcheck

    def verify_sectionformulas(self):
        verify = self.driver.find_element_by_name("Formulas:").is_displayed()
        return verify

    def verify_doublingtime(self):
        verify = self.driver.find_element_by_name("DoublingTime").is_displayed()
        return verify

    def verify_rQP(self):
        verify = self.driver.find_element_by_name("rQP").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Apply").click()
        return verify

    def removehistory(self):
        appdata = os.getenv('APPDATA')
        try:
            if os.path.isfile(appdata + "\Assay Analyzer 2.0\D37712\History.xml"):
                os.remove(appdata + "\Assay Analyzer 2.0\D37712\History.xml")
        except:
            print("history file not found")

    def verify_section1ingallery(self):
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("CellElement_0_0").click()
        time.sleep(2)
        verify = self.driver.find_element_by_name("DoublingTime: ").is_displayed()
        return verify

    def verify_section2ingallery(self):
        self.driver.find_element_by_accessibility_id("CellElement_0_0").click()
        time.sleep(2)
        verify = self.driver.find_element_by_name("rQP: ").is_displayed()
        return verify

    """testcase T42419"""

    def verify_columnsections(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_ColumnsByCSVType").click()
        time.sleep(3)
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_ColumnsByCSVTypeView_ColumnsListBySelectedType_ColumnIsSelected_CellType").is_selected()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_ColumnsByCSVTypeView_ColumnsListBySelectedType_ColumnName_CellType").click()

        # self.driver.find_element_by_name("CellType").click()
        self.driver.find_element_by_name("Apply").click()
        return verify

    def verify_unselectattrcolumn(self):
        self.driver.find_element_by_accessibility_id("CellElement_0_0").click()
        time.sleep(2)
        try:
            verify = self.driver.find_element_by_name("CellType: ").is_displayed()
            return verify
        except:
            b = False
            return b

    """testcase T42440"""

    def verify_defaultThemeviews(self):
        verify = self.driver.find_element_by_name("Theme").is_displayed()
        return verify

    def verify_theme1(self):
        verify = self.driver.find_element_by_name("Primary color scheme:").is_displayed()
        return verify

    def verify_theme2(self):
        verify = self.driver.find_element_by_name("Secondary color scheme:").is_displayed()
        return verify

    def verify_importsection(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_Import").is_displayed()
        return verify

    def verify_exportsection(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_Export").is_displayed()
        return verify

    def verify_Resetsection(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_Reset").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Cancel").click()
        return verify

    """testcase T42441"""

    def verify_alternatename(self):
        actionchains = ActionChains(self.driver)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_DefaultColumns").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnsView_DefaultColumns_Add").click()
        actionchains = ActionChains(self.driver)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_ColumnName").click()

        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_ColumnName").send_keys("demo")

        time.sleep(2)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_ColumnTypes").click()
        time.sleep(3)
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actionchains.send_keys(Keys.RETURN).perform()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_Alternates_Add").click()

        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_Apply").click()
        self.driver.find_element_by_name("PenId").click()
        for x in range(0, 18):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        self.driver.find_element_by_name("demo").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnsView_DefaultColumns_Edit").click()

        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_Alternates_Add").click()
        time.sleep(3)
        verify = self.driver.find_element_by_name("demo1").is_displayed()
        return verify

    def verify_renamealternate(self):
        actionchains = ActionChains(self.driver)
        alt = self.driver.find_element_by_name("demo1")
        actionchains.double_click(alt).perform()
        edit = self.driver.find_elements_by_class_name("TextBox")
        edit[1].click()
        keyboard.press('backspace')
        alert = self.driver.find_element_by_name("Alternate name must be unique").is_displayed()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_WbLevel_DefaultColumnEditorView_Close").click()
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Cancel").click()
        return alert

    """testcase T42447"""

    def verify_Targetcols(self):
        actionchains = ActionChains(self.driver)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_ColumnsByCSVType").click()
        time.sleep(2)
        self.driver.find_element_by_name("TargetBased").click()
        time.sleep(2)
        self.driver.find_element_by_name("PenId").click()
        for x in range(0, 6):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()

        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_ColumnsByCSVTypeView_ColumnsListBySelectedType_ColumnIsSelected_Area_Pixels").is_selected()
        return verify

    def verify_targetcol1(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_ColumnsByCSVTypeView_ColumnsListBySelectedType_ColumnIsSelected_Median_Brightness").is_selected()
        return verify

    def verify_targetcol2(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_ColumnsByCSVTypeView_ColumnsListBySelectedType_ColumnIsSelected_Max_Background_Brightness").is_selected()
        return verify

    def verify_targetcol3(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_ColumnsByCSVTypeView_ColumnsListBySelectedType_ColumnIsSelected_DiameterMicrons"
        ).is_selected()
        self.driver.find_element_by_name("Objective").click()
        return verify

    def verify_targetcol4(self):
        actionchains = ActionChains(self.driver)
        for x in range(0, 5):
            actionchains.send_keys(Keys.ARROW_DOWN).perform()
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_ColumnsByCSVTypeView_ColumnsListBySelectedType_ColumnIsSelected_CentroidX_Microns").is_selected()
        return verify

    def verify_targetcol5(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_ColumnsByCSVTypeView_ColumnsListBySelectedType_ColumnIsSelected_CentroidY_Microns").is_selected()
        desktop = str(os.path.join(Path.home(), "Desktop\D37712"))
        try:
            if os.path.isfile(desktop + "\Assay Analyzer Version 20191129.2.json"):
                os.remove(desktop + "\Assay Analyzer Version 20191129.2.json")
        except:
            print("json file not found")
        return verify

    """Template Builder"""

    """testcase T42349"""

    def verify_Template(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_DataImportTemplate").click()

        verify = self.driver.find_element_by_name("CLD").is_displayed()
        return verify

    def verify_templatechip(self):
        verify = self.driver.find_element_by_name("T-Cells").is_displayed()
        return verify

    def verify_addbuttonenable(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Add").is_enabled()
        return verify

    def verify_importbuttonenable(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Import").is_enabled()
        return verify

    def verify_editbuttondisable(self):
        try:
            verify = self.driver.find_element_by_accessibility_id(
                "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Edit").is_enabled()
            return verify
        except:
            b = False
            return b

    def verify_copybuttondisable(self):
        try:
            verify = self.driver.find_element_by_accessibility_id(
                "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Copy").is_enabled()
            return verify
        except:
            b = False
            return b

    def verify_removebuttondisable(self):
        try:
            verify = self.driver.find_element_by_accessibility_id(
                "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Remove").is_enabled()
            return verify
        except:
            b = False
            return b

    def verify_exportbuttondisable(self):
        try:
            verify = self.driver.find_element_by_accessibility_id(
                "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Export").is_enabled()
            return verify
        except:
            b = False
            return b

    def verify_removechipdisable(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Item_CLD"
        ).click()
        try:
            verify = self.driver.find_element_by_accessibility_id(
                "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Remove").is_enabled()
            return verify
        except:
            b = False
            return b

    def cancel(self):
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Cancel").click()

    """testcase T42350"""

    def verify_newdataimport(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Add").click()
        time.sleep(2)
        verify = self.driver.find_element_by_name("ADD NEW DATA TEMPLATE").is_displayed()
        return verify

    def verify_templatewindow(self):
        actionchains = ActionChains(self.driver)
        name = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplateEditorView_TemplateName")
        name.click()
        time.sleep(1)
        name.send_keys("test")
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplateEditorView_TemplateTypes"
        ).click()
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actionchains.send_keys(Keys.RETURN).perform()
        time.sleep(2)
        self.driver.find_element_by_name("ADD NEW DATA TEMPLATE").click()
        csv = self.driver.find_elements_by_class_name("RadWatermarkTextBox")
        # print(csv)
        csv[2].click()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplateEditorView_TemplateItems_Item_Empty"
        ).click()
        combo = self.driver.find_elements_by_class_name("RadComboBox")
        combo[1].click()
        actionchains.send_keys(Keys.ARROW_DOWN).perform()
        actionchains.send_keys(Keys.RETURN).perform()
        csv[1].click()
        csv[1].send_keys("csvtest")
        csv[3].click()
        csv[3].send_keys("Processed Data")
        csv[5].click()
        csv[5].send_keys("LoadCellCount.csv")
        preview = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplateEditorView_TemplateItems_ItemOpenRegexEditorForCsvCommand_Tejas.Services.Entities.TemplateItem"
        )
        print(preview)
        preview.click()
        verify = self.driver.find_element_by_name("REGEX EXPRESSION EDITOR").is_displayed()
        return verify

    def verify_editorcsv(self):
        verify = self.driver.find_element_by_name("...\D37712_LoadCellCount.csv").is_displayed()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_RegexEditorView_Close").click()
        return verify

    def verify_savedtemplate(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplateEditorView_Apply"
        ).click()
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Item_Test"
        ).is_displayed()
        # self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Apply").click()
        return verify

    """testcase T42351"""

    def verify_editsavedtemp(self):
        actionchains = ActionChains(self.driver)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Item_Test"
        ).click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Edit"
        ).click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplateEditorView_TemplateItems_CSVType_PenBased").click()
        keyboard.press('down')
        keyboard.press('enter')
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplateEditorView_Apply"
        ).click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Item_Test"
        ).click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Edit"
        ).click()
        verify = self.driver.find_element_by_name("CSV Filter criteria").is_displayed()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplateEditorView_Apply"
        ).click()
        # self.driver.find_element_by_accessibility_id(
        #     "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Remove").click()
        return verify

    """testcase T42352"""

    def verify_copytemplate(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Item_Test"
        ).click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Copy").click()

        verify = self.driver.find_element_by_name("EDIT 'TEST' DATA TEMPLATE").is_displayed()
        return verify

    def verify_changecopy(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplateEditorView_TemplateItems_CSVType_TargetBased").click()
        keyboard.press('up')
        keyboard.press('enter')

        try:
            verify = self.driver.find_element_by_name("CSV Filter criteria").is_displayed()
            return verify
        except:
            b = False
            return b

    def verify_savedcopy(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplateEditorView_Apply"
        ).click()
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Item_Test-Copy"
        ).is_displayed()
        return verify

    """testcase T42353"""

    def verify_removetemp(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Item_Test-Copy"
        ).click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Remove").click()

        try:
            verify = self.driver.find_element_by_accessibility_id(
                "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Remove").is_displayed()
            return verify

        except:
            b = False
            return b

    """testcase T42354"""

    def verify_exporttemplate(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Item_Test"
        ).click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Export").click()
        time.sleep(4)
        verify = self.driver.find_element_by_name("Save As").is_displayed()
        self.driver.find_element_by_accessibility_id("1").click()
        try:
            time.sleep(3)
            data = self.driver.find_element_by_name("Save As")
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            self.driver.find_element_by_name("Yes").click()

        self.driver.find_element_by_name("OK").click()
        return verify

    def verify_exportedtemplate(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Export").click()
        linedown = self.driver.find_elements_by_accessibility_id("DownButton")
        print(linedown)
        for x in range(0, 4):
            linedown[1].click()

        verify = self.driver.find_element_by_name("test.chiptemplate").is_displayed()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("2").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Item_Test"
        ).click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Remove").click()
        return verify

    """testcase T42355"""

    def verify_importtemplate(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Import").click()
        verify = self.driver.find_element_by_name("Open").is_displayed()
        return verify

    def verify_selecttemplate(self):
        verify = self.driver.find_element_by_name("test.chiptemplate").is_displayed()
        self.driver.find_element_by_name("test.chiptemplate").click()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("1").click()
        return verify

    def verify_templateinlist(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_DataImportTemplatesView_Templates_Item_Test"
        ).is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Cancel").click()
        return verify

    """testcase T42356"""

    def createfiltertemp(self):
        actionchains = ActionChains(self.driver)
        filter = self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_ContextMenu_ElementsTree_Element_Filter2")
        actionchains.context_click(filter).perform()
        self.driver.find_element_by_name("Create Filter Template").click()
        verify = self.driver.find_element_by_name("FILTER TEMPLATE CREATION").is_displayed()
        self.driver.find_element_by_class_name("TextBox").click()
        self.driver.find_element_by_class_name("TextBox").send_keys("demotemp")
        self.driver.find_element_by_name("OK").click()
        time.sleep(2)
        filter = self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_ContextMenu_ElementsTree_Element_Filter2")
        actionchains.context_click(filter).perform()
        self.driver.find_element_by_name("Create Filter Template").click()
        verify = self.driver.find_element_by_name("FILTER TEMPLATE CREATION").is_displayed()
        self.driver.find_element_by_class_name("TextBox").click()
        self.driver.find_element_by_class_name("TextBox").send_keys("demotemp1")
        self.driver.find_element_by_name("OK").click()
        return verify

    def verify_savedfiltertemp(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_FilterTemplate").click()
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_FilterTemplatesView_Templates_Item_Demotemp").is_displayed()
        return verify

    def verify_savedfiltertemp1(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_FilterTemplatesView_Templates_Item_Demotemp1").is_displayed()
        # self.driver.find_element_by_name(
        #     "Application").click()
        return verify

    """testcase T42358"""

    def verify_workflowtype(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_WorkbookTypes"
        ).click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Add"
        ).click()
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_ManageWorkflowView"
        ).is_displayed()
        return verify

    def verify_workflowname(self):
        verify = self.driver.find_element_by_name("Name :").is_displayed()
        return verify

    def verify_dataimport(self):
        verify = self.driver.find_element_by_name("Data Import Templates").is_displayed()
        return verify

    def verify_filtertemp(self):
        verify = self.driver.find_element_by_name("Filter Templates").is_displayed()
        return verify

    def verify_filterSave(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_ManageWorkflowView_Apply"
        ).is_displayed()
        return verify

    def verify_filterCancel(self):
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_Cancel"
        ).is_displayed()
        return verify

    def verify_entername(self):
        # actionchains=ActionChains(self.driver)
        name = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_ManageWorkflowView_WorkflowName"
        )
        name.click()
        name.send_keys("demoflow")
        self.driver.find_element_by_name("Filter Templates").click()

        try:
            check = self.driver.find_element_by_accessibility_id(
                "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_EditableFilterTemplateItemView_Templates_Item_Demotemp").is_selected()
            return check

        except:
            b = False
            return b

    def verify_checkfiltertemp(self):
        try:
            check = self.driver.find_element_by_accessibility_id(
                "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_EditableFilterTemplateItemView_Templates_Item_Demotemp1").is_selected()
            return check

        except:
            b = False
            return b

    def verify_saveworkflow(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_ManageWorkflowView_Apply"
        ).click()
        time.sleep(2)
        verify = self.driver.find_element_by_name("demoflow").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Apply").click()
        return verify

    def verify_savedbook(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_WorkbookTypes"
        ).click()
        self.driver.find_element_by_name("demoflow").click()
        verify = self.driver.find_element_by_name("demoflow").is_displayed()
        return verify

    """testcase T42359"""

    def verify_editworbook(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Edit").click()
        name = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_ManageWorkflowView_WorkflowName"
        )
        name.click()
        name.send_keys("edit")
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_ManageWorkflowView_Apply"
        ).click()
        time.sleep(2)
        verify = self.driver.find_element_by_name("demoflowedit").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Apply").click()
        return verify

    """testcase T42360"""

    def verify_copyworkbook(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_WorkbookTypes"
        ).click()
        self.driver.find_element_by_name("demoflowedit").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Copy"
        ).click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_ManageWorkflowView_Apply"
        ).click()
        verify = self.driver.find_element_by_name("demoflowedit - Copy").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Apply").click()
        return verify

    """testcase T42361"""

    def verify_removeworkbook(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_WorkbookTypes"
        ).click()
        self.driver.find_element_by_name("demoflowedit - Copy").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Remove"
        ).click()
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Apply").click()

    def verify_removedworkbook(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_WorkbookTypes"
        ).click()
        try:
            verify = self.driver.find_element_by_name("demoflowedit - Copy").is_displayed()
            return verify
        except:
            b = False
            return b

    def verify_applysetting(self):
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Apply").click()

    """testcase T42362"""

    def verify_selectedtemplate(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_WorkbookTypes"
        ).click()
        self.driver.find_element_by_name("demoflowedit").click()
        verify = self.driver.find_element_by_name("CLD").is_displayed()
        return verify

    def verify_Formula1(self):
        verify = self.driver.find_element_by_name("DoublingTime").is_displayed()
        return verify

    def verify_Formula2(self):
        verify = self.driver.find_element_by_name("rQP").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Apply").click()
        return verify

    """testcase T42363"""

    def verify_editbackbutton(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_SettingsMenu_MenuElement_WorkbookTypes"
        ).click()
        self.driver.find_element_by_name("demoflowedit").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_WorkflowsView_Workflows_Edit").click()
        verify = self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_ManageWorkflowView_Cancel"
        ).is_displayed()
        return verify

    def verify_unchangedworkbook(self):
        self.driver.find_element_by_accessibility_id(
            "AutomationId_SettingsWindow_AppLevel_TemplateBuilder_ManageWorkflowView_Cancel"
        ).click()
        verify = self.driver.find_element_by_name("demoflowedit").is_displayed()
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Apply").click()
        return verify

    """testcase T42364"""

    def verify_wrkbookinfile(self):
        self.driver.find_element_by_accessibility_id("AutomationId_MainWindow_NavigationMenu_MenuElement_File").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id(
            "AutomationId_MainWindow_NavigationMenu_MenuElement_NewWorkbook").click()
        time.sleep(2)
        verify = self.driver.find_element_by_name("demoflowedit").is_displayed()
        # self.driver.find_element_by_name("Graphs").click()
        return verify

    """testcase T42365"""

    def verify_templateinwrkbook(self):
        self.driver.find_element_by_name("demoflowedit").click()
        try:
            time.sleep(3)
            data = self.driver.find_element_by_name("CONFIRMATION")
            data1 = data.is_displayed()
        except:
            data1 = False

        if data1 == True:
            self.driver.find_element_by_name("Cancel").click()

    """testcase T42375"""

    def verify_Filterbuilder(self):
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Cancel").click()
        self.driver.find_element_by_accessibility_id(
            "AutomationId_WorkbookExplorer_AdditionalButton_AddChipFolder(s)").click()
        self.driver.find_element_by_name("Desktop").click()
        self.driver.find_element_by_name("D37712").click()
        # driver.find_element_by_accessibility_id("0").click()
        self.driver.find_element_by_accessibility_id("1").click()

    def canceltempwindow(self):
        self.driver.find_element_by_accessibility_id("AutomationId_SettingsWindow_Cancel").click()
