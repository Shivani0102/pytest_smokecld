from assaycld import assaycld
import csvcld
import allure
import pytest

global test_case_ids

test_case_ids = [222466, 222468, 222469, 222470, 222471, 222475, 222476, 222480, 222481, 222482, 222483, 222485, 222486,
                 222488, 222489, 222490, 222491, 222492, 222493, 222494, 222498, 222499, 222500, 222502, 222507, 222508,
                 222511, 222513, 222514, 222515, 222523, 222531, 222532, 222538, 222540, 222543, 222544, 222545, 222546,
                 222547, 222548, 222549, 222550, 222551, 222552, 222553, 222556, 222558, 222560, 222562, 222564, 222568,
                 222569, 222570, 222571, 239898, 239900, 239903, 239905, 239907, 239912, 239913, 239914, 239915, 239916,
                 239917, 239921, 239922, 239925, 239926, 239927, 239928, 239929, 239930, 239932, 239937, 239940, 239941,
                 239931, 222622, 222623,
                 222624, 222625, 222626, 222631, 222633, 222636, 222637, 222638, 222643, 222642, 222644, 222645, 222647,
                 222648,
                 222651, 222652,
                 222653, 222656, 222657, 222659, 222661, 222666, 222668, 222667, 222669, 222670, 222671, 222672, 222673,
                 222674, 222676, 222677, 222679, 222680, 222681, 222682, 222683, 222684, 222685, 222686, 222687, 222688,
                 222689,
                 222690,
                 222691, 222693, 222694, 222695, 222696, 222697, 222698, 222699, 222700, 222703
                 ]

global execution_time
execution_time = []

global update_testrail
update_testrail = True

"""test case 222466"""
test = ""


@allure.title('this is the test title')
def test_Start_222466(driver):
    global lp
    lp = assaycld(driver)
    global test
    test = str(test_case_ids[0])
    lp.time_start()
    if update_testrail == True:
        print("got it")
        lp.createTestRun(test_case_ids)


def stop():
    # print("stop")
    time = lp.time_stop()
    execution_time.append(time)


def Time():
    print("time")
    time = 0
    execution_time.append(time)


def case_fields():
    print("case field")
    lp.case_fields(test)


def fail_update():
    print("fail update")
    lp.updateTestCase(test, "fail")


def pass_update():
    pass
    lp.updateTestCase(test, "pass")


def teardwn():
    if update_testrail == True:
        # print("teardown")
        lp.closeTestRun()
    csvcld.write_csv(execution_time, "datacld_test.csv")


"""test case C222468"""


def test_maximize_222468():
    global test
    test = str(test_case_ids[1])
    lp.maximize()
    lp.time_start()


"""testcase 222469"""


def test_logoverify_222469():
    global test
    test = str(test_case_ids[2])
    lp.time_start()
    response = lp.logo_verify()
    assert response == True, "logo not found"


"""testcase C222470"""


def test_versionnumber_222470():
    global test
    test = str(test_case_ids[3])
    verify = lp.verify_version_number()
    assert verify == True, "version number not found"


"""testcase T222471"""


def test_verifyshortinfo():
    global test
    test = str(test_case_ids[4])
    verify = lp.verify_shortinformation()
    assert verify == True, "content not found"


"""testcase C222475"""


def test_verifyfilterwind_222475():
    global test
    test = str(test_case_ids[5])
    verify = lp.verify_filterbuilder()
    assert verify == True, "filter builder window not found"


"""testcase T35914"""


def test_verifydataimporttemplateselements():
    # global test
    # test = "126379"
    lp.verify_data_import_templates_element()
    cld = lp.verify_data_import_templates_element_cld()
    assert cld == True, "cld not found"
    add = lp.verify_data_import_templates_element_add()
    assert add == True, "add button not found"
    edit = lp.verify_data_import_templates_element_edit()
    assert edit == True, "edit button not found"
    copy = lp.verify_data_import_templates_element_copy()
    assert copy == True, "copy button not found"
    remove = lp.verify_data_import_templates_element_remove()
    assert remove == True, "Remove button not found"
    imp = lp.verify_data_import_templates_element_import()
    assert imp == True, "import button not found"
    export = lp.verify_data_import_templates_element_export()
    assert export == True, "export button not found"


"""testcase T35915"""


def test_verifyworkbooktypeelement():
    # global test
    # test = "126387"
    lp.time_start()
    lp.verify_workbook_type_element()
    custom = lp.verify_workbook_type_element_custom()
    assert custom == True, "custom not found"
    add = lp.verify_workbook_type_element_add()
    assert add == True, "add button not found"
    edit = lp.verify_workbook_type_element_edit()
    assert edit == True, "edit button not found"
    copy = lp.verify_workbook_type_element_copy()
    assert copy == True, "copy button not found"
    remove = lp.verify_workbook_type_element_remove()
    assert remove == True, "remove button not found"


"""testcase T35885"""


def test_workbookexplorer():
    # global test
    # test = "747"
    lp.time_start()
    save = lp.workbook_explorer_save()
    assert save == True, "save button not found"
    openworkbook = lp.workbook_explorer_openworkbook()
    assert openworkbook == True, "open workbook button not found"
    addchip = lp.workbook_explorer_addchip()
    assert addchip == True, "add chip button not found"
    addfilter = lp.workbook_explorer_addfilter()
    assert addfilter == True, "add filter button not found"
    addgraph = lp.workbook_explorer_addgraph()
    assert addgraph == True, "add graph button not found"


"""Testcase T36382"""


def test_openworkbooktype():
    # global test
    # test = "126395"
    lp.time_start()
    verify = lp.open_workbook_type()
    assert verify == True, "CLD workbook not open"


"""testcase T35886"""


def test_addchip():
    # global test
    # test = "748"
    lp.time_start()
    chip = lp.add_chip()
    assert chip == True, "chip not found"


"""testcase C222476"""


def test_verifyexpander_222476():
    global test
    test = str(test_case_ids[6])
    lp.time_start()
    verify = lp.verify_expander()
    assert verify == True, "expander not working"


"""testcase T35887"""


def test_verifyoptionchip():
    # global test
    # test = "749"
    lp.time_start()
    lp.verify_option_chip()
    timeline = lp.verify_timeline()
    assert timeline == True, "view in timeline not found"
    gallery = lp.verify_gallery()
    assert gallery == True, "view in gallery not found"
    rawdata = lp.verify_rawdata()
    assert rawdata == True, "view in rawdata not found"
    remove = lp.verify_remove()
    assert remove == True, "remove not found"
    reload = lp.verify_reload()
    assert reload == True, "reload not found"
    folder = lp.verify_containing_folder()
    assert folder == True, "containing folder not found"


"""testcase C222480"""


def test_verifyremovechip():
    global test
    test = str(test_case_ids[7])
    lp.time_start()
    verify = lp.verify_removechip()
    assert verify == False, "chip not removed"


"""testcase C222481"""


def test_verifysavebutton_222481():
    global test
    test = str(test_case_ids[8])
    lp.time_start()
    chip = lp.add_chip()
    assert chip == True, "chip not found"
    verify = lp.verify_saveworkbookbutton()
    assert verify == True, "explorer pane not found"


"""testcase 222482"""


def test_usersaveworkbook_222482():
    global test
    test = str(test_case_ids[9])
    lp.time_start()
    lp.verify_usersaveworkbook()
    # assert verify == True, "workbook not saved"


"""testcase C222483"""


def test_openworkbook_222483():
    global test
    test = str(test_case_ids[10])
    lp.time_start()
    lp.verify_changeworkbook()
    lp.add_chip()
    verify = lp.verify_useropenworkbook()
    assert verify == True, "workbook not found"


"""testcase T42384"""

"""containinffolder"""

"""testcase 222485"""


def test_graphscreen_222485():
    global test
    test = str(test_case_ids[11])
    lp.time_start()
    lp.verify_changeworkbook()
    verify = lp.verify_graphbutton()
    assert verify == True, "graph window not found"


"""testcase C222486"""


def test_verify_reloadchip_222486():
    global test
    test = str(test_case_ids[12])
    lp.time_start()
    lp.add_chip()
    lp.verify_reloadchips()


"""testcase C222488"""


def test_verifychippopup_222488():
    global test
    test = str(test_case_ids[13])
    lp.time_start()
    verify = lp.verify_chipconfirmation()
    assert verify == True, "chip has been removed"


"""testcase C222489"""


def test_verify_draganddropui_222489():
    global test
    test = str(test_case_ids[14])
    lp.time_start()
    verify = lp.verify_draganddropui()
    assert verify == True, "ui has been changed"


"""testcase C222490"""


def test_opentimeline_222490():
    global test
    test = str(test_case_ids[15])
    lp.time_start()
    verify = lp.verify_opentimeline()
    assert verify == "Chip Timeline"


"""testcase C222491"""


def test_verify_switchtimeline_222491():
    global test
    test = str(test_case_ids[16])
    lp.time_start()
    verify = lp.verify_switchtimeline()
    assert verify == True, "chip timeline is not switched"


"""testcase C222492 and C222495"""


def test_chiptimelineimagesequence_222492():
    global test
    test = str(test_case_ids[17])
    lp.time_start()
    lp.timeline_image_sequence_expander()
    sequence1 = lp.timeline_image_sequence1()
    assert sequence1 == True, "image sequence not found"
    sequence2 = lp.timeline_image_sequence2()
    assert sequence2 == True, "image sequence not found"
    sequence3 = lp.timeline_image_sequence3()
    assert sequence3 == True, "image sequence not found"
    sequence4 = lp.timeline_image_sequence4()
    assert sequence4 == True, "image sequence not found"


"""testcase C222493"""


def test_verifychiptimelineelement_222493():
    global test
    test = str(test_case_ids[18])
    lp.time_start()
    view = lp.verify_chiptimeline_timeline_view()
    assert view == True, "timeline view not found"
    grid = lp.verify_chiptimeline_matching_grid()
    assert grid == True, "matching grid not found"


"""testcase C222494"""


def test_verify_timelinegridview_222494():
    global test
    test = str(test_case_ids[19])
    lp.time_start()
    verify = lp.verify_timelinegridview()
    assert verify == True, "image sequence not found"


"""testcase C222498"""


def test_verify_removechipfromtimeline_222498():
    global test
    test = str(test_case_ids[20])
    lp.time_start()
    verify = lp.verify_removechipfromtimeline()
    assert verify == False, "chip not deleted from timeline"


"""testcase C222499"""


def test_verify_selectedchipdata_222499():
    global test
    test = str(test_case_ids[21])
    lp.time_start()
    verify = lp.verify_selectedchipdata()
    assert verify == True, "chipdata  not found"


"""testcase C222500"""


def test_verify_timelinehistoryfile_222500():
    global test
    test = str(test_case_ids[22])
    lp.time_start()
    verify = lp.verify_timelinehistoryfile()
    assert verify == True

    # """"testcase 42301"""

    #
    # def test_verify_openhistoryxml():
    #     global test
    #     test = "42301"
    #     lp.time_start()
    #     verify = lp.verify_openhistoryxml()
    #     assert verify == True, "csv path not found"


""""testcase C222502"""


def test_verify_imageseqxml_222502():
    global test
    test = str(test_case_ids[23])
    lp.time_start()
    verify = lp.verify_imageseqxmlforempty()
    assert verify == True, "empty type not found"
    verify1 = lp.verify_imageseqxmlforload()
    assert verify1 == True, "load type not found"
    verify2 = lp.verify_imageseqxmlforassay()
    assert verify2 == True, "assay type not found"
    verify3 = lp.verify_imageseqxmlforculture()
    assert verify3 == True, "culture type not found"
    # lp.close_timeline()


def test_closetimeline():
    lp.time_start()
    lp.close_timeline()


"""testcase 754"""


def test_rawdata():
    # global test
    # test = "754"
    lp.time_start()
    verify = lp.open_raw_data()
    assert verify == "Raw Data"


"""testcase C222507"""


def test_verify_groupbyfeature_222507():
    global test
    test = str(test_case_ids[24])
    lp.time_start()
    lp.verify_groupbyfeature()
    verify1 = lp.verify_groupbypenid1()
    assert verify1 == True, "penid groupby not found for 1"
    verify2 = lp.verify_groupbypenid2()
    assert verify2 == True, "penid groupby not found for 2"
    verify3 = lp.verify_groupbypenid3()
    assert verify3 == True, "penid groupby not found for 3"


"""testcase C222508"""


def test_verify_hierarichalgrouping_222508():
    global test
    test = str(test_case_ids[25])
    lp.time_start()
    lp.verify_hierarichalgrouping()
    verify = lp.verify_groupbyemptypenid1()
    assert verify == "1", "empty penid1 not found"
    verify1 = lp.verify_groupbyemptypenid2()
    assert verify1 == "D37712", "empty penid2 not found"
    # verify2 = lp.verify_groupbyemptypenid3()
    # assert verify2 == True, "empty penid3


"""testcase 222511"""


def test_verify_addparamusingcompoperator_222511():
    global test
    test = str(test_case_ids[26])
    lp.time_start()
    lp.verify_addparameterusingcompoperator()
    lp.verify_otherattribute()
    verify = lp.raw_data_verify_parameter1()
    assert verify == True, "compparameter1 not added"


"""testcase C222513"""


def test_verify_Cparameteringrid_222513():
    global test
    test = str(test_case_ids[27])
    lp.time_start()
    verify = lp.verify_Cparameteringrid()
    assert verify == True, "added Cparameter is not found in grid"


"""testcase C222514"""


def test_verify_parameteringallery_222514():
    global test
    test = str(test_case_ids[28])
    lp.time_start()
    lp.close_raw_data()
    verify = lp.open_gallery()
    assert verify == "Gallery"
    verify = lp.verify_parameteringallery()
    assert verify == True, "parameter not found in gallery attribute"


"""testcase C222515"""


def test_verifyremoveparameter_222515():
    global test
    test = str(test_case_ids[29])
    lp.time_start()
    lp.close_gallery()
    lp.open_raw_data()
    lp.remove_new_parameter()


"""testcase T42253"""
"""Lparamater"""

"""testcase C222523"""


def test_verify_logparameter_222523():
    global test
    test = str(test_case_ids[30])
    lp.verify_logparameter()
    lp.verify_logselect()
    lp.verify_movetoright()
    lp.verify_selectattribute()
    verify = lp.raw_data_verify_Logparameter()
    assert verify == True, "logparameter not found"


"""testcase C222531"""


def test_verify_attrinexpressioneditor_222531():
    global test
    test = str(test_case_ids[31])
    lp.time_start()
    verify = lp.verify_attrinexpressioneditor()
    assert verify == True, "assay not found"
    verify1 = lp.verify_cultureattr()
    assert verify1 == True, "culture not found"


"""testcase C222532"""


def test_verify_editnumericvalue_222532():
    global test
    test = str(test_case_ids[32])
    lp.time_start()
    verify = lp.verify_editnumericvalue()
    assert verify == "21", "numeric value not changed"
    verify1 = lp.verify_changetodefault()
    assert verify1 == "1", "numeric value not changed to default"


#
def test_closerawdata():
    lp.time_start()
    lp.close_raw_data()


"""filter builder"""


def test_clickfilter():
    # global test
    # test = "781"
    lp.time_start()
    verify = lp.click_filter()
    assert verify == "Filter Builder"


"""testcase T35899"""


def test_addchipinfilter():
    # global test
    # test = "782"
    lp.time_start()
    lp.add_chip_in_filter()


"""testcase T35900"""


def test_filtername():
    # global test
    # test = "783"
    lp.time_start()
    lp.filter_name("fil")


"""testcase T35901"""


def test_addconditioninfilter():
    # global test
    # test = "784"
    lp.time_start()
    lp.add_condition_filter()
    penid = lp.penid()
    assert penid == True, "penid not found"
    state = lp.pen_state()
    assert state == True, "penstate not found"
    loadpenid = lp.load_pen_filter()
    assert loadpenid == True, "load penid not found"
    deviceid = lp.load_device_id()
    assert deviceid == True, "load device id not found"
    countverified = lp.load_cell_count_verified()
    assert countverified == True, "load cell count verified not found"
    cellcount = lp.load_cell_count()
    assert cellcount == True, "cell count not found"
    lp.abc()


"""testcase T35902"""


def test_filterbuildersetminmax():
    global test
    # test = "785"
    # lp.time_start()
    verify = lp.filter_builder_set_min()
    assert verify == True, "min button not found"
    verify1 = lp.filter_builder_set_max()
    assert verify1 == True, "ax button not found"
    verify2 = lp.filter_builder_increase()
    assert verify2 == True, "min and max button not working"


"""testcase C222538"""


def test_verify_stringtypeparameter_222538():
    global test
    test = str(test_case_ids[33])
    lp.time_start()
    verify = lp.verify_stringtypeparameter()
    assert verify == True, "Pens:  not found"
    verify1 = lp.verify_stringtypeparameter1()
    assert verify1 == True, "Total:  not found"


"""testcase T35903"""


def test_filtersavebuttononed():
    # global test
    # test = "787"
    lp.time_start()
    lp.filter_close()
    verify = lp.filter_save_button_oned()
    assert verify == True, "1-D filter not saved"


"""testcase C222540"""


def test_verify_addmultiplecondition_222540():
    global test
    test = str(test_case_ids[34])
    lp.time_start()
    lp.click_filter()
    lp.add_chip_in_filter()
    lp.filter_name("filter1")
    lp.add_condition_filter()
    lp.abc()
    lp.filter_builder_set_min()
    lp.filter_builder_set_max()
    lp.filter_builder_increase()
    lp.verify_addmultiplecondition()
    lp.verify_scndcond()
    lp.verify_stringtypeparameter1()
    verify = lp.verify_gettotalpencount()
    assert verify == "1687", "count not verified"


def test_close_fil():
    lp.close_filter()
    lp.verify_openexplorer()
    lp.open_gallery()
    verify1 = lp.verify_selectgalleryfilter()
    assert verify1 == "Visible 1687 of 1758 pens", "count not matched"
    lp.close_gallery()


"""testcase T42235"""
"""boolean"""

"""testcase C222543"""


def test_verify_openfilterwindow_222543():
    global test
    test = str(test_case_ids[35])
    lp.time_start()
    verify = lp.verify_savedfilter()
    assert verify == True, "saved filter not found"
    verify1 = lp.verify_openfilterwindow()
    assert verify1 == True, "edit filter window not found"
    lp.verify_closefilter()


"""testcase C222544"""


def test_verify_openchipfromfilter_222544():
    global test
    test = str(test_case_ids[36])
    lp.time_start()
    verify = lp.verify_openchipfromfilter()
    assert verify == "1758", "pen count not matched"
    lp.verify_closefilter()


"""testcase C222545"""


def test_verify_disableenablefilter_222545():
    global test
    test = str(test_case_ids[37])
    lp.time_start()
    lp.verify_disableenablefilter()
    verify = lp.disabletoggle()
    assert verify == False, "condition 1 is not disabled"
    verify1 = lp.verify_secondtoggledisable()
    assert verify1 == False, "condition 2 not disabled"


"""testcase C222546"""


def test_verify_deletefiltercond_222546():
    global test
    test = str(test_case_ids[38])
    lp.time_start()
    verify = lp.verify_deletefiltercond()
    assert verify == False, "condition not removed"
    verify1 = lp.verify_getpencountafterdeletion()
    assert verify1 == True, "correct pen count not found"


"""testcase C222547"""


def test_verify_editfiltername_222547():
    global test
    test = str(test_case_ids[39])
    lp.close_filter()
    lp.verify_openexplorer()
    lp.verify_editfiltername()
    lp.verify_removename()
    verify1 = lp.verify_changedname()
    assert verify1 == True, "filter name not edited"


"""testcase C222548"""


def test_verify_filterclick_222548():
    global test
    test = str(test_case_ids[40])
    lp.time_start()
    verify = lp.verify_filterclick()
    assert verify == True, "filter window not found"


"""testcase C222549"""


def test_verify_removefilter_222549():
    global test
    test = str(test_case_ids[41])
    lp.time_start()
    verify = lp.verify_removefilter()
    assert verify == False, "filter not removed"


"""testcase C222550"""


def test_verify_customparaminfilter_222550():
    global test
    test = str(test_case_ids[42])
    lp.click_filter()
    lp.add_chip_in_filter()
    lp.filter_name("cust")
    lp.add_condition_filter()
    verify = lp.verify_customparaminfilter()
    assert verify == True, "custom parameter not found"


"""testcase C222551"""


def test_verify_filterconditionusingparam_222551():
    global test
    test = str(test_case_ids[43])
    lp.time_start()
    verify = lp.verify_filterconditionusingparam()
    assert verify == "829", "count not found"
    lp.close_filter()


"""testcase C222552"""


def test_verify_filterpen_222552():
    global test
    test = str(test_case_ids[44])
    lp.time_start()
    lp.verify_openexplorer()
    lp.open_gallery()
    lp.verify_filterpen()
    lp.close_gallery()
    lp.click_filter()
    lp.add_chip_in_filter()
    lp.filter_name("filterpen")
    lp.add_condition_filter()
    lp.verify_selectfilter()
    lp.close_filter()
    lp.verify_openexplorer()
    lp.open_gallery()
    verify = lp.verif_filteringallery()
    assert verify == True, "rejected pen not visible"


def test__closegall():
    lp.close_gallery()


"""testcase C222553"""


def test_verify_validationmessage_222553():
    global test
    test = str(test_case_ids[45])
    lp.time_start()
    verify = lp.verify_validationmessage()
    assert verify == True, "validation message not found"


"""testcase T35983"""


def test_filtertwodcondition():
    # global test
    # test = "126398"
    lp.time_start()
    lp.click_filter()
    lp.add_chip_in_filter()
    lp.filter_name("filter2")
    lp.filter_twod_condition()
    xaxis = lp.filter_twod_xaxis()
    assert xaxis == True, "xaxis combobox not found"
    yaxis = lp.filter_twod_yaxis()
    assert yaxis == True, "yaxis combobox not found"
    # verify = lp.filter_verify_chart()
    # assert verify == True, "2-D Condition not working"


"""testcase T35984"""


def test_filtertwodconditonsave():
    # global test
    # test = "126399"
    lp.time_start()
    lp.verify_savefilter()


"""testcase C222556"""


def test_verify_changegraph_222556():
    global test
    test = str(test_case_ids[46])
    lp.time_start()
    verify = lp.verify_changegraph()
    assert verify == True, "graph not changed"


"""testcase T42371"""
"""-------------"""

"""testcase C222558"""


def test_verify_expand2dfilter_222558():
    global test
    test = str(test_case_ids[47])
    lp.time_start()
    verify = lp.verify_expand2dfilter()
    assert verify == True, "expanded window not found"


"""testcase C222560"""


def test_verify_2Dconditiontogallery_222560():
    global test
    test = str(test_case_ids[48])
    lp.time_start()
    verify = lp.verify_2Dconditiontogallery()
    assert verify == "0", "pen count not correct"


def test_closefil():
    lp.close_filter()
    lp.verify_openexplorer()
    lp.open_gallery()
    verify = lp.verify_filteringallery()
    assert verify == True, "pen count not matched"


# def test_closegall():
#     lp.close_gallfil()


"""testcase C222562"""


def test_verify_dragtofilter_222562():
    global test
    test = str(test_case_ids[49])
    lp.time_start()
    lp.close_gallfil()
    lp.verify_dragtofilter()
    verify = lp.verify_drggedchip()
    assert verify == True, "added chip not displayed in filter"


"""testcase C222564"""


def test_verify_changesin1D_222564():
    global test
    test = str(test_case_ids[50])
    lp.time_start()
    lp.click_filter()
    lp.add_chip_in_filter()
    lp.filter_name("chng1D")
    lp.add_condition_filter()
    verify = lp.verify_changesin1D()
    assert verify == True, "graph not changed for 1D"


"""testcase C222568"""


def test_verify_decreasinginmultiplecond_222568():
    global test
    test = str(test_case_ids[51])
    lp.time_start()
    lp.verify_addmultiplecondition()
    lp.verify_scndcond()
    verify = lp.verify_decreasinginmultiplecond()
    assert verify == True, "decreasing count not found"


"""testcase C222569"""


def test_verify_removefiltergallery_222569():
    global test
    test = str(test_case_ids[52])
    lp.time_start()
    lp.close_filter()
    lp.verify_openexplorer()
    lp.verify_removefiltergallery()
    lp.open_gallery()
    verify = lp.verify_removedfilter()
    assert verify == False, "filter not removed from gallery"
    lp.click()


"""testcase C222570"""


def test_verify_filterdroprefresh_222570():
    global test
    test = str(test_case_ids[53])
    lp.time_start()
    lp.close_gallfil()
    lp.click_filter()
    verify = lp.verify_filterdroprefresh()
    assert verify == True
    lp.verify_closefilter()
    verify = lp.remove_2ndchip()
    assert verify == False, "2nd chip not removed"


"""testcase C222571"""


def test_verify_filterstuck_222571():
    global test
    test = str(test_case_ids[54])
    lp.open_raw_data()
    lp.click_filter()
    lp.add_chip_in_filter()
    lp.remove_custom_parameter()
    lp.close_raw_data()
    lp.verify_filterstuck()
    # assert verify == True, "filter got stuck"


def test_closefilt():
    lp.verify_closefilter()


"""testcase 753"""


def test_opengallery():
    # global test
    # test = "753"
    lp.time_start()
    verify = lp.open_gallery()
    assert verify == "Gallery"


"""testcase T35969"""


def test_galleryimagesequence():
    # global test
    # test = "768"
    lp.time_start()
    verify = lp.gallery_image_sequence_empty()
    assert verify == True, "empty not found"
    verify1 = lp.gallery_image_sequence_load()
    assert verify1 == True, "Load not found"
    verify2 = lp.gallery_image_sequence_culture()
    assert verify2 == True, "culture not found"
    verify3 = lp.gallery_image_sequence_assay()
    assert verify3 == True, "Assay not found"
    verify4 = lp.gallery_image_sequence_culture2()
    assert verify4 == True, "Culture not found"
    verify5 = lp.gallery_image_sequence_assay2()
    assert verify5 == True, "assay2 not found"


"""TestCase T35893"""


def test_gallersetting():
    # global test
    # test = "767"
    lp.time_start()
    lp.gallery_setting()
    visible = lp.visible()
    assert visible == True, "visible not found"
    show = lp.show_rank()
    assert show == True, "show rank not found"
    column = lp.column_name()
    assert column == True, "column name not found"
    footer = lp.column_footer()
    assert footer == True, "column footer not found"
    height = lp.row_height()
    assert height == True, "row height not found"
    digit = lp.digits_after_comma()
    assert digit == True, "digit after comma not found"
    pen = lp.pen_reject_approval()
    assert pen == True, "pen reject approval not found"


"""testcase C222574"""


def test_verify_rankforselection_239898():
    global test
    test = str(test_case_ids[55])
    lp.time_start()
    verify = lp.verify_emptyrankforselection()
    assert verify == True, "column empty is not selected"
    verify1 = lp.verify_loadrankforselection()
    assert verify1 == True, "column load is not selected"
    lp.verify_removecheckbxselection()
    verify2 = lp.verify_emptyrankfornonselection()
    assert verify2 == False, "column empty is selected"
    verify3 = lp.verify_loadrankfornonselection()
    assert verify3 == False, "column load is selected"
    lp.verify_defaultcheckbxselection()


"""testcase C222576"""


def test_verify_rowheightvalue_239900():
    global test
    test = str(test_case_ids[56])
    lp.time_start()
    verify = lp.verify_rowheightvalue()
    assert verify == "130", "row height value not matched"
    lp.verify_rowheightincrease()
    verify1 = lp.verify_rowheightincreasedvalue()
    assert verify1 == "140", "row height value not increased"


"""testcase C222579"""


def test_verify_reorderingofcolumns_239903():
    global test
    test = str(test_case_ids[57])
    lp.time_start()
    verify = lp.verify_reorderingofcolumns()
    assert verify == "Empty", "header value not found"
    lp.verify_columnchange()
    verify1 = lp.verify_reorderingofchangedcolumns()
    assert verify1 == "Load", "header value not changed"


"""testcase C222581"""


def test_verify_brightnesswindow_239905():
    global test
    test = str(test_case_ids[58])
    lp.time_start()
    verify = lp.verify_brightnesswindow()
    assert verify == True, "brightness window not visible"


"""testcase C222583"""


def test_verify_totalpencount_239907():
    global test
    test = str(test_case_ids[59])
    lp.time_start()
    verify = lp.verify_totalpencount()
    assert verify == "1758", "pen count not found"


"""testcase C222588"""


def test_verify_rejectedpens_239912():
    global test
    test = str(test_case_ids[60])
    lp.time_start()
    verify = lp.verify_beforerejectedpens()
    assert verify == "Pen_2", "pen count not found"
    verify1 = lp.verify_afterrejectedpens()
    assert verify1 == False, "pen not rejected"


"""testcase C222589"""


def test_addeffilter_239913():
    global test
    test = str(test_case_ids[61])
    lp.time_start()
    lp.close_gallery()
    verify = lp.verify_Addedfilterforexlorer()
    assert verify == True, "filter1 not found"
    verify1 = lp.verify_Addedfilter1forexplorer()
    assert verify1 == True, "filter2 not found"
    lp.open_gallery()
    verify3 = lp.verify_Addedfilterforgallery()
    assert verify3 == True, "customfilter not found in gallery"
    verify4 = lp.verify_Addedfilter1forgallery()
    assert verify4 == True, "filter2 not found in gallery"


"""testcase C222590"""


def test_verify_filterredcount_239914():
    global test
    test = str(test_case_ids[62])
    lp.time_start()
    verify = lp.verify_filterredcount()
    assert verify == True, "count not matched"


"""testcase C222591"""


def test_verify_removegalleryfilter_239915():
    global test
    test = str(test_case_ids[63])
    lp.time_start()
    verify = lp.verify_removegalleryfilter()
    assert verify == True, "filter not removed from gallery"


"""testcase C222592"""


def test_verify_changepenstate_239916():
    global test
    test = str(test_case_ids[64])
    lp.time_start()
    verify = lp.verify_changepenstate()
    assert verify == True, "state not changed"
    lp.close_gallery()


"""testcase C222593"""


def test_verify_savedpenstate_239917():
    global test
    test = str(test_case_ids[65])
    lp.time_start()
    lp.open_gallery()
    lp.verify_savedpenstate()
    lp.close_gallery()
    lp.open_gallery()
    verify = lp.verify_selectedpen()
    assert verify == True, "pen not selected"


"""testcase C222597"""


def test_verify_datacolumn_239921():
    global test
    test = str(test_case_ids[66])
    lp.time_start()
    lp.gallery_select_data_attribute()
    verify1 = lp.verify_attribute1()
    assert verify1 == True, "selected attribute not found"
    verify2 = lp.verify_attribute2()
    assert verify2 == True, "selected attribute not found"
    verify3 = lp.verify_attribute3()
    assert verify3 == True, "selected attribute not found"
    verify4 = lp.verify_attribute4()
    assert verify4 == True, "selected attribute not found"


"""testcase C222598"""


def test_validationattrmessage_239922():
    global test
    test = str(test_case_ids[67])
    lp.time_start()
    lp.verify_validationattrmessage()
    verify = lp.verify_displayedmessage()
    assert verify == True, "validation message not found"


"""testcase C222601"""


def test_verify_exporttoarchive_239925():
    global test
    test = str(test_case_ids[68])
    lp.time_start()
    verify = lp.verify_exporttoarchive()
    assert verify == True, "archive button not found"
    verify1 = lp.verify_exporttoarchiveclick()
    assert verify1 == True, "Images only not displayed"
    verify2 = lp.verify_archiveitem1()
    assert verify2 == True, "Images Per Pen not displayed"
    verify3 = lp.verify_archiveitem2()
    assert verify3 == True, "Images Per Image Sequence not found"
    verify4 = lp.verify_archiveitem3()
    assert verify4 == True, "Images and CSVs not found"


"""testcase C222602"""


def test_verify_exportselectedthumb_239926():
    global test
    test = str(test_case_ids[69])
    lp.time_start()
    verify = lp.verify_exportselectedthumb()
    assert verify == True, "file explorer not found"
    # lp.verify_exportdefaultfilename()
    verify1 = lp.verify_exportdefaultfilename()
    assert verify1 == True, "zip file not found"
    verify2 = lp.verify_datainzip()
    assert verify2 == True, "jpg not found"


"""testcase C222603"""


def test_verify_penidforexporting_239927():
    global test
    test = str(test_case_ids[70])
    lp.time_start()
    verify = lp.verify_penidforexporting()
    assert verify == True, "penid window not found"
    lp.verify_rangeforpenid()
    lp.verify_saverangefile()
    verify1 = lp.verify_rangeinzip()
    assert verify1 == True, "range not found"
    verify2 = lp.verify_onlyrangeinzip()
    assert verify2 == True, "different range found"


"""testcase C222604"""


def test_verifyunselectcolumn_239928():
    global test
    test = str(test_case_ids[71])
    lp.time_start()
    verify = lp.verify_selectedcolumn1()
    assert verify == True, "column not found"
    verify1 = lp.verify_selectedcolumn2()
    assert verify1 == True, "column not found"
    lp.verify_unselectcolumn()
    verify2 = lp.verify_unselectedcolumn1()
    assert verify2 == False, "column not removed"
    verify3 = lp.verify_unselectedcolumn1()
    assert verify3 == False, "column not removed"
    lp.verify_changecoltodefault()


"""testcase C222605"""


def test_verify_penrejectiondisabled_239929():
    global test
    test = str(test_case_ids[72])
    lp.time_start()
    verify = lp.verify_penrejectiondisabled()
    assert verify == False, "confirmation message not disabled"
    verify1 = lp.verify_rejectedpen()
    assert verify1 == False, "pen not rejected"


"""testcase C222606"""


def test_verify_rejectionmessage_239930():
    global test
    test = str(test_case_ids[73])
    lp.time_start()
    verify = lp.verify_rejectionmessage()
    assert verify == True, "rejection confirmation message not found"


"""testcase C222608"""


def test_verify_cancelpenreject_239932():
    global test
    test = str(test_case_ids[74])
    lp.time_start()
    verify = lp.verify_cancelpenreject()
    assert verify == True, "cancel button not found"
    verify = lp.verify_cancelrejectedpen()
    assert verify == True, "pen got rejected"


"""testcase C222613"""


def test_verify_archive1000_239937():
    global test
    test = str(test_case_ids[75])
    lp.time_start()
    lp.verify_archive1000()
    verify = lp.verify_range1000inzip()
    assert verify == True, "file is less than 1000pens"


"""testcase C222616"""


def test_verify_unselectpenarchive_239940():
    global test
    test = str(test_case_ids[76])
    lp.time_start()
    lp.verify_unselectpenarchive()
    verify = lp.verify_unselectinzip()
    assert verify == False, "rejected pen not deleted"


"""testcase C222617"""


def test_verify_headersortingpersist_239941():
    global test
    test = str(test_case_ids[77])
    lp.time_start()
    lp.verify_headersortingpersist()
    verify = lp.verify_defaultcolumnsorting()
    assert verify == True, "default column pen not found"
    verify = lp.verify_changedcolumnsorting()
    assert verify == True, "changed column pen not found"
    lp.close_gallery()


"""testcase T35970"""


def test_addgraphbutton():
    # global test
    # test = "875"
    lp.time_start()
    verify = lp.add_graph_button()
    assert verify == "Graph Builder"
    verify1 = lp.add_graph()
    assert verify1 == True, "scatter plot not found"


"""testcase T35971"""


def test_graphbuilderscatterplotelements():
    # global test
    # test = "876"
    lp.time_start()
    verify = lp.graph_builder_graph_type()
    assert verify == True, "graph type not found"
    verify1 = lp.graph_builder_chip()
    assert verify1 == True, "chip not found"
    verify2 = lp.graph_builder_save_button()
    assert verify2 == "Save"
    verify3 = lp.graph_builder_export()
    assert verify3 == True, "export button not found"
    verify4 = lp.graph_builder_setting()
    assert verify4 == True, "setting button not found"
    verify5 = lp.graph_builder_linktogallery()
    assert verify5 == "Link-To-Gallery"
    verify6 = lp.graph_builder_linktorawdata()
    assert verify6 == "Link-To-Raw-Data"
    verify7 = lp.graph_builder_select()
    assert verify7 == "SelectOrZoom"
    verify8 = lp.graph_builder_xaxis()
    assert verify8 == True, "xaxis not found"
    verify9 = lp.graph_builder_yaxis()
    assert verify9 == True, "yaxis not found"
    verify10 = lp.graph_builder_groupby()
    assert verify10 == True, "groupby not found"


"""testcase C222622"""


def test_verify_xandyaxislabels_222622():
    global test
    test = str(test_case_ids[79])
    lp.time_start()
    verify = lp.verify_xaxislabels()
    assert verify == True, "x axis label not found"
    verify1 = lp.verify_yaxislabels()
    assert verify1 == True, "y axis label not found"


"""testcase C222623"""


def test_verify_xandyaxisdropdwn_222623():
    global test
    test = str(test_case_ids[80])
    lp.time_start()
    verify = lp.verify_xaxisdropdown()
    assert verify == True, "Pen_Id option not found"
    verify1 = lp.verify_xaxisdropdown1()
    assert verify1 == True, "Device_Id option not found"
    verify2 = lp.verify_xaxisdropdown2()
    assert verify2 == True, "Cell_Count_Verified option not found"
    verify3 = lp.verify_yaxisdropdown()
    assert verify3 == True, "Pen State option not found"
    verify4 = lp.verify_yaxisdropdown1()
    assert verify4 == True, "Device_Id option not found"
    verify5 = lp.verify_yaxisdropdown2()
    assert verify5 == True, "Cell_Count_Verified option not found"


"""testcase T35972"""


def test_graphbuilderaxisattribute():
    # global test
    # test = "877"
    lp.time_start()
    verify = lp.graph_builder_axis_attribute()
    assert verify == True, "graph not found"


"""testcase C222624"""


def test_verify_groupbyoption_222624():
    global test
    test = str(test_case_ids[81])
    lp.time_start()
    verify = lp.verify_groupbyoption()
    assert verify == True, "Pen State option not found in groupby"
    verify = lp.verify_groupbyoption1()
    assert verify == True, "Device_Id option not found in groupby"
    verify = lp.verify_groupbyoption2()
    assert verify == True, "Cell_Count_Verified option not found in groupby"


"""testcase C222625"""


def test_verify_changegroupby_222625():
    global test
    test = str(test_case_ids[82])
    lp.time_start()
    verify = lp.verify_changegroupby()
    assert verify == True, "legend panel not found"


"""testcase C222626"""


def test_verify_penplotlegends_222626():
    global test
    test = str(test_case_ids[83])
    lp.time_start()
    verify = lp.verify_penplotlegends()
    assert verify == True, "graph range not found"
    verify = lp.verify_penplotlegends1()
    assert verify == False, "graph range not hided"
    lp.verify_gettodefault()


"""testcase C222631"""


def test_verify_linktogallery_222631():
    global test
    test = str(test_case_ids[84])
    lp.time_start()
    verify = lp.verify_linktogallery()
    assert verify == True, "link to gallery button not found"
    verify1 = lp.verify_galleryredirecting()
    assert verify1 == True, "gallery window not found"
    lp.close_gallery()
    lp.close_link()


"""testcase C222633"""


def test_verify_linktorawdata_222633():
    global test
    test = str(test_case_ids[85])
    lp.time_start()
    verify = lp.verify_linktorawdata()
    assert verify == True, "link to raw data button not found"
    verify1 = lp.verify_rawdataredirecting()
    assert verify1 == True, "rawdata window not found"
    lp.close_raw_data()
    lp.close_rawlink()


"""testcase C222636"""


def test_verify_exportgraph_222636():
    global test
    test = str(test_case_ids[86])
    lp.time_start()
    verify = lp.verify_exportgraph()
    assert verify == True, "export graph button not found"
    verify = lp.verify_savedialog()
    assert verify == True, "export graph button not found"
    verify = lp.verify_savefile()
    assert verify == True, "confirmation message not found"
    verify = lp.verify_savedimage()
    assert verify == True, "image saved not found"


"""testcase C222637"""


def test_verify_graphsetting_222637():
    global test
    test = str(test_case_ids[87])
    lp.time_start()
    verify = lp.verify_graphsetting()
    assert verify == True, "setting option not found"
    verify = lp.verify_settingelement1()
    assert verify == True, "Shape option not found"
    verify = lp.verify_settingelement2()
    assert verify == True, "Fill option not found"
    verify = lp.verify_settingelement3()
    assert verify == True, "Height option not found"
    verify = lp.verify_settingelement4()
    assert verify == True, "Width option not found"
    verify = lp.verify_settingelement5()
    assert verify == True, "Stroke option not found"
    verify = lp.verify_settingelement6()
    assert verify == True, "Stroke Thickness option not found"
    verify = lp.verify_settingelement7()
    assert verify == True, "Palette option not found"
    verify = lp.verify_settingelement8()
    assert verify == True, "Selection Color option not found"
    verify = lp.verify_attributes()
    assert verify == True, "Attributes not found"
    verify = lp.verify_preview()
    assert verify == True, "preview not found"
    verify = lp.verify_okbutton()
    assert verify == True, "ok button not found"


"""testcase C222638"""


def test_verify_selecttooltipattr_222638():
    global test
    test = str(test_case_ids[88])
    lp.time_start()
    verify = lp.verify_selecttooltipattr()
    assert verify == True, "penid not selected"
    verify = lp.verify_selecttooltipattr1()
    assert verify == True, "deviceid not selected"
    verify = lp.verify_selecttooltipattr2()
    assert verify == True, "cell count verified not selected"
    verify = lp.verify_selecttooltipattr3()
    assert verify == True, "cell count not selected"
    verify = lp.verify_selecttooltipattr4()
    assert verify == True, "cell type not selected"
    verify = lp.verify_selecttooltipattr5()
    assert verify == True, "timestamp not selected"
    lp.verify_scatterpoints()
    assert verify == True, "scatterpoint don't include penid attribute"


"""testcase C222643"""


def test_verify_emptygraphname_222643():
    global test
    test = str(test_case_ids[89])
    lp.time_start()
    verify = lp.verify_emptygraphname()
    assert verify == True, "save graph window not found"
    verify1 = lp.verify_savegaphwindow()
    assert verify1 == True, "validation message not found"


"""testcase C222642"""


def test_verify_savegraphname_222642():
    global test
    test = str(test_case_ids[90])
    lp.time_start()
    verify = lp.verify_savegraphname()
    assert verify == True, "save graph window not found"
    lp.verify_savegaph()
    lp.close_graph()


"""testcase C222644"""


def test_verify_graphinworkbook_222644():
    global test
    test = str(test_case_ids[91])
    lp.time_start()
    verify = lp.verify_graphinworkbook()
    assert verify == True, "workbook not found in explorer"
    verify = lp.verify_opensavedgraph()
    assert verify == True, "first attribute not pre selected"
    verify = lp.verify_attr()
    assert verify == True, "second attribute not pre selected"
    lp.close_graph()


"""testcase C222645"""


def test_verify_changesavedgraph_222645():
    global test
    test = str(test_case_ids[92])
    lp.time_start()
    lp.verify_changesavedgraph()
    lp.close_graph()
    verify = lp.verify_openchangedgraph()
    assert verify == False, "changes not found in saved graph"
    lp.close_graph()


"""testcase C222647"""


def test_verify_removegraphconf_222647():
    global test
    test = str(test_case_ids[93])
    lp.time_start()
    verify = lp.verify_removegraphconf()
    assert verify == True, "confirmation message not found"
    verify = lp.verify_removedgraph()
    assert verify == False, "graph not removed"


"""testcase C222648"""


def test_verify_stringtypevalidation_222648():
    global test
    test = str(test_case_ids[94])
    lp.time_start()
    verify = lp.add_graph_button()
    assert verify == "Graph Builder"
    verify1 = lp.add_graph()
    assert verify1 == True, "scatter plot not found"
    lp.verify_stringtypevalidation()
    lp.close_graph()
    # verify2 = lp.verify_stringtypevalidation()
    # assert verify2 == True, "validation message not found"


"""testcase T35978"""


def test_graphbuilderhistogram():
    global test
    test = "126365"
    lp.time_start()
    lp.add_graph_histogram()
    verify = lp.histogram_select_attribute()
    assert verify == True, "attribute not selected"
    verify1 = lp.graph_builder_chip()
    assert verify1 == True, "chip dropdown not found"
    verify2 = lp.graph_builder_save_button()
    assert verify2 == "Save"
    verify3 = lp.graph_builder_export()
    assert verify3 == True, "export not found"
    verify4 = lp.graph_builder_linktogallery()
    assert verify4 == "Link-To-Gallery"
    verify5 = lp.graph_builder_linktorawdata()
    assert verify5 == "Link-To-Raw-Data"
    verify6 = lp.histogram_xaxis()
    assert verify6 == True, "histogram xaxis not found"
    verify7 = lp.histogram_bin_value()
    assert verify7 == True, "bin dropdown not found"
    verify8 = lp.histogram_null_value_checkbox()
    assert verify8 == True, "null value"


"""testcase T35979"""


def test_histogramselectxaxis():
    global test
    test = "126366"
    lp.time_start()
    verify = lp.histogram_select_xaxis()
    assert verify == True, "graph not found"


"""testcase C222651"""


def test_verify_changebinquantity_222651():
    global test
    test = str(test_case_ids[95])
    lp.time_start()
    lp.verify_changebinquantity()
    verify = lp.verify_bincount()
    assert verify == True, "range upto 10 not found"
    verify1 = lp.verify_changedbinvalue()
    assert verify1 == True, "changed graph not found"


"""testcase C222652"""


def test_verify_nullablevalues_222652():
    global test
    test = str(test_case_ids[96])
    lp.time_start()
    verify = lp.verify_nullablevalues()
    assert verify == True, "nullable value checkbox not found"
    verify = lp.verify_changedtonull()
    assert verify == True, "changed to nullable value not found"


"""testcase C222653"""


def test_verify_exporthistogram_222653():
    global test
    test = str(test_case_ids[97])
    lp.time_start()
    verify = lp.verify_exporthistogram()
    assert verify == True, "save as explorer not found"
    verify1 = lp.verify_savegraph()
    assert verify1 == True, "confirmation popup not found"
    lp.histogram_save()
    lp.close_graph()
    lp.open_histogram()
    verify = lp.verify_axis()
    assert verify == True, "histogram axis attribute not found"
    verify1 = lp.verify_bin()
    assert verify1 == True, "bin value not found"
    lp.close_graph()


"""testcase C222656"""


def test_verify_edithistogram_222656():
    global test
    test = str(test_case_ids[98])
    lp.time_start()
    lp.verify_edithistogram()
    lp.close_graph()
    lp.open_histogram()
    verify = lp.verify_changedhistogram()
    assert verify == True, "changed bin value not found"
    # lp.close_graph()


def test_closegraph():
    lp.close_graph()


"""testcase C222657"""


def test_verify_removehistogram_222657():
    global test
    test = str(test_case_ids[99])
    lp.time_start()
    lp.verify_removehistogram()
    verify = lp.verify_removedhistogram()
    assert verify == False, "histogram graph not removed"


"""testcase C222659"""


def test_verify_histogramlinkgallery_222659():
    global test
    test = str(test_case_ids[100])
    lp.time_start()
    lp.add_graph_histogram()
    verify = lp.histogram_select_attribute()
    assert verify == True, "attribute not selected"
    lp.verify_linkgallery()
    verify = lp.verify_linktogallery()
    assert verify == True, "link to gallery button not found"
    verify1 = lp.verify_galleryredirecting()
    assert verify1 == True, "gallery window not found"
    lp.close_gallery()
    lp.close_link()


"""testcase C222661"""


def test_verify_histogramlinkraw_222661():
    global test
    test = str(test_case_ids[101])
    lp.time_start()
    verify = lp.verify_linktorawdata()
    assert verify == True, "link to raw data button not found"
    verify1 = lp.verify_rawdataredirecting()
    assert verify1 == True, "rawdata window not found"


def test_closesetting():
    lp.close_raw_data()
    lp.close_rawlink()
    lp.close_graph()


"""Settings"""

"""testcase C222666"""


def test_verify_colortheme_222666():
    global test
    test = str(test_case_ids[102])
    lp.time_start()
    lp.verify_opensettings()
    verify = lp.verify_colortheme()
    assert verify == True, "Dark option not found"
    verify1 = lp.verify_primaryoption()
    assert verify1 == True, "Light option not found"
    verify2 = lp.verify_scndrycolortheme()
    assert verify2 == True, "Blue option not found"
    verify3 = lp.verify_secondaryoption()
    assert verify3 == True, "Orange option not found"


"""testcase C222668"""


def test_verify_exportsettings_222668():
    global test
    test = str(test_case_ids[103])
    lp.time_start()
    verify = lp.verify_exportsettings()
    assert verify == True, "saveas window not found"
    lp.verify_saveexportsetting()
    verify1 = lp.verify_exportconfirmation()
    assert verify1 == True, "export confirmation message not found"


"""testcase C222667"""


def test_verify_importsettings_222667():
    global test
    test = str(test_case_ids[104])
    lp.time_start()
    verify = lp.verify_importsettings()
    assert verify == True, "open window not found"
    verify = lp.verify_savedfile()
    assert verify == True, "file not found"
    verify = lp.verify_importconfirmation()
    assert verify == True, "confirmation message not found"
    lp.verify_applychanges()


"""testcase C222669"""


def test_verify_resetsettings_222669():
    global test
    test = str(test_case_ids[105])
    lp.time_start()
    lp.verify_opensettings()
    verify = lp.verify_resetsettings()
    assert verify == True, "confirmation message not found"


"""testcase C222670"""


def test_verify_columncsv_222670():
    global test
    test = str(test_case_ids[106])
    lp.time_start()
    lp.verify_opensettings()
    lp.verify_columncsv()
    lp.verify_opensettings()
    verify = lp.verify_savedcsvcol()
    assert verify == True, "column not saved for csv"


"""testcase C222671"""


def test_verify_thumbnails_222671():
    global test
    test = str(test_case_ids[107])
    lp.time_start()
    lp.verify_opensettings()
    verify = lp.verify_thumbnail()
    assert verify == True, "Low thumbnail not found"
    verify = lp.verify_thumbnail1()
    assert verify == True, "Medium thumbnail not found"
    verify = lp.verify_thumbnail2()
    assert verify == True, "High thumbnail not found"
    verify = lp.verify_thumbnail3()
    assert verify == True, "Original thumbnail not found"
    lp.verify_opensettings()
    verify = lp.verify_changedthumbnail()
    assert verify == True, "Pen and Channel area not selected"


"""testcase C222672"""


def test_verify_thumbnailalert_222672():
    global test
    test = str(test_case_ids[108])
    lp.time_start()
    verify = lp.verify_thumbnailalert()
    assert verify == True, "alert message not found"
    lp.verify_default()


"""testcase C222673"""


def test_verify_thumbnaildisplay_222673():
    global test
    test = str(test_case_ids[109])
    lp.time_start()
    lp.verify_opensettings()
    verify = lp.verify_thumbnaildisplay()
    assert verify == True, "image type not found"


"""testcase C222674"""


def test_verify_workbookcolumn_222674():
    global test
    test = str(test_case_ids[110])
    lp.time_start()
    lp.verify_opensettings()
    verify = lp.verify_workbookcolumn()
    assert verify == True, "default column window not found"
    lp.verify_addcolumn()
    verify = lp.verify_addedcolumn()
    assert verify == True, "added column not found"


"""testcase C222676"""


def test_verify_updatecol_222676():
    global test
    test = str(test_case_ids[111])
    lp.time_start()
    lp.verify_updatecol()
    verify = lp.verify_editwin()
    assert verify == True, "edit window not found"
    verify = lp.verify_changedcol()
    assert verify == True, "changes not found in default column"


"""testcase C222677"""


def test_verify_reloadpaneoption_222677():
    global test
    test = str(test_case_ids[112])
    lp.time_start()
    lp.verify_opensettings()
    verify = lp.verify_reloadpaneoption()
    assert verify == True, "reload pane checkbox not found"
    # lp.verify_selectreloadpane()
    # assert verify1 == True, "reload pane checkbox is not selected"


"""testcase C222679"""


def test_verify_defaultparam_222679():
    global test
    test = str(test_case_ids[113])
    lp.time_start()
    lp.verify_opensettings()
    verify = lp.verify_defaultparam()
    assert verify == True, "CLD chip not found"
    verify1 = lp.verify_sectionformulas()
    assert verify1 == True, "Formula section not found"
    verify2 = lp.verify_doublingtime()
    assert verify2 == True, "doublint time section not found"
    verify3 = lp.verify_rQP()
    assert verify3 == True, "rQP section not found"
    lp.open_gallery()
    verify4 = lp.verify_section1ingallery()
    assert verify4 == True, "doubling time not found in gallery"
    verify5 = lp.verify_section2ingallery()
    assert verify5 == True, "rQP not found in gallery"
    lp.close_gallery()


"""comment from below"""

"""testcase C222680"""


def test_verify_columnsections_222680():
    global test
    test = str(test_case_ids[114])
    lp.verify_opensettings()
    lp.verify_columnsections()
    lp.open_gallery()
    verify = lp.verify_unselectattrcolumn()
    assert verify == False, "cell type column is not unselected"


def test_closegall():
    lp.close_gallery()


"""testcase C222681"""


def test_verify_defaultThemeviews():
    global test
    test = str(test_case_ids[115])
    lp.time_start()
    lp.verify_opensettings()
    verify = lp.verify_defaultThemeviews()
    assert verify == True, "theme option not found"
    verify1 = lp.verify_theme1()
    assert verify1 == True, "primary color scheme not found"
    verify2 = lp.verify_theme2()
    assert verify2 == True, "secondary color scheme not found"
    verify3 = lp.verify_importsection()
    assert verify3 == True, "Import settings button not found"
    verify4 = lp.verify_exportsection()
    assert verify4 == True, "Export settings button not found"
    verify5 = lp.verify_Resetsection()
    assert verify5 == True, "Reset settings button not found"


"""testcase C222682"""


def test_verify_alternatename_222682():
    global test
    test = str(test_case_ids[116])
    lp.time_start()
    lp.verify_opensettings()
    verify = lp.verify_alternatename()
    assert verify == True, "alternate name not found"
    verify1 = lp.verify_renamealternate()
    assert verify1 == True, "alert message not found"


"""testcase C222683"""


def test_verify_Targetcols_222683():
    global test
    test = str(test_case_ids[117])
    lp.time_start()
    lp.verify_opensettings()
    verify = lp.verify_Targetcols()
    assert verify == True, "Area_Pixels is not selected"
    verify1 = lp.verify_targetcol1()
    assert verify1 == True, "Median_Brightness is not selected"
    verify2 = lp.verify_targetcol2()
    assert verify2 == True, "Max_Background_Brightness is not selected"
    verify3 = lp.verify_targetcol3()
    assert verify3 == True, "Diameter_Microns is not selected"
    verify4 = lp.verify_targetcol4()
    assert verify4 == True, "CentroidX_Microns is not selected"
    verify5 = lp.verify_targetcol5()
    assert verify5 == True, "CentroidY_Microns is not selected"


"""testcase C222684"""


def test_verify_Template_222684():
    global test
    test = str(test_case_ids[118])
    lp.time_start()
    # lp.verify_opensettings()
    verify = lp.verify_Template()
    assert verify == True, "cld chip not found in template"
    verify1 = lp.verify_templatechip()
    assert verify1 == True, "T-cells chip not found in template"
    verify2 = lp.verify_addbuttonenable()
    assert verify2 == True, "add button is not enabled"
    verify3 = lp.verify_importbuttonenable()
    assert verify3 == True, "import button is not enabled"
    verify4 = lp.verify_editbuttondisable()
    assert verify4 == False, "edit button is enabled"
    verify5 = lp.verify_copybuttondisable()
    assert verify5 == False, "copy button is enabled"
    verify6 = lp.verify_removebuttondisable()
    assert verify6 == False, "remove button is enabled"
    verify7 = lp.verify_exportbuttondisable()
    assert verify7 == False, "export button is enabled"
    verify8 = lp.verify_removechipdisable()
    assert verify8 == False, "remove button is enabled for chip"
    # lp.cancel()


"""testcase C222685"""


def test_verify_newdataimport_222685():
    global test
    test = str(test_case_ids[119])
    lp.time_start()
    verify = lp.verify_newdataimport()
    assert verify == True, "New data template window not found"
    verify1 = lp.verify_templatewindow()
    assert verify1 == True, "expression editor window not found"
    verify2 = lp.verify_editorcsv()
    assert verify2 == True, "csv in preview not found"
    verify3 = lp.verify_savedtemplate()
    assert verify3 == True, "Saved template not found"


"""testcase C222686"""


def test_verify_editsavedtemp_222686():
    global test
    test = str(test_case_ids[120])
    lp.time_start()
    verify = lp.verify_editsavedtemp()
    assert verify == True, "changes not saved for template"


"""testcase C222687"""


def test_verify_copytemplate_222687():
    global test
    test = str(test_case_ids[121])
    lp.time_start()
    verify = lp.verify_copytemplate()
    assert verify == True, "edit template window not found"
    verify = lp.verify_changecopy()
    assert verify == False, "changes not found"
    verify = lp.verify_savedcopy()
    assert verify == True, "saved test copy not found"


"""testcase C222688"""


def test_verify_removetemp_222688():
    global test
    test = str(test_case_ids[122])
    lp.time_start()
    verify = lp.verify_removetemp()
    assert verify == True, "test copy template not removed"


"""testcase C222689"""


def test_verify_exporttemplate_222689():
    global test
    test = str(test_case_ids[123])
    lp.time_start()
    verify = lp.verify_exporttemplate()
    assert verify == True, "save as dialog not found"
    verify = lp.verify_exportedtemplate()
    assert verify == True, "exported template not found"


"""testcase C222690"""


def test_verify_importtemplate_222690():
    global test
    test = str(test_case_ids[124])
    lp.time_start()
    verify = lp.verify_importtemplate()
    assert verify == True, "open dialog not found"
    verify1 = lp.verify_selecttemplate()
    assert verify1 == True, "import file not found"
    verify2 = lp.verify_templateinlist()
    assert verify2 == True, "imported template not found"



"""testcase C222691"""


def test_createfiltertemp_222691():
    global test
    test = str(test_case_ids[125])
    lp.time_start()
    verify = lp.createfiltertemp()
    assert verify == True, "filter template creation window not found"
    lp.verify_opensettings()
    verify1 = lp.verify_savedfiltertemp()
    assert verify1 == True, "saved filter template demotemp not found"
    verify2 = lp.verify_savedfiltertemp1()
    assert verify2 == True, "saved filter template demotemp1 not found"
    # lp.verify_resetsettings()


"""testcase C222693"""


def test_verify_workflowtype_222693():
    global test
    test = str(test_case_ids[126])
    lp.time_start()
    # lp.verify_opensettings()
    verify = lp.verify_workflowtype()  # incomplete
    assert verify == True, "workflow window not found"
    verify1 = lp.verify_workflowname()
    assert verify1 == True, "name label not found"
    verify2 = lp.verify_dataimport()
    assert verify2 == True, "Data Import not found"
    verify3 = lp.verify_filtertemp()
    assert verify3 == True, "Filter Templates not found"
    verify4 = lp.verify_filterSave()
    assert verify4 == True, "save button not found"
    verify5 = lp.verify_filterCancel()
    assert verify5 == True, "cancel button not found"
    verify6 = lp.verify_entername()
    assert verify6 == False, "demo is pre-selected"
    verify8 = lp.verify_checkfiltertemp()
    assert verify8 == False, "demo is pre-selected"
    verify9 = lp.verify_saveworkflow()
    assert verify9 == True, "saved workflow not found"
    lp.verify_opensettings()
    verify10 = lp.verify_savedbook()
    assert verify10 == True, "changes to setting not found"


"""testcase C222694"""


def test_verify_editworbook_222694():
    global test
    test = str(test_case_ids[127])
    lp.time_start()
    verify = lp.verify_editworbook()
    assert verify == True, "edited workbook not found"
    lp.verify_opensettings()


"""testcase C222695"""


def test_verify_copyworkbook_222695():
    global test
    test = str(test_case_ids[128])
    lp.time_start()
    verify = lp.verify_copyworkbook()
    assert verify == True, "workbook copy not found"
    lp.verify_opensettings()


"""testcase C222696"""


def test_verify_removeworkbook_222696():
    global test
    test = str(test_case_ids[129])
    lp.time_start()
    lp.verify_removeworkbook()
    lp.verify_opensettings()
    verify = lp.verify_removedworkbook()
    assert verify == False, "demoflowedit - Copy workbook not removed"
    lp.verify_applysetting()
    lp.verify_opensettings()


"""testcase C222697"""


def test_verify_selectedtemplate_222697():
    global test
    test = str(test_case_ids[130])
    lp.time_start()
    verify = lp.verify_selectedtemplate()
    assert verify == True, "selected data template not found"
    verify = lp.verify_Formula1()
    assert verify == True, "selected formula1 not found"
    verify = lp.verify_Formula2()
    assert verify == True, "selected formula2 not found"


"""testcase C222698"""


def test_verify_editbackbutton_222698():
    global test
    test = str(test_case_ids[131])
    lp.time_start()
    lp.verify_opensettings()
    verify = lp.verify_editbackbutton()
    assert verify == True, "backbutton not found"
    verify1 = lp.verify_unchangedworkbook()
    assert verify1 == True, "unchanged demoflowedit workbook not found"


"""testcase C222699"""


def test_verify_wrkbookinfile_222699():
    global test
    test = str(test_case_ids[132])
    lp.time_start()
    verify = lp.verify_wrkbookinfile()
    assert verify == True, "workbooktype not found in file > new workbook"


"""testcase C222700"""


def test_verify_templateinwrkbook_222700():
    global test
    test = str(test_case_ids[133])
    lp.time_start()
    lp.verify_templateinwrkbook()
    lp.verify_opensettings()
    verify1 = lp.verify_savedfiltertemp()
    assert verify1 == True, "saved filter template demotemp not found"
    verify2 = lp.verify_savedfiltertemp1()
    assert verify2 == True, "saved filter template demotemp1 not found"


"""testcase C222703"""


def test_verify_filterbuilder_222703():
    global test
    test = str(test_case_ids[134])
    lp.time_start()
    lp.verify_Filterbuilder()
    lp.verify_opensettings()
    verify1 = lp.verify_savedfiltertemp()
    assert verify1 == True, "saved filter template demotemp not found"
    verify2 = lp.verify_savedfiltertemp1()
    assert verify2 == True, "saved filter template demotemp1 not found"
    lp.canceltempwindow()


"""testcase C222607"""


def test_verify_rejectallpens_239931():
    global test
    test = str(test_case_ids[78])
    lp.time_start()
    lp.open_gallery()
    verify = lp.verify_rejectallpens()
    assert verify == True, "PenRejectApproval is not checked"
    verify1 = lp.verify_clickrejectpen()
    assert verify1 == True, "confirmation message not found"
    verify2 = lp.verify_rejectedpen1()
    assert verify2 == False, "pen_4 not rejected"
    verify3 = lp.verify_rejectedpen2()
    assert verify3 == False, "pen_5 not rejected"
    lp.close_gallery()


"""----------------------------------------------------------------------"""


def test_removeworkbook():
    lp.deleteworkbook()


"""-----------------------------------------------------------------------------------------------------------------------"""
"""old"""


def test_close():
    lp.time_start()
    lp.close()
