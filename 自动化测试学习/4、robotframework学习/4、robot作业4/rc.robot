*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Keywords ***
Setup WebTest
    Open Browser   http://localhost/mgr/login/login.html    chrome
    Set Selenium Implicit Wait   10

TearDown WebTest
    Close Browser

DeleteAllCourse
    Loginwebsite
    set selenium implicit wait  2
    :For   ${one}  IN RANGE  99
        \  sleep  1
        \  ${html}=  Get Webelement  tag=html
#        \  ${eles}=  Evaluate   $html.find_elements_by_css_selector("*[ng-click^='delOne']")
        \  ${eles}=  Get Webelements   css=*[ng-click^='delOne']
        \  Exit For Loop If   $eles==[]
        \  Click Element   @{eles}[0]
        \  sleep  1
        \  Click Element   xpath=//div[@class='bootstrap-dialog-footer-buttons']//button[2]
    TearDown WebTest
    Set Selenium Implicit Wait   10

Loginwebsite
    Open Browser   http://localhost/mgr/login/login.html    chrome
    Set Selenium Implicit Wait   10
    input text       id = username    auto
    input text       id = password    sdfsdfsdf
    click element    css = button

Addcourse
    [Arguments]     ${name}      ${desc}    ${displayidx}
    #添加课程按钮
    click element    xpath = //div[@class='ng-scope']//button//span
    #输入课程名称
    input text      xpath = //div[@ng-if='showAddOne']//input[1]    ${name}
    #详情描述
    input text      xpath = //div[@ng-if='showAddOne']//textarea    ${desc}
    #展示次序
    input text      xpath = //div[@ng-if='showAddOne']//input[2]    ${displayidx}
    #点击创建课程按钮
    click element   xpath = //button[@ng-click='addOne()']

GetcourseList
    ${eles} =     Get Webelements    xpath = //tr[@total-items]//td[2]
    ${lessons} =     create list
    :FOR  ${ele}  IN  @{eles}
        \   log to console  ${ele.text}
        \    Append To List    ${lessons}   ${ele.text}
    [Return]  ${lessons}













